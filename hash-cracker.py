import hashlib

# Get and validate input
hash_input = input("Input the hash that you want to crack: ")
while len(hash_input) < 32:
    print("Hash too short!")
    hash_input = input("Input the hash that you want to crack: ")

hash_alg = input("Input the hashing algorithm used (md5/sha1/sha256): ").strip().upper()
while hash_alg not in ["MD5", "SHA1", "SHA256"]:
    print("Invalid hash algorithm!")
    hash_alg = input("Input the hashing algorithm used (md5/sha1/sha256): ").strip().upper()

# Process wordlist
FOUND = False
with open("milw0rm-dictionary.txt", "r", encoding="UTF-8") as wordlist:
    for index, word in enumerate(wordlist):
        word = word.strip()  # Remove whitespace
        
        # Fix: Properly call encode() and hexdigest()
        if hash_alg == "MD5":
            hashed_word = hashlib.md5(word.encode('utf-8')).hexdigest()
        elif hash_alg == "SHA1":
            hashed_word = hashlib.sha1(word.encode('utf-8')).hexdigest()
        else:  # SHA256
            hashed_word = hashlib.sha256(word.encode('utf-8')).hexdigest()
            
        if hash_input == hashed_word:
            print(f"Password Found: {word}")
            FOUND = True
            break

if not FOUND:
    print("Password not found in wordlist")