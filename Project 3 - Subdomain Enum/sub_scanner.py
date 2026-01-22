import requests 
import sys 

# 1. Define the target domain (e.g., google.com)
# We will check: www.google.com, admin.google.com, etc.
domain = "google.com" 

# 2. Open the file containing subdomain names
file = open("subdomains.txt")
content = file.read() # Read the whole file
subdomains = content.splitlines() # Split it into a list

print(f"Scanning subdomains for: {domain}")
print("-" * 30)

# 3. Loop through each subdomain in the list
for sub in subdomains:
    # Construct the full URL (e.g., http://admin.google.com)
    url = f"http://{sub}.{domain}" 
    
    try:
        # 4. Send a request to the URL
        # timeout=2 means "give up if it takes longer than 2s"
        requests.get(url, timeout=2) 
        
        # 5. If the line above didn't crash, the site exists!
        print(f"[+] Discovered: {url}") 
        
    except requests.ConnectionError:
        # This runs if the subdomain does NOT exist
        pass
