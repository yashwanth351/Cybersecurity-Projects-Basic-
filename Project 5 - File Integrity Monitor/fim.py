import hashlib
import time
import os

# 1. The file we want to protect
target_file = "secret.txt"

def calculate_hash(file_path):
    """Reads a file and returns its MD5 hash (Fingerprint)"""
    with open(file_path, "rb") as f:
        file_content = f.read()
        return hashlib.md5(file_content).hexdigest()

def update_baseline():
    """Mode A: Save the initial fingerprint"""
    print(f"Calculating baseline for {target_file}...")
    hash_value = calculate_hash(target_file)
    
    # Save the hash to a text file (baseline.txt)
    with open("baseline.txt", "w") as f:
        f.write(hash_value)
    
    print(f"[+] Baseline saved! Hash: {hash_value}")

def check_integrity():
    """Mode B: Monitor for changes"""
    # 1. Load the old hash
    if not os.path.exists("baseline.txt"):
        print("Error: No baseline found! Run with 'update' first.")
        return

    with open("baseline.txt", "r") as f:
        original_hash = f.read()

    print(f"Monitoring {target_file} for changes...")
    print("Press Ctrl+C to stop.")

    # 2. Infinite Loop: Check every 1 second
    try:
        while True:
            current_hash = calculate_hash(target_file)
            
            if current_hash != original_hash:
                print(f"\n[!!!] ALERT! FILE MODIFIED!")
                print(f"Original: {original_hash}")
                print(f"New:      {current_hash}")
                
                # Update the variable so it doesn't spam the alert forever
                original_hash = current_hash 
            
            time.sleep(1) # Wait 1 second before checking again

    except KeyboardInterrupt:
        print("\nStopping monitor.")

# --- MAIN MENU ---
user_input = input("Enter 'A' to Update Baseline or 'B' to Start Monitoring: ").upper()

if user_input == "A":
    update_baseline()
elif user_input == "B":
    check_integrity()
else:
    print("Invalid option.")
