class DataLinkFraming:
    """A class to handle data link layer framing and stuffing techniques."""
    
    @staticmethod
    def apply_character_count(payload: str) -> str:
        payload_length = len(payload)
        return f"{payload_length}{payload}"

    @staticmethod
    def apply_byte_stuffing(payload: str, flag_char: str = '$', esc_char: str = '/') -> str:
        stuffed_frame = [flag_char]
        for char in payload:
            if char in (flag_char, esc_char):
                stuffed_frame.append(esc_char)
            stuffed_frame.append(char)
        stuffed_frame.append(flag_char)
        
        return "".join(stuffed_frame)

    @staticmethod
    def apply_bit_stuffing(payload: str) -> str:
        stuffed_bits = []
        consecutive_ones = 0
        
        for bit in payload:
            stuffed_bits.append(bit)
            if bit == '1':
                consecutive_ones += 1
                if consecutive_ones == 5:
                    stuffed_bits.append('0')
                    consecutive_ones = 0
            else:
                consecutive_ones = 0
                
        flag_sequence = "01111110"
        return f"{flag_sequence}{''.join(stuffed_bits)}{flag_sequence}"

    @staticmethod
    def calculate_efficiency(original_bits: int, framed_bits: int) -> float:
        return (original_bits / framed_bits) * 100


def main():
    print("--- Framing Techniques Menu ---")
    print("1. Character Count")
    print("2. Byte Stuffing")
    print("3. Bit Stuffing")

    try:
        user_choice = int(input("Enter your choice (1-3): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if user_choice == 1:
        raw_data = input("Enter data: ")
        framed_data = DataLinkFraming.apply_character_count(raw_data)
        
    elif user_choice == 2:
        raw_data = input("Enter data: ")
        framed_data = DataLinkFraming.apply_byte_stuffing(raw_data)
        
    elif user_choice == 3:
        raw_data = input("Enter binary data: ")
        framed_data = DataLinkFraming.apply_bit_stuffing(raw_data)
        
    else:
        print("Invalid choice. Exiting program.")
        return

    
    original_size_bits = len(raw_data) * 8
    frame_size_bits = len(framed_data) * 8
    overhead = frame_size_bits - original_size_bits
    efficiency_pct = DataLinkFraming.calculate_efficiency(original_size_bits, frame_size_bits)

    
    print("\n--- Framing Results ---")
    print(f"Original data: {raw_data}")
    print(f"Framed data:   {framed_data}")
    print(f"Original size: {original_size_bits} bits")
    print(f"Frame size:    {frame_size_bits} bits")
    print(f"Overhead:      {overhead} bits")
    print(f"Efficiency:    {efficiency_pct:.2f}%")


if __name__ == "__main__":
    main()