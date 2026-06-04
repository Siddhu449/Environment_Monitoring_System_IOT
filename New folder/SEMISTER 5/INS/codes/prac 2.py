import string

def generate_key():
    a = list(string.ascii_uppercase)
    b = list(reversed(a))  # Z, Y, X, ..., A
    return dict(zip(a, b))

def encrypt(text, key):
    return ''.join(key.get(c, c) for c in text.upper())

def decrypt(text, key):
    rev_key = {v: k for k, v in key.items()}
    return ''.join(rev_key.get(c, c) for c in text)

if __name__ == "__main__":
    key = generate_key()
    # print("Key:", key)  # <- This line is now hidden from output

    # Accept input from user
    msg = input("Enter the message to encrypt: ")

    enc = encrypt(msg, key)
    dec = decrypt(enc, key)

    print("Original text :", msg)
    print("Encrypted text:", enc)
    print("Decrypted text:", dec)
