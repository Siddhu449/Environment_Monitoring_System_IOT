def caesar(text, shift): 
    result = []
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            result.append(chr((ord(c) - base + shift) % 26 + base))
        else:
            result.append(c)
    return ''.join(result)

text = input("Enter text: ") 
enc = caesar(text, 3)
dec = caesar(enc, -3)

print("Encrypted:", enc)
print("Decrypted:", dec) 

 
