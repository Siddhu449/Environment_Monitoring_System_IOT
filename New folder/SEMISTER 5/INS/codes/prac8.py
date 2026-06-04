import random

def power_mod(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:  
            result = (result * base) % mod
        exp = exp >> 1 
        base = (base * base) % mod
    return result


P = 23       
G = 5         

print(f"Publicly known values:\nPrime (P): {P}, Generator (G): {G}")

a = random.randint(2, P-2)
A = power_mod(G, a, P)  

b = random.randint(2, P-2)
B = power_mod(G, b, P)  

print(f"\nAlice's Private Key (a): {a}")
print(f"Bob's Private Key (b): {b}")
print(f"Alice sends: A = {A}")
print(f"Bob sends: B = {B}")

key_Alice = power_mod(B, a, P) 
key_Bob = power_mod(A, b, P)  

print("\n--- Shared Secret Computation ---")
print(f"Alice computes key: {key_Alice}")
print(f"Bob computes key:   {key_Bob}")

if key_Alice == key_Bob:
    print(f"\n✅ Shared Symmetric Key: {key_Alice}")
else:
    print("\n❌ Key Mismatch. Something went wrong!")
