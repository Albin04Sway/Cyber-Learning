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

## Day 3 - Edge Cases and Validation

### What is an edge case?
Input or situation your code didn't expect.
Always think: what could a user type that breaks this?

### Validation pattern
valid = True          # assume innocent until proven guilty
for part in parts:    # check each piece
    if bad:           # if anything fails
        valid = False # mark as invalid
if valid:             # final verdict
    ...

### Three ways an IP part fails validation
1. Contains letters or symbols - not a digit
2. Value is less than 0
3. Value is greater than 255

### elif vs else
elif  - another condition to check (has a condition)
else  - final fallback if nothing matched (no condition)

### TCP Three Way Handshake
SYN     - scanner says "can we connect?"
SYN-ACK - target says "yes, ready"
ACK     - scanner confirms, connection open

Port responses:
Open     - SYN-ACK received
Closed   - RST received
Filtered - silence, timeout
## Day 3 - Sockets and What Happens Under the Hood

### What is a socket?
IP Address + Port + Protocol = Socket
The full address of a specific service on a specific machine

### Socket code breakdown
import socket                              # pull in the library
s = socket.socket(AF_INET, SOCK_STREAM)   # create TCP/IPv4 socket
s.settimeout(1)                           # wait max 1 second
result = s.connect_ex((target, port))     # attempt handshake
if result == 0 → port is OPEN            # 0 = success
s.close()                                 # always close the socket

### Pentesting output conventions
[+]  positive - something found
[-]  negative - nothing found
[!]  warning or error
[*]  informational

### Wireshark packet patterns
Open port:     SYN → SYN-ACK → ACK
Closed port:   SYN → RST
Filtered port: SYN → silence → timeout

### Why settimeout matters
Without it, filtered ports hang your scanner forever
Too short = false negatives (slow ports look closed)
Too long = slow scanner
