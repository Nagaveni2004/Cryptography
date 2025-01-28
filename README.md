# Cryptography


# Affine Cipher
The Affine Cipher is a type of monoalphabetic substitution cipher, where each letter in an alphabet is mapped to its numeric equivalent, encrypted using a simple mathematical function, and then converted back to a letter. The encryption function is of the form \(E(x) = (a \cdot x + b) \mod m\), where \(a\) and \(m\) are coprime. Decryption is done using the modular inverse of \(a\).

# Euclidean Algorithm
The Euclidean Algorithm is a method for finding the greatest common divisor (GCD) of two numbers. The Extended Euclidean Algorithm also finds coefficients of Bézout's identity, which are useful for finding the modular inverse. It plays a fundamental role in various cryptographic algorithms.

# ElGamal Encryption
ElGamal Encryption is an asymmetric key encryption algorithm used for secure data transmission. It relies on the Diffie-Hellman key exchange principle and works over groups where the discrete logarithm problem is hard. The encryption involves random numbers to ensure that even the same message encrypted multiple times will yield different ciphertexts.

# RSA Cipher
The RSA Cipher is an asymmetric cryptographic algorithm that is widely used for secure data transmission. It works on the principle of factoring the product of two large prime numbers. The security of RSA relies on the difficulty of the prime factorization problem. The algorithm includes key generation, encryption, and decryption processes.

# Vigenère Cipher
The Vigenère Cipher is a method of encrypting alphabetic text using a simple form of polyalphabetic substitution. A keyword is repeated to match the length of the plaintext, and each letter of the plaintext is shifted along the alphabet by the number of positions determined by the corresponding letter of the keyword.

You can use the above code snippets to implement these ciphers in Python. Each example includes functions for encryption and decryption, along with modular arithmetic operations that are crucial for these cryptographic techniques.
