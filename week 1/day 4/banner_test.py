import socket

def grab_banner(target, port):
    try:
        # Create a TCP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        
        # Connect to the target
        s.connect((target, port))
        
        # Some services send banner immediately on connect
        # HTTP needs a request first
        s.send(b"HEAD / HTTP/1.0\r\n\r\n")
        
        # Receive up to 1024 bytes of response
        banner = s.recv(1024).decode(errors="ignore")
        s.close()
        
        return banner.strip()
        
    except Exception as e:
        return f"No banner received: {e}"

# Test against a real website
target = "scanme.nmap.org"
port = 80

print(f"[*] Attempting banner grab on {target}:{port}")
print(f"[*] Response:")
print("-" * 40)

banner = grab_banner(target, port)
print(banner)

print("-" * 40)