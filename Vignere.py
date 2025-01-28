def generate_key(text, key):
    key = list(key)
    if len(text) == len(key):
        return ''.join(key)
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return ''.join(key)

def vigenere_encrypt(text, key):
    encrypted = []
    key = generate_key(text.replace(" ", ""), key)  # Remove spaces for the key generation
    text_no_spaces = text.replace(" ", "")  # Remove spaces from text
    for i in range(len(text_no_spaces)):
        char = (ord(text_no_spaces[i].upper()) + ord(key[i].upper()) - 2 * ord('A')) % 26
        encrypted.append(chr(char + ord('A')))
    encrypted_text = ''.join(encrypted)
    
    # Reintroduce spaces at the correct positions
    result = []
    index = 0
    for char in text:
        if char == ' ':
            result.append(' ')
        else:
            result.append(encrypted_text[index])
            index += 1
    return ''.join(result)

def vigenere_decrypt(cipher, key):
    decrypted = []
    key = generate_key(cipher.replace(" ", ""), key)  # Remove spaces for key generation
    cipher_no_spaces = cipher.replace(" ", "")  # Remove spaces from cipher
    for i in range(len(cipher_no_spaces)):
        char = (ord(cipher_no_spaces[i]) - ord(key[i]) + 26) % 26
        decrypted.append(chr(char + ord('A')))
    decrypted_text = ''.join(decrypted)
    
    # Reintroduce spaces at the correct positions
    result = []
    index = 0
    for char in cipher:
        if char == ' ':
            result.append(' ')
        else:
            result.append(decrypted_text[index])
            index += 1
    return ''.join(result)

# Example usage
if __name__ == "__main__":
    # Get user input for the text and key
    text = input("Enter the text to encrypt (uppercase letters only): ")
    key = input("Enter the key (uppercase letters only): ")

    # Encrypt the text
    encrypted = vigenere_encrypt(text, key)
    print(f"Encrypted: {encrypted}")

    # Decrypt the text
    decrypted = vigenere_decrypt(encrypted, key)
    print(f"Decrypted: {decrypted}")
