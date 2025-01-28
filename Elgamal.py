import random

# Function to perform modular exponentiation
def modular_exponentiation(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

# Function to find modular inverse
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

# Function to encrypt the numeric plaintext using ElGamal
def elgamal_encrypt(plaintext_number, p, e1, e2):
    r = random.randint(1, p - 1)
    c1 = modular_exponentiation(e1, r, p)
    c2 = (plaintext_number * modular_exponentiation(e2, r, p)) % p
    return c1, c2

# Function to decrypt the ciphertext using ElGamal
def elgamal_decrypt(c1, c2, d, p):
    s = modular_exponentiation(c1, d, p)
    s_inv = mod_inverse(s, p)
    plaintext_number = (c2 * s_inv) % p
    return plaintext_number

# Convert a character to its numeric representation (A = 0, B = 1, ..., Z = 25)
def char_to_num(char):
    return ord(char.upper()) - ord('A')

# Convert a numeric value back to a character (0 = A, 1 = B, ..., 25 = Z)
def num_to_char(num):
    return chr(num + ord('A'))

# Main function to handle encryption and decryption
if __name__ == "__main__":
    # Get user input for public and private keys, and plaintext
    p = int(input("Enter a large prime number (p): "))
    e1 = int(input("Enter the base (e1): "))
    d = int(input("Enter the private key (d): "))

    # Calculate e2 from e1 and d
    e2 = modular_exponentiation(e1, d, p)

    # Get plaintext input (either numeric or character data)
    plaintext = input("Enter the plaintext to encrypt (letters or numbers): ")

    # Determine if the input is numeric or character
    if plaintext.isdigit():
        # If the input is numeric, convert to an integer
        plaintext_number = int(plaintext)
        print(f"Numeric plaintext: {plaintext_number}")
    else:
        # If the input is alphabetic, convert each character to a number
        plaintext_number = [char_to_num(char) for char in plaintext]
        print(f"Character plaintext converted to numbers: {plaintext_number}")

    # Encrypt the plaintext
    if isinstance(plaintext_number, list):
        ciphertext = [elgamal_encrypt(num, p, e1, e2) for num in plaintext_number]
        print(f"Ciphertext: {ciphertext}")
    else:
        c1, c2 = elgamal_encrypt(plaintext_number, p, e1, e2)
        print(f"Ciphertext: (c1={c1}, c2={c2})")

    # Decrypt the ciphertext
    if isinstance(plaintext_number, list):
        decrypted_numbers = [elgamal_decrypt(c1, c2, d, p) for c1, c2 in ciphertext]
        decrypted_text = ''.join([num_to_char(num) for num in decrypted_numbers])
        print(f"Decrypted: {decrypted_text}")
    else:
        decrypted_number = elgamal_decrypt(c1, c2, d, p)
        print(f"Decrypted: {decrypted_number}")
