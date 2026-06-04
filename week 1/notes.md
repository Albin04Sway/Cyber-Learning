#Day 1
Every device on a network has an IP address. It tells the network where to deliver the data.
DNS is basically like a phonebook. It returns the IP address of your desired website, so then the browser connects you to that IP address.
Every device has multiple ports. Ports are used to accept packets for specific serivces. HTTP web server uses port 80, SSH remote login uses port 22.
When you scan a port, you get 3 responses:
    Open - something is active on the port, a service is running.
    Closed - The port exists but there is no service running. Nothing active on the port.
    Filtered - The port exists but there is something preventing access to see whether there is an active connection with the port or not. Most likely a firewall.
TCP vs UDP - 2 ways to send data
    TCP is reliable, ordered and confirmed. Before data is sent, it does a three-way-handshake to establish connection. In a phone call, before starting to talk, you make sure the call is connected, same thing.
    UDP is fast, no confirmation, fire and forget. Just like sending a letter, ydk if its arrived.
    Port scanners work on TCP because TCP requires a connection to be established. Scanning a port with TCP means that if there is an established connection, there will also be a response.

#Day 2
F-String Alignment
print(f"{'SCAN INFORMATION' :^40}") - centres within 40 characters
print(f"{'Target IP' :<12}: {target_ip}") - left aligns label in 12 characters

Type Conversion
- input() always returns a string
- use int() to convert to integer e.g. int(input("Port: "))
- use str() to convert to string e.g. str(age)
- mixing types causes TypeError


String Methods
- .strip() - removes whitespace
- .split() - splits a string into a list
- len()    - an integer of the length
