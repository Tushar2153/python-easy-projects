#list of alphabets
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encryption(plain_text,shift):# for encryption of mesage

    cipher_text=""

    for char in plain_text:# iterating over each character in plain text

        position=alphabet.index(char)#searching for position of each letter in the list alphabet
        new_position=(position+shift) % 26 # encrypting the message according to the shift key
        cipher_text+=alphabet[new_position]
    
    print(f"here is the encrypted text\t{cipher_text}")

def decryption(cipher_text,shift):# for decryption of message
    
    plain_text=""

    for char in cipher_text:

        position=alphabet.index(char) #searching for position of each letter in the list alphabet
        new_position=(position-shift)%26 #decrypting the message according to the shift key
        plain_text+=alphabet[new_position]

    print(f"decypyted text is \t{plain_text}")

x= input("type 'encrypt' for encryption,type 'decrypt' for decryption\n")

text=input("enter ypur message\n")#input for the text
shift_key=int(input("enter the shift key\n"))#input for the shift key

if x=="encrypt":
    encryption(text,shift_key)
elif x=="decrypt":
    decryption(text,shift_key,)

