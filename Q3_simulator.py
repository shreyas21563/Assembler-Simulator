#   Format to decide

import re


def decimal_to_binary(n):
    L = ""
    while(n>0):
        L += str(n%2)
        n = n//2
    
    return (16-len(L))*"0" + L[::-1]
def binary_to_decimal(str_val):
    ans = 0
    s = str_val[::-1]
    for i in range(0, len(str_val)):
        if s[i]=='1':
            ans += (2**i)
    return ans
def floater_to_binary(a):
    f = str(a)
    
    ans = f.split(".")
    x = int(ans[0])
    bin_ans = decimal_to_binary(x)
    y = ans[1]
    y_actual = "0." + y
    s = float(y_actual)
    ans_float = ''
    if(int(y_actual[2:]) == 0):
        ans_float += "00000"
    else:
        for i in range(5):
            if(s>=1):
                s -= 1
            x_new = str(float(s*2))
            
            # elif(int(x_new[2:]) == 0 and i!=0):
            #     ans_float += '1'
            #     ans_float += (5-i)*'0'
            #     break

            ans_float += x_new[0]
            
            s = s*2
    fin = bin_ans[:] + "." + ans_float
    fin_ans = ''
    fin_ans = str(float(fin))
    fin_ans += '00000'
    a = fin_ans.split(".")
    expo = 0
    mantissa = ''
    if(int(a[0])!=0):
        expo = fin_ans.index('.')-1
        count = 0
        i = 1
        while(count<5):
            if(fin_ans[i]!='.'):
                mantissa += fin_ans[i]
                count += 1
            i += 1
    expo_new = decimal_to_binary(expo)
    if(expo_new==""):
        expo_new = "0"
    if(mantissa==""):
        mantissa = "00000"
    return [expo_new, mantissa]
#print(floater_to_binary(2.5))
dict_opcode = {
    '10000': ['add', 'TypeA'],
    '00000': ['addf','TypeA'],
    '10001' : ['sub', 'TypeA'],
    '00001' : ['subf','TypeA'],
    '10110' : ['mul', 'TypeA'], 
    '11010' : ['xor', 'TypeA'], 
    '11011' : ['or', 'TypeA'],
    '11100' : ['and', 'TypeA'],
    '10010' : ['movB', 'TypeB'],
    '00010' : ['movf','TypeB'],
    '11000' : ['rs', 'TypeB'],
    '11001' : ['ls', 'TypeB'],
    '10011' : ['movC', 'TypeC'],
    '10111' : ['div', 'TypeC'],
    '11101' : ['not', 'TypeC'],
    '11110' : ['cmp', 'TypeC'],
    '10100' : ['ld', 'TypeD'],
    '10101' : ['st', 'TypeD'],
    '11111' : ['jmp', 'TypeE'],
    '01100' : ['jlt', 'TypeE'],
    '01101' : ['jgt', 'TypeE'],
    '01111' : ['je', 'TypeE'],
    '01010' : ['hlt', 'TypeF']
}
dict_register={
    "000":"R0",
    "001":"R1",
    "010":"R2",
    "011":"R3",
    "100":"R4",
    "101":"R5",
    "110":"R6",
    "111":"FLAGS"
    }

#*************

def EnglishA(L):
    # A = [7, 10, 13]
    list = []
    list.append(dict_register[L[7:10]])
    list.append(dict_register[L[10:13]])
    list.append(dict_register[L[13:16]])
    return list

def EnglishB(L):
    # B = [5, 8]
    list = []
    list.append(dict_register[L[5:8]])
    list.append(binary_to_decimal(L[8:]))
    return list
def binary_to_dec(x,y,z):
    p = x.split(".")
    a = p[0]
    if len(p)>1:
        b=p[1]
        sum1 = 0
        for i in range(len(b)):
            sum1= float(p[1][i])*2**(-(i+1))+sum1
    a = int(a)
    y =int(y)
    z = int(z)
    
    num =a
    s=""
    r=0
    i=0
    sum =0
    while num!=0:
        r = num%10
        if r!=0:
            sum = sum+r*2**i
        num = num //10
        i+=1
    s = s+ str(sum)
    if len(p)>1:
        return sum +sum1
    else:
        return sum
