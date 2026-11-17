import socket

def start_receiver():
    """Initializes the server to listen for incoming frames."""
    host_address = "localhost"
    port_number = 9999
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host_address, port_number))
    server_socket.listen(1)
    
    print(f"[*] Server initialized. Waiting for connection on port {port_number}...")
    
    active_connection, client_address = server_socket.accept()
    print(f"[+] Connection successfully established with: {client_address}")
    
    while True:
        incoming_payload = active_connection.recv(1024).decode()
        
        # Handle empty data or connection drops
        if not incoming_payload:
            break
            
        # Check for the termination signal
        if incoming_payload == "END":
            print("[*] Transmission sequence completed by client.")
            break
            
        print(f"[>] Received data: {incoming_payload}")
        
        # Dispatch the Acknowledgment back to the sender
        active_connection.send("ACK".encode())
        
    # Clean up the sockets
    active_connection.close()
    server_socket.close()

if __name__ == "__main__":
    start_receiver()