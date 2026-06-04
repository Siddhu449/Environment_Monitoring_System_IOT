def manual_encrypt_rail_fence():
    plaintext = input("Enter the plaintext: ").replace(" ", "").upper()
    rails = 2
    length = len(plaintext)

    matrix = [[" " for _ in range(length)] for _ in range(rails)]

    row = 0
    direction = 1  

    for col in range(length):
        matrix[row][col] = plaintext[col]
        row += direction
        if row == 0 or row == rails - 1:
            direction *= -1

    print("\nPlaintext:", plaintext)

    print("\nRail Fence Matrix:")
    for r in matrix:
        print(" ".join(r))

    cipher = ''.join([char for row in matrix for char in row if char != " "])
    print("\nCipher Text:", cipher)

manual_encrypt_rail_fence()



































