#print(binary_to_dec("1.01101",2,10))

def EnglishB2(L):
    list = []
    list.append(dict_register[L[5:8]])
    a = L[8:]
    exp = binary_to_decimal(a[:3])
    real_str = '1.'+ a[3:]
    #real_str = real_str[:exp+1]+"."+real_str[exp+1:]
    real_str = binary_to_dec(real_str,2,10)
    x= (2**exp)*real_str
    list.append(str(x))
    return list
# print(binary_to_dec("1.0010",2,10))

def EnglishC(L):
    # C = [10, 13]
    list = []
    list.append(dict_register[L[10:13]])
    list.append(dict_register[L[13:16]])
    return list

def EnglishD(L):
    # D = [5, 8]
    list = []
    list.append(dict_register[L[5:8]])
    list.append(binary_to_decimal(L[8:])) 
    return list

def EnglishE(L):
    # E = [8]
    list = []
    list.append(binary_to_decimal(L[8:])) 
    return list

#*************

instruction = []
list_english = []
memory = []
bits = '0000000000000000'

register_val = {
    "R0" : 0,
    "R1" : 0,
    "R2" : 0,
    "R3" : 0,
    "R4" : 0,
    "R5" : 0,
    "R6" : 0,
    "FLAGS" : "0000000000000000"
}




#******************

#   Type A

def add(a, b, c):
    if(register_val[a] + register_val[b] > 65535):
        register_val[c] = (register_val[a] + register_val[b])%65536
        register_val["FLAGS"] = "0000000000001000"
    elif(register_val[a] + register_val[b] <65536):       #here change is required
        register_val["FLAGS"] = "0000000000000000"
        register_val[c] = register_val[a] + register_val[b]
        #register_val_binary[c] = decimal_to_binary(register_val[c])
    return
def addf(a,b,c):
    if(register_val[a] + register_val[b] >252):
        register_val[c] = 252.0
        register_val["FLAGS"] = "0000000000001000"
    if (register_val[a]+register_val[b]<=252):                 #here change is required
        register_val["FLAGS"] = "0000000000000000"
        register_val[c] = register_val[a]+register_val[b]
def sub(a, b, c):   #Incomplete
    if(register_val[a] - register_val[b] < 0):
        register_val[c] = 0
        
        register_val["FLAGS"] = "0000000000001000" 
    elif(register_val[a] - register_val[b] < 65536):
        register_val["FLAGS"] = "0000000000000000"
        register_val[c] = register_val[a] - register_val[b]
    return
def subf(a, b, c):   #Incomplete
    if(register_val[a] - register_val[b] < 1):
        register_val[c] = 0.0
        register_val["FLAGS"] = "0000000000001000" 
    elif(register_val[a] - register_val[b] < 252):
        register_val["FLAGS"] = "0000000000000000"
        register_val[c] = register_val[a] - register_val[b]
    return
def mul(a, b, c):
    if(register_val[a] * register_val[b] >= 65536):
        register_val[c] = (register_val[a] * register_val[b])%65536   #here check is required
        register_val["FLAGS"] = "0000000000001000"
    elif(register_val[a] * register_val[b] <65536):                       #here 
        register_val["FLAGS"] = "0000000000000000"
        register_val[c] = register_val[a] * register_val[b]
    return

def xor(a, b, c):
    register_val["FLAGS"] = "0000000000000000"
    register_val[c] = (register_val[a]^register_val[b])
    return

def AND(a, b, c):
    register_val["FLAGS"] = "0000000000000000"
    register_val[c] = (register_val[a]&register_val[b])
    return 

def OR(a, b, c):
    register_val["FLAGS"] = "0000000000000000"
    register_val[c] = (register_val[a]|register_val[b])
    return  

#   Type B 

def movB(a, b):
    register_val["FLAGS"] = "0000000000000000"
    register_val[a] = b
    return
def movf(a,b):
    register_val["FLAGS"] = "0000000000000000"
    register_val[a] = b
