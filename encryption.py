def caesar_encrypt(plaintext, shift):
    """
    Encrypt a plaintext string using the Caesar cipher algorithm with a given shift value.

    Parameters:
    plaintext (str): The plaintext to encrypt.
    shift (int): The number of positions to shift the characters in the plaintext.

    Returns:
    str: The encrypted ciphertext.
    """

    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shifted_char = chr(((ord(char.lower()) - 97 + shift) % 26) + 97)
            if char.isupper():
                shifted_char = shifted_char.upper()
            ciphertext += shifted_char
        else:
            ciphertext += char

    return ciphertext

def caesar_decrypt(ciphertext, shift):
    """
    Decrypt a ciphertext string using the Caesar cipher algorithm with a given shift value.

    Parameters:
    ciphertext (str): The ciphertext to decrypt.
    shift (int): The number of positions to shift the characters in the ciphertext.

    Returns:
    str: The decrypted plaintext.
    """

    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shifted_char = chr(((ord(char.lower()) - 97 - shift) % 26) + 97)
            if char.isupper():
                shifted_char = shifted_char.upper()
            plaintext += shifted_char
        else:
            plaintext += char

    return plaintext

def encrypt_file(input_file, output_file, shift):
    """
    Encrypt the contents of an input file using the Caesar cipher algorithm with a given shift value and write the encrypted contents to an output file.

    Parameters:
    input_file (str): The path to the input file.
    output_file (str): The path to
    """