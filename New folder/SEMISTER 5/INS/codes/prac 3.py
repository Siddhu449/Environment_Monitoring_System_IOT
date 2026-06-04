def vigenere_encrypt(msg, key):
    key = key.upper().replace(" ", "")
    res, i = '', 0
    for c in msg.upper():
        if c == ' ':
            res += ' '
        else:
            res += chr(((ord(c) - 65 + ord(key[i % len(key)]) - 65) % 26) + 65)
            i += 1
    return res

def vigenere_decrypt(msg, key):
    key = key.upper().replace(" ", "")
    res, i = '', 0
    for c in msg.upper():
        if c == ' ':
            res += ' '
        else:
            res += chr(((ord(c) - ord(key[i % len(key)]) + 26) % 26) + 65)
            i += 1
    return res

msg = input("Enter message: ")
key = input("Enter key: ")
enc = vigenere_encrypt(msg, key)
print("Encrypted Message:", enc)
print("Decrypted Message:", vigenere_decrypt(enc, key))

