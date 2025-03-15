import nmap
import socket

def scan_ports(ip, ports="1-65535"):
    scanner = nmap.PortScanner()
    scanner.scan(ip, ports, arguments="-A -T4")

    for port in scanner[ip]['tcp']:
        service = scanner[ip]['tcp'][port]['name']
        state = scanner[ip]['tcp'][port]['state']
        print(f"Port {port}: {state} | Service: {service}")

    print("\n🔍 Banner Grabbing:")
    for port in [80, 443, 22]:
        try:
            sock = socket.create_connection((ip, port), timeout=2)
            banner = sock.recv(1024).decode().strip()
            print(f"Port {port} Banner: {banner}")
        except:
            continue
