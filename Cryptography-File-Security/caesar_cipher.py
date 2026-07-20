#!/usr/bin/env python3
import os

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_ascii = (ord(char) - ascii_offset + shift) % 26 + ascii_offset
            result += chr(encrypted_ascii)
        else:
            result += char    
    return result

def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)

# Main program
if __name__ == "__main__":
    shift = 3
    input_file = "input.txt"


    if not os.path.exists(input_file):
        with open(input_file, "w") as file:
            file.write("Knowledge is power. Learn the basics of cryptography.")
        print(f"[*] Created '{input_file}' with default text.")

    with open(input_file, "r") as file:
        plaintext = file.read()

    print("--- Caesar Cipher Tool ---")
    print("Original Plaintext:\n", plaintext)


    encrypted_text = caesar_cipher(plaintext, shift)
    print("\n[+] Encrypted Text:\n", encrypted_text)
    
    with open("encrypted.txt", "w") as file:
        file.write(encrypted_text)

    decrypted_text = caesar_decipher(encrypted_text, shift)
    print("\n[+] Decrypted Text:\n", decrypted_text)

    with open("decrypt.txt", "w") as file:
        file.write(decrypted_text)
        
    print("\n[*] All files (encrypted.txt, decrypt.txt) updated successfully!")
