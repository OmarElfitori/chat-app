# LAN Chat Application

## Description
This is a simple real-time LAN chat application built with Python using sockets and threading. It allows multiple users to connect to the same server and exchange messages over a local network.

## Features
- Multi-client chat
- Real-time messaging
- Username support
- Socket-based communication
- Threading for handling multiple clients

## Requirements
- Python 3

## How to Run

### Start the Server
```bash
python server.py
```

### Start the Client
```bash
python client.py
```

Enter the server IP (for testing on the same computer use `127.0.0.1`) and then enter your username.

## Technologies
- Python
- Socket
- Threading
## Connect Over a Local Network

1. Make sure all computers are connected to the same Wi-Fi or LAN.
2. Run the server on one computer:
   ```bash
   python server.py
   ```
3. Find the server computer's local IP address using:
   ```bash
   ipconfig
   ```
4. Use the IPv4 Address shown by ipconfig.
5. Run client.py on the other computers.
6. When prompted for the server IP, enter the server computer's IPv4 address.

## How It Works

- The server uses Python's socket module to create a TCP server.
- The server listens for incoming client connections.
- Each connected client is handled in a separate thread using the threading module.
- When a client sends a message, the server receives it and broadcasts it to every connected client.
- Each client has two threads:
  - One thread continuously receives incoming messages.
  - One thread continuously sends user messages.
- This allows real-time communication between multiple users.