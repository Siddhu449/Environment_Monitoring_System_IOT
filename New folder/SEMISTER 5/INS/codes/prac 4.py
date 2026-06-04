def generate_matrix(key, show=False):
    key = key.upper().replace('J', 'I').replace(' ', '')
    matrix = []
    for char in key + 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if char.isalpha() and char not in matrix:
            matrix.append(char)
    grid = [matrix[i:i+5] for i in range(0, 25, 5)]

    if show:
        print("\nMatrix:")
        for row in grid:
            print(' '.join(row))
    return grid

def find_position(matrix, letter):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == letter:
                return i, j

def prepare_text(text):
    text = text.upper().replace('J', 'I')
    clean = ''.join(c for c in text if c.isalpha())
    result, i = '', 0
    while i < len(clean):
        a = clean[i]
        b = clean[i+1] if i+1 < len(clean) else 'X'
        if a == b:
            result += a + 'X'
            i += 1
        else:
            result += a + b
            i += 2
    return result + 'X' if len(result) % 2 else result

def encrypt_pair(a, b, m):
    r1, c1 = find_position(m, a)
    r2, c2 = find_position(m, b)
    if r1 == r2:
        return m[r1][(c1+1)%5] + m[r2][(c2+1)%5]
    elif c1 == c2:
        return m[(r1+1)%5][c1] + m[(r2+1)%5][c2]
    else:
        return m[r1][c2] + m[r2][c1]

def decrypt_pair(a, b, m):
    r1, c1 = find_position(m, a)
    r2, c2 = find_position(m, b)
    if r1 == r2:
        return m[r1][(c1-1)%5] + m[r2][(c2-1)%5]
    elif c1 == c2:
        return m[(r1-1)%5][c1] + m[(r2-1)%5][c2]
    else:
        return m[r1][c2] + m[r2][c1]

def playfair_encrypt(msg, key):
    m = generate_matrix(key, show=True)
    prepared = prepare_text(msg)
    return ' '.join(encrypt_pair(prepared[i], prepared[i+1], m) for i in range(0, len(prepared), 2))

def playfair_decrypt(cipher, key, original_message):
    m = generate_matrix(key, show=False)
    plain = ''.join(decrypt_pair(cipher[i], cipher[i+1], m) for i in range(0, len(cipher), 2))
    
    result = ''
    p_index = 0
    for c in original_message:
        if c == ' ':
            result += ' '
        else:
            result += plain[p_index]
            p_index += 1
    return result

msg = input("Enter message: ")
key = input("Enter key: ")

encrypted = playfair_encrypt(msg, key)
print("\nEncrypted:", encrypted)

decrypted = playfair_decrypt(encrypted.replace(' ', ''), key, msg.upper())
print("Decrypted:", decrypted.title())  