def ls(a, imm):
    for i in range(0, imm):
        register_val[a] *= 2 
    register_val["FLAGS"] = "0000000000000000"
def rs(a, imm):
    for i in range(0, imm):
        register_val[a] = int(register_val[a]/2)
    register_val["FLAGS"] = "0000000000000000"
#   Type C

def movC(a, b):
    register_val[a] = register_val[b]
    register_val["FLAGS"] = "0000000000000000"
    return

def div(a, b):
    register_val["R0"] = int(register_val[a]/register_val[b])
    register_val["R1"] = register_val[a]%register_val[b]
    register_val["FLAGS"] = "0000000000000000"
    return

def Not(a, b):
    X = decimal_to_binary(register_val[a])   
    Y = ""
    for i in X:
        if i=="0":
            Y += "1"
        else:
            Y += "0"
    register_val[b] = binary_to_decimal
    register_val["FLAGS"] = "0000000000000000"
    return

def cmp(a, b):
    if(register_val[a]==register_val[b]):
        register_val["FLAGS"] = "0000000000000001"
    elif(register_val[a]<register_val[b]):
        register_val["FLAGS"] = "0000000000000100"
    elif(register_val[a]>register_val[b]):
        register_val["FLAGS"] = "0000000000000010"
    return

#   Type D

def st(a, b):
    memory[b] = decimal_to_binary(register_val[a])
    register_val["FLAGS"] = "0000000000000000"

def ld(a, b):
    register_val[a] = binary_to_decimal(memory[b])
    register_val["FLAGS"] = "0000000000000000"

#   Type E

def jlt():
    if(register_val["FLAGS"][-3]=="1"):
        register_val["FLAGS"] = "0000000000000000"
        return True
    register_val["FLAGS"] = "0000000000000000"
    return False

def jgt():
    if(register_val["FLAGS"][-2]=="1"):
        register_val["FLAGS"] = "0000000000000000"
        return True
    register_val["FLAGS"] = "0000000000000000"
    return False

def je():
    if(register_val["FLAGS"][-1]=="1"):
        register_val["FLAGS"] = "0000000000000000"
        return True
    register_val["FLAGS"] = "0000000000000000"
    return False

#******************

while(1):
    try:
        line = input() 
    except EOFError:
        break
    memory.append(line)
    instruction.append(line)
for i in range(len(instruction), 256):
    memory.append(bits)
for i_main in instruction:
    ty = dict_opcode[i_main[0:5]][1]
    ins = dict_opcode[i_main[0:5]][0]
    str_val = ""
    if ty=='TypeF':
        list_english.append('hlt')
    elif ty=='TypeA':
        list = EnglishA(i_main)
        str_val +=ins + " " + list[0] + " " + list[1] + " " + list[2]
        list_english.append(str_val)
    elif ty=='TypeB':
        if (ins=='movf'):                                  # movf decimal value is dealt here
            list = EnglishB2(i_main)
            str_val +=ins + " " + list[0] + " " + str(list[1])
            #print(list,str_val)
            list_english.append(str_val)
        else:
            list = EnglishB(i_main)
            str_val +=ins + " " + list[0] + " " + str(list[1])
            list_english.append(str_val)
    elif ty=='TypeC':
        list = EnglishC(i_main)
        str_val +=ins + " " + list[0] + " " + list[1]
        list_english.append(str_val)
    elif ty=='TypeD':   
        list = EnglishD(i_main)
        str_val +=ins + " " + list[0] + " " + str(list[1])
        list_english.append(str_val)
    elif ty=='TypeE':
        list = EnglishE(i_main)
        str_val +=ins + " " + str(list[0])
        list_english.append(str_val)

PC = 0

FLAG = False

