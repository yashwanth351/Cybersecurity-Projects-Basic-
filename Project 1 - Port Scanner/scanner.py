import sys
import socket

# 1. Get the target IP from the command line
# syntax: python3 scanner.py <ip>
target = sys.argv[1] 

print(f"Scanning target: {target}")

try:
    # 2. Loop through ports 1 to 100 (Common ports are in this range)
    for port in range(1, 100): 
        
        # 3. Create a socket object (IPv4, TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # 4. Set a timeout so it doesn't hang if the port is closed (0.5 seconds)
        s.settimeout(0.5) 
        
        # 5. Try to connect. connect_ex returns 0 if successful.
        result = s.connect_ex((target, port)) 
        
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        
        s.close()

except KeyboardInterrupt:
    print("\nExiting...")
    sys.exit()

except socket.error:
    print("\nCould not connect to server.")
    sys.exit()
