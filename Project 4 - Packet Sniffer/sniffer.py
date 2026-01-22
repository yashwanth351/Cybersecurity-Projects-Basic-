from scapy.all import *
import sys

# 1. Define the function that runs for EVERY packet caught
def process_packet(packet):
    
    # 2. Check if the packet has an IP layer (most do)
    if packet.haslayer(IP):
        src_ip = packet[IP].src  # Sender's IP
        dst_ip = packet[IP].dst  # Receiver's IP
        
        # 3. Print the flow: Sender ==> Receiver
        print(f"[+] Packet: {src_ip}  ==>  {dst_ip}")
        
        # 4. Special Check: Is it a PING (ICMP) packet?
        if packet.haslayer(ICMP):
            print("    L___ ICMP Packet Detected (Ping!)")

print("Starting Sniffer... Press Ctrl+C to stop.")
print("Waiting for data...")

# 5. Start Sniffing!
# store=False: Don't save packets in RAM (prevents crashing)
# prn=process_packet: Run our function on every packet
sniff(filter="icmp", prn=process_packet, store=False)
