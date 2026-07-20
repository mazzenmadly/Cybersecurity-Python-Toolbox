#!/usr/bin/env python3

import hashlib
import os  

def hash_master_key():
    master_key = input('Enter a master key. This key will be used to access all your saved passwords. Make it strong!\n')
    # Hash the master key using SHA-256
    hashed_key = hashlib.sha256(master_key.encode()).hexdigest()
    # Store the hashed key securely in a file
    with open("master_key.txt", "w") as f:
        f.write(hashed_key)
    print("Master key saved successfully!\n")

def verify_key():
    entered_key = input("Enter your master key to verify:\n")
    with open("master_key.txt", "r") as f:
        stored_key = f.read().strip()
    hashed_entered_key = hashlib.sha256(entered_key.encode()).hexdigest()
    if hashed_entered_key == stored_key:
        print("Matched")
    else:
        print("Doesn't match")

if __name__ == "__main__":
    
    if not os.path.exists("master_key.txt"):
        hash_master_key()
    else:
        print("--- Welcome Back ---")
        verify_key()
