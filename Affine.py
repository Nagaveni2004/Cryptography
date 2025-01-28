# affine_cipher.py
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for i in range(m):
        if (a * i) % m == 1:
            return i
    return None

def affine_encrypt(text, a, b, m=26):
    if gcd(a, m) != 1:
        raise ValueError("a and m must be coprime.")
    encrypted = ''.join(
        chr((a * (ord(char) - ord('A')) + b) % m + ord('A'))
        if char.isalpha() else char for char in text.upper()
    )
    return encrypted

def affine_decrypt(cipher, a, b, m=26):
    a_inv = mod_inverse(a, m)
    if not a_inv:
        raise ValueError("Modular inverse doesn't exist.")
    decrypted = ''.join(
        chr((a_inv * (ord(char) - ord('A') - b)) % m + ord('A'))
        if char.isalpha() else char for char in cipher.upper()
    )
    return decrypted

# Example usage
if __name__ == "__main__":
    # Get user input
    plaintext = input("Enter the plaintext to encrypt: ")
    a = int(input("Enter the value for a (should be coprime with 26): "))
    b = int(input("Enter the value for b: "))

    # Encrypt the input text
    ciphertext = affine_encrypt(plaintext, a, b)
    print(f"Encrypted: {ciphertext}")

    # Decrypt the ciphertext
    decrypted = affine_decrypt(ciphertext, a, b)
    print(f"Decrypted: {decrypted}")
