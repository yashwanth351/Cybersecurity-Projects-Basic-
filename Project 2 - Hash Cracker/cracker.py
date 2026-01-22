import hashlib

# 1. The target hash we are trying to crack (This is the MD5 for "hello")
target_hash = "5d41402abc4b2a76b9719d911017c592"

print(f"Target Hash: {target_hash}")
print("Attempting to crack...")

# 2. Open the wordlist file
try:
    with open("wordlist.txt", "r") as file:
        
        # 3. Read each password one by one
        for line in file:
            word = line.strip() # Remove spaces/newlines
            
            # 4. Hash the word using MD5
            # We must encode the string to bytes before hashing
            hashed_word = hashlib.md5(word.encode()).hexdigest()
            
            # 5. Compare!
            if hashed_word == target_hash:
                print(f"\n[!] PASSWORD FOUND: {word}")
                print(f"Hash verified: {hashed_word}")
                exit() # Stop the script once found
                
    print("\nPassword not found in wordlist.")

except FileNotFoundError:
    print("Could not find wordlist.txt file!")
