def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def encrypt(msg, e, n):
    return [pow(ord(char), e, n) for char in msg]

def decrypt(cipher, d, n):
    return ''.join([chr(pow(char, d, n)) for char in cipher])

p = 61
q = 53
n = p * q            
phi = (p - 1) * (q - 1) 

e = 19

d = modinv(e, phi)

public_key = (e, n)
private_key = (d, n)

message = input("Enter the message to encrypt (use capital letters A-Z): ")

cipher = encrypt(message, e, n)
decrypted = decrypt(cipher, d, n)

print("\n--- RSA Encryption and Decryption ---")
print("Original Message:", message)
print("Public Key (e, n):", public_key)
print("Private Key (d, n):", private_key)
print("Encrypted Message:", cipher)
print("Decrypted Message:", decrypted)
