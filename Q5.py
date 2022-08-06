import math

dict_size = {
    'KB' : 10,
    'MB' : 20,
    'GB' : 30,
    'TB' : 40,
    'Kb' : 7,
    'Mb' : 17,
    'Gb' : 27,
    'Tb' : 37,
}

def query_1():
    mem_size = input("Enter size of memory (ex:- 16 MB) : ")
    addressable = input("What kind of addressable memory is it (Byte,Bit,Nibble,Word) : ")
    len_inst  = int(input("Enter the length of each instruction in bits : "))
    
    len_reg = int(input("Enter the length of each register in bits : "))
    mem_size = mem_size.split( )
    size = math.ceil(math.log2(int(mem_size[0])))
    ans_1 = 0
    ans_2 = 0
    ans_3 = 0
    ans_4 = 0
    ans_5 = 0
    if (addressable=="Byte"):
        ans_1 = size + dict_size[mem_size[1]]
    elif (addressable =="Bit"):
        ans_1 = size + dict_size[mem_size[1]]+3
    elif (addressable == "Nibble"):
        ans_1 = size + dict_size[mem_size[1]]+1
    elif (addressable == "Word"):
        t = len_inst/8
        ans_1  = (2**(size + dict_size[mem_size[1]]))/(t)
        ans_1 = math.ceil(math.log2(ans_1))
    

    p = ans_1
    q = 0
    r = len_reg
    q = len_inst - p - r
    ans_2 = q
    s = len_inst - q - r -r
    ans_3 = s
    ans_4 = int(2**q)
    ans_5 = int(2**len_reg)
    print()
    print("Minimum number of bits needed to represent an address in the given architecture : ", ans_1)
    print("Number of bits needed by opcode : ", ans_2)
    print("Number of filler bits in Instruction type 2 : ", ans_3)
    print("Maximum numbers of instructions this ISA can support : ", ans_4)
    print("Maximum number of registers this ISA can support : ", ans_5)

def Query2():
    ty = int(input("Which category is it (1 or 2): "))
    if(ty==1):
        mem_size = input("Enter size of memory (ex:- 16 MB) : ")
        addressable = input("What kind of addressable memory is it (Byte,Bit,Nibble,Word) : ")
        #len_inst  = int(input("Enter the length of each instruction in bits : "))
        new_bits = int(input("Number of bits in the CPU : "))
        new_add = input("What kind of addressable memory do you want to change it to (Byte,Bit,Nibble,Word) : ")
        #len_reg = int(input("Enter the length of each register in bits : "))
        mem_size = mem_size.split( )
        size = math.ceil(math.log2(int(mem_size[0])))
        ans_1 = 0
        ans_2 = 0
        
        if (addressable=="Byte"):
            ans_1 = size + dict_size[mem_size[1]]
        elif (addressable =="Bit"):
            ans_1 = size + dict_size[mem_size[1]]+3
        elif (addressable == "Nibble"):
            ans_1 = size + dict_size[mem_size[1]]+1
        elif (addressable == "Word"):
            t = new_bits/8
            ans_1  = (2**(size + dict_size[mem_size[1]]))/(t)
            ans_1 = math.ceil(math.log2(ans_1))
            
        if (new_add=="Byte"):
            ans_2 = size + dict_size[mem_size[1]]
        elif (new_add =="Bit"):
            ans_2 = size + dict_size[mem_size[1]]+3
        elif (new_add == "Nibble"):
            ans_2 = size + dict_size[mem_size[1]]+1
        elif (new_add == "Word"):
            t = new_bits/8
            ans_2  = (2**(size + dict_size[mem_size[1]]))/(t)
            ans_2 = math.ceil(math.log2(ans_2))

        if(ans_2-ans_1>0):
            print("+" + str(ans_2-ans_1))
        elif(ans_2-ans_1<=0):
            print(ans_2-ans_1)
        print(ans_1, "pins ->", ans_2, "pins")
    elif(ty==2):
        #mem_size = input("Enter size of memory (ex:- 16 MB) : ")
        new_bits = int(input("Number of bits in the CPU : "))
        pins = int(input("How many pins are there : "))
        addressable = input("What kind of addressable memory is it (Byte,Bit,Nibble,Word) : ")
        #len_inst  = int(input("Enter the length of each instruction in bits : "))
        t = int(new_bits/8)
        ans = 0
        x = 0
        if (addressable=="Byte"):  
            x = pins
            ans = 2**pins
        elif (addressable =="Bit"):
            x = pins - 3  
            ans = (2**(pins))/8
        elif (addressable == "Nibble"): 
            x = pins -1 
            ans = (2**(pins))/2
        elif (addressable == "Word"):
            t = new_bits/8
            x = pins + math.log2(t)
            ans = (2**(pins))*t
        y = 2**(x-30)
        print("Main Memory can be " + str(ans) + " Bytes")
        print("Answer in GB : ", y)

############################################################################################################################
X = int(input("WHICH TYPE OF QUERY IS IT (1 OR 2) : "))
if (X==1):
    query_1()
elif (X==2):
    Query2()