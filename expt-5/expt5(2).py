def simulate_go_back_n(frame_list, window_capacity):
    """Simulates the Go-Back-N ARQ protocol transmission."""
    total_frames = len(frame_list)
    base_index = 0

    while base_index < total_frames:
        
        window_end = min(base_index + window_capacity, total_frames)
        
        print("\n[Sender] Transmitting current window:")
        for i in range(base_index, window_end):
            print(f"   -> Sending Frame {i}: '{frame_list[i]}'")

      
        try:
            lost_frame = int(input("\n[Network] Enter lost frame number (-1 if no frame is lost): "))
        except ValueError:
            print("[System] Invalid input detected. Assuming no frame was lost (-1).")
            lost_frame = -1

        if lost_frame == -1:
            print("[Receiver] All frames in the current window received successfully.")
            
            base_index = window_end
        else:
            print(f"[!] Alert: Frame {lost_frame} was lost in transit!")
            print(f"[*] Go-Back-N triggered: Rolling back and retransmitting from Frame {lost_frame}...")
            
            base_index = lost_frame

    print("\n*** Transfer Protocol Complete: All frames transmitted successfully. ***")


def main():
    print("=== Go-Back-N ARQ Protocol Simulation ===")
    
    try:
        num_frames = int(input("Enter total number of frames to send: "))
        window_size = int(input("Enter window size: "))
    except ValueError:
        print("Invalid input. Please enter whole numbers only.")
        return

    frame_buffer = []
    for index in range(num_frames):
        frame_content = input(f"Enter payload for Frame {index}: ")
        frame_buffer.append(frame_content)

    print("\n--- Initiating Transfer ---")
    simulate_go_back_n(frame_buffer, window_size)


if __name__ == "__main__":
    main()