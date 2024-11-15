sbox=[[0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
      [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
      [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
      [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
      [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
      [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
      [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
      [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
      [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
      [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
      [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
      [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
      [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
      [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
      [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
      [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]]

Rcon=[
    [0x01, 0x00, 0x00, 0x00, 0x00], 
    [0x02, 0x00, 0x00, 0x00, 0x00],   
    [0x04, 0x00, 0x00, 0x00, 0x00], 
    [0x08, 0x00, 0x00, 0x00, 0x00], 
    [0x10, 0x00, 0x00, 0x00, 0x00],
    [0x20, 0x00, 0x00, 0x00, 0x00],
    [0x40, 0x00, 0x00, 0x00, 0x00],
    [0x80, 0x00, 0x00, 0x00, 0x00],
    [0x1b, 0x00, 0x00, 0x00, 0x00],
    [0x36, 0x00, 0x00, 0x00, 0x00]
]

def sub_bytes(s):
    for i in range(4):
        for j in range(4):
            row=s[i][j] >> 4 #primii 4 biti dau linia
            column=s[i][j] & 0x0f #ultimii 4 biti dau coloana 
            s[i][j]=sbox[row][column]


def shift_rows(s):
    #prima linie ramane neschimbata, urmatoarele se deplaseaza la stanga cu n pozitii, unde n e numarul randului
    s[1]=s[1][1:] + s[1][:1]
    s[2]=s[2][2:] + s[2][:2]
    s[3]=s[3][3:] + s[3][:3]


def xTimes(x):
    if x & 0x80: #primul bit e 1
        x = x << 1 & 0xFF #shiftam cu o pozitie la stanga
        x ^= 0x1b #facem xor cu sirul 0011011
    else:
        x = x << 1 &0xff#doar shiftam cu o pozitie la stanga
    return x 

def mix_a_column(s):
    a=s[0]
    b=s[1]
    c=s[2]
    d=s[3]

    s[0] = xTimes(a) ^ xTimes(b) ^ b ^ c ^ d
    s[1] = a ^ xTimes(b) ^ xTimes(c) ^ c ^ d
    s[2] = a ^ b ^ xTimes(c) ^ xTimes(d) ^ d
    s[3] = xTimes(a) ^ a ^ b ^ c ^ xTimes(d)

def mix_columns(s):
    for i in range(4):  
        column=[]
        column = [s[j][i] for j in range(4)]  # extrag coloana
        
        mix_a_column(column)
        
        for j in range(4):  # actualizez matricea s cu valorile calculate
            s[j][i] = column[j]


def add_round_key(s, k):   
    for i in range(4):
        for j in range(4):
            s[i][j] ^= k[i][j]


def rot_word(word):
    return word[1:]+word[:1]

def sub_word(word):
    substituted_word = []
    for byte in word:
        # Iau randul și coloana pentru byte-ul curent
        row = byte >> 4
        column = byte & 0x0F
        # Substituție și adăugare la lista substituită
        substituted_byte = sbox[row][column]
        substituted_word.append(substituted_byte)
    return substituted_word

    

#AES-128
Nk=4 #lungime cheie
Nb=4 #marime bloc
Nr=10 #numar runde
#nk, nb se refera la nr de cuvinte din 32 de biti fiecare

def key_expansion(key):
    key_expanded = [key]
    key_prev=key_expanded[-1]
    w0 = [row[0] for row in key_prev]
    w1 = [row[1] for row in key_prev]
    w2 = [row[2] for row in key_prev]
    w3 = [row[3] for row in key_prev]
   
    for i in range(1,Nr+1):
        #iau w3 care reprezinta ultimul elem din key prev si aplic operatiile rotate, sub, xor cu rcon
        w3_new=w3
        #rotate
        w3_new=rot_word(w3_new)
        #iau din sbox
        w3_new=sub_word(w3_new)
        #xor cu Rcon
        rcon=Rcon[i-1]
        res=[] 
        for element1, element2 in zip(w3_new,rcon):
            res.append(element1^element2)
        w3_new=res
        
        #calculam w4,w5,w6,w7
        w4=[]
        for element1, element2 in zip(w0,w3_new):
            w4.append(element1^element2)
    
        w5=[]
        for element1, element2 in zip(w1,w4):
            w5.append(element1^element2)
     
        w6=[]
        for element1, element2 in zip(w2,w5):
            w6.append(element1^element2)
        
        w7=[]
        for element1, element2 in zip(w3,w6):
            w7.append(element1^element2)
        
        #adaugam in lista cheia generata
        round_columns = [w4, w5, w6, w7]
        transpusa = [[rand[i] for rand in round_columns] for i in range(len(round_columns[0]))]
        key_expanded.append(transpusa)
        
        w0=w4
        w1=w5
        w2=w6
        w3=w7
         
    return key_expanded

def cipher(input_block, Nr, w):
    state = input_block
    #print("input:")
    #print(state)
    #for row in state:
    #    line = ' '.join(['0x{:02x}'.format(element) for element in row])
    #    print(line)
    
    add_round_key(state, w[0])

    for round in range(1, Nr):
        sub_bytes(state)
        print('Runda ', round)
        #print('Dupa sub')
        #for row in state:
        #    line = ' '.join(['0x{:02x}'.format(element) for element in row])
        #    print(line)
        shift_rows(state)
        #print('Dupa shift')
        #for row in state:
        #    line = ' '.join(['0x{:02x}'.format(element) for element in row])
        #    print(line)
        mix_columns(state)
        print('Dupa mix')
        for row in state:
            line = ' '.join(['0x{:02x}'.format(element) for element in row])
            print(line)
        add_round_key(state, w[round])
        #for row in w[round]:
        #    line = ' '.join(['0x{:02x}'.format(element) for element in row])
        #    print(line)
    print('Runda 10')
    sub_bytes(state)
    print('Dupa sub')
    for row in state:
        line = ' '.join(['0x{:02x}'.format(element) for element in row])
        print(line)
    shift_rows(state)
    print('Dupa shift')
    for row in state:
        line = ' '.join(['0x{:02x}'.format(element) for element in row])
        print(line)
    add_round_key(state, w[Nr])
    print('Dupa add')
    for row in state:
        line = ' '.join(['0x{:02x}'.format(element) for element in row])
        print(line)
    return state



