# 🛡️ Python Cybersecurity Toolkit

A collection of custom security tools built in Python, demonstrating proficiency in Network Reconnaissance, Cryptography, and Traffic Analysis.

## 📂 Project Overview

| Tool | Function | Key Concepts |
| :--- | :--- | :--- |
| **1. Port Scanner** | Scans target IP for open ports (TCP) | Socket Programming, Networking |
| **2. Hash Cracker** | Cracks MD5 hashes using a dictionary attack | Cryptography, Brute-Force Logic |
| **3. Subdomain Enumerator** | Discovers hidden subdomains (admin, dev, etc.) | Web Recon, HTTP Requests |
| **4. Packet Sniffer** | Captures and filters live network traffic | Scapy, Network Forensics, ICMP |
| **5. File Integrity Monitor** | Alerts when critical files are modified | System Defense, Hashing, Baseline comparison |

## 🚀 How to Run

**Prerequisites:**
* Python 3.x
* Kali Linux (Preferred)
* Scapy (`pip install scapy`)

**Example Usage (Port Scanner):**
```bash
python3 scanner.py <Target-IP>
