target_ip = input("Target IP: ")
target_ip = target_ip.strip()

parts = target_ip.split(".")

if len(parts) != 4:
    print("Invalid IP Address")
else:
    valid = True
    for part in parts:
        if not part.isdigit():
            valid = False
        elif int(part) < 0 or int(part) > 255:
            valid = False

    if valid:
        print("Valid IP Address")
    else:
        print("Invalid IP Address")


start_port = int(input("Start Port: "))
if start_port < 1 or start_port > 65535:
    print("Invalid Start Port")
    
end_port = int(input("End Port: "))
if end_port < 1 or end_port> 65535:
    print("Invalid End Port")

if start_port >= end_port:
    print("Start port must be less than end port")

protocol = "TCP"
total_port = end_port - start_port + 1

print("=" * 40 )
print(f"{'SCAN INFORMATION' :^40}")
print("=" * 40 )

print(f"{'Target IP' :<12}: {target_ip}")
print(f"{'Start Port' :<12}: {start_port}")
print(f"{'End Port' :<12}: {end_port}")
print(f"{'Protocol' :<12}: {protocol}")
print(f"{'Total ports' :<12}: {total_port}")
print("=" * 40 )

