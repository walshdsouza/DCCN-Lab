import socket

def start_sender():
    """Initializes the client to send frames and wait for ACKs."""
    target_host = "localhost"
    target_port = 9999
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((target_host, target_port))
    
    try:
        total_frames = int(input("Enter total number of frames to send: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        client_socket.close()
        return
        
    for frame_index in range(total_frames):
        frame_payload = input(f"Enter payload for Frame {frame_index}: ")
        
        while True:
            print(f"\n[>>] Transmitting Frame {frame_index}: '{frame_payload}'")
            client_socket.send(frame_payload.encode())
            
            # Wait for the server's response
            server_ack = client_socket.recv(1024).decode()
            
            if server_ack == "ACK":
                print(f"[<<] Acknowledgment for Frame {frame_index} received.")
                print("[*] Preparing next transmission...")
                break
            else:
                print("[!] Acknowledgment failed. Initiating retransmission...")
                
    # Send termination signal and close connection
    client_socket.send("END".encode())
    client_socket.close()
    
    print("\n*** Transfer Protocol Complete: All frames successfully transmitted. ***")

if __name__ == "__main__":
    start_sender()