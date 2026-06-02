target_ip = input("Target IP: ")
target_ip = target_ip.strip()
start_port = int(input("Start Port: "))
end_port = int(input("End Port: "))
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

