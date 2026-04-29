# ============================================
#  AS | Attika Sufyan
#  Cybersecurity Student
#  GitHub: github.com/attikasufyan870-del
#  Course: EC-Council Cybersecurity
#  Topic: Network Device Tracker
#  Date: April 2026
# ============================================

import subprocess
import socket
import os

def track_devices():
    print("=" * 55)
    print("  AS | Attika Sufyan — Network Device Tracker")
    print("=" * 55)
    print("\n🔍 Network Pe Connected Devices Track Ho Rahe Hain...")
    print("⚠️  Sirf Apne Network Pe Use Karo!\n")
    
    # Network range
    network = input("Network address likho (e.g., 192.168.1): ")
    
    print(f"\n📡 Scanning {network}.0/24...\n")
    print("-" * 55)
    
    active_devices = []
    
    for i in range(1, 255):
        ip = f"{network}.{i}"
        
        # Ping command
        result = subprocess.run(
            ["ping", "-n", "1", "-w", "500", ip],
            capture_output=True
        )
        
        if result.returncode == 0:
            # Device mila!
            try:
                hostname = socket.gethostbyaddr(ip)[0]
            except:
                hostname = "Unknown Device"
            
            active_devices.append(ip)
            print(f"✅ Device Mila!")
            print(f"   📍 IP Address: {ip}")
            print(f"   💻 Device Name: {hostname}")
            print("-" * 55)
    
    print(f"\n📊 Total Devices Found: {len(active_devices)}")
    print("\n🔐 Security Tip:")
    print("✅ Unknown devices dekh kar block karo!")
    print("✅ Router settings check karo!")
    print("=" * 55)

# Program Start
track_devices()