while(1):
    X = PC
    string = list_english[PC].split(" ")
    if(string[0]=="hlt"):
        register_val["FLAGS"] = "0000000000000000"
        FLAG = True
    if(string[0]=="add"):
        add(string[1], string[2], string[3])
        PC += 1
    if (string[0]=="addf"):                    #addf
        addf(string[1],string[2],string[3])
        PC+=1
    elif(string[0]=="sub"):
        sub(string[1], string[2], string[3])
        PC += 1
    elif(string[0]=="subf"):
        subf(string[1],string[2],string[3])    #subf
        PC+=1
    elif(string[0]=="mul"):
        mul(string[1], string[2], string[3])
        PC += 1
    elif(string[0]=="xor"):
        xor(string[1], string[2], string[3])
        PC += 1
    elif(string[0]=="or"):
        OR(string[1], string[2], string[3])
        PC += 1
    elif(string[0]=="and"):
        AND(string[1], string[2], string[3])
        PC += 1
    elif(string[0]=="movB"):
        movB(string[1], int(string[2]))
        PC += 1
    elif(string[0]=="movf"):
        movf(string[1],float(string[2]))
        PC+=1
    elif(string[0]=="ls"):
        ls(string[1], int(string[2]))  
        PC += 1 
    elif(string[0]=="rs"):    
        rs(string[1], int(string[2]))
        PC += 1
    elif(string[0]=="movC"):
        movC(string[1], string[2])
        PC+=1
    elif(string[0]=="div"):
        div(string[1], string[2])
        PC+=1   
    elif(string[0]=="not"):   
        Not(string[1], string[2])
        PC+=1
    elif(string[0]=="cmp"):
        cmp(string[1], string[2])
        PC += 1
    elif(string[0]=="ld"):
        ld(string[1], int(string[2]))
        PC += 1
    elif(string[0]=="st"):
        st(string[1], int(string[2]))
        PC += 1
    elif(string[0]=="jmp"):
        register_val["FLAGS"] = "0000000000000000"
        PC = int(string[1]) - 1
    elif(string[0]=="jlt"):
        if(jlt()):
            PC = int(string[1]) - 1
        else:
            PC += 1
        
    elif(string[0]=="jgt"):
        if(jgt()):
            PC = int(string[1]) - 1
        else:
            PC += 1
    elif(string[0]=="je"):
        if(je()):
            PC = int(string[1]) - 1
        else:
            PC += 1

    print(decimal_to_binary(X)[8:], end = " ")
    if (type(register_val["R0"])==int or register_val["R0"]==0):

        print(decimal_to_binary(register_val["R0"]), end =" ")
    else:
        a = floater_to_binary(register_val["R0"])
        b = a[1]
        print("00000000"+str(a[0][13:16])+b, end =" ")
    if (type(register_val["R1"])==int or register_val["R1"]==0):

        print(decimal_to_binary(register_val["R1"]), end =" ")
    else:
        a = floater_to_binary(register_val["R1"] )
        b = a[1]
        print("00000000"+str(a[0][13:16])+b, end =" ")
    if (type(register_val["R2"])==int or register_val["R2"]==0):
        print(decimal_to_binary(register_val["R2"]), end =" ")
    else:
        a = floater_to_binary(register_val["R2"])
        b = a[1]
        print("00000000"+str(a[0][13:16])+b, end =" ")
    if (type(register_val["R3"])==int or register_val["R3"]==0):
        print(decimal_to_binary(register_val["R3"]), end =" ")
    else:
        a = floater_to_binary(register_val["R3"])
        b = a[1]
        print("00000000"+str(a[0][13:16])+b, end =" ")
    if (type(register_val["R4"])==int or register_val["R4"]==0):
        print(decimal_to_binary(register_val["R4"]), end =" ")
    else:
        a = floater_to_binary(register_val["R4"])
        b = a[1]
        print("00000000"+str(a[0][13:16])+b, end =" ")
    if (type(register_val["R5"])==int or register_val["R5"]==0):
        print(decimal_to_binary(register_val["R5"]), end =" ")
    else:
        a = floater_to_binary(register_val["R5"])
        b = a[1]
        print("00000000"+str(a[0][13:16])+b, end =" ")
    if (type(register_val["R6"])==int or register_val["R6"]==0):
        print(decimal_to_binary(register_val["R6"]), end =" ")
    else:
        a = floater_to_binary(register_val["R6"])
        b = a[1]
        print("00000000"+str(a[0][13:16])+b, end =" ")
    print(register_val["FLAGS"])
    
    if(FLAG):
        break
for j in memory:
    print(j)