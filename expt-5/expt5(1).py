import random
import time

def simulate_stop_and_wait(payload_list):
    """Simulates the Stop-and-Wait ARQ protocol transmission."""
    current_index = 0
    total_frames = len(payload_list)

    while current_index < total_frames:
        current_data = payload_list[current_index]
        print(f"\n[Sender] Transmitting Frame {current_index}: '{current_data}'")
        time.sleep(1)

        # Simulating network reliability (50% chance of success)
        transmission_success = random.choice([True, False])

        if transmission_success:
            print(f"[Receiver] Frame {current_index} arrived safely.")
            print(f"[Receiver] Dispatching ACK {current_index}...")
            time.sleep(1)
            
            print(f"[Sender] Acknowledgment {current_index} confirmed.")
            print("[Sender] Proceeding to the next transmission.")
            current_index += 1
        else:
            print(f"[Network] Error: Frame {current_index} dropped or ACK lost.")
            print(f"[Sender] Timer expired! Re-sending Frame {current_index}...")

    print("\n*** Transmission Complete: All frames delivered successfully. ***")


def main():
    print("=== Stop-and-Wait ARQ Protocol ===")
    
    try:
        num_frames = int(input("How many frames would you like to send? "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    frame_buffer = []
    for index in range(num_frames):
        frame_content = input(f"Enter payload for Frame {index}: ")
        frame_buffer.append(frame_content)

    print("\n--- Initiating Transfer ---")
    simulate_stop_and_wait(frame_buffer)


if __name__ == "__main__":
    main()