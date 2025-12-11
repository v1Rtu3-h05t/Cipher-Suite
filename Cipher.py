import string
import sys
from collections import Counter

BANNER = r"""
╔══════════════════════════════════════════════════════════════╗
║ ██╗   ██╗ ██╗██████╗ ████████╗██╗   ██╗██████╗              ║
║ ██║   ██║███║██╔══██╗╚══██╔══╝██║   ██║╚════██╗             ║
║ ██║   ██║╚██║██████╔╝   ██║   ██║   ██║ █████╔╝             ║
║ ╚██╗ ██╔╝ ██║██╔══██╗   ██║   ██║   ██║ ╚═══██╗             ║
║  ╚████╔╝  ██║██║  ██║   ██║   ╚██████╔╝██████╔╝             ║
║   ╚═══╝   ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═════╝              ║
║                                                              ║
║         ██╗  ██╗ ██████╗ ███████╗████████╗                  ║
║         ██║  ██║██╔═████╗██╔════╝╚══██╔══╝                  ║
║         ███████║██║██╔██║███████╗   ██║                     ║
║         ██╔══██║████╔╝██║╚════██║   ██║                     ║
║         ██║  ██║╚██████╔╝███████║   ██║                     ║
║         ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝                     ║
║                                                              ║
║                  CIPHER SUITE v2.1                           ║
║              Advanced Cryptography Tools                     ║
╚══════════════════════════════════════════════════════════════╝
"""

# === CAESAR CIPHER ENGINE ===
class PhantomCipher:
    def __init__(self):
        self.alpha_low = list(string.ascii_lowercase)
        self.alpha_up = list(string.ascii_uppercase)
    
    def morph_char(self, target, offset, alpha):
        """Morph a single character within its alphabet."""
        if target not in alpha:
            return target
        current_pos = alpha.index(target)
        new_pos = (current_pos + offset) % len(alpha)
        return alpha[new_pos]
    
    def execute(self, message, offset, operation, preserve_case=True):
        """
        Execute cipher operation on message.
        
        Args:
            message: Input text
            offset: Shift amount (0-25)
            operation: 'encode' or 'decode'
            preserve_case: Keep original capitalization
        """
        if operation == "decode":
            offset = -offset
        
        result = ""
        for target in message:
            if preserve_case and target.isupper():
                result += self.morph_char(target, offset, self.alpha_up)
            elif target.lower() in self.alpha_low:
                morphed = self.morph_char(target.lower(), offset, self.alpha_low)
                result += morphed
            else:
                result += target
        
        return result
    
    # === Ghost Mode: Brute Force ===
    def ghost_crack(self, ciphertext):
        """Try all 26 possible shifts and return results."""
        possibilities = []
        for offset in range(26):
            decrypted = self.execute(ciphertext, offset, "decode")
            possibilities.append((offset, decrypted))
        return possibilities
    
    # === Pattern Recognition ===
    def pattern_scan(self, text):
        """Perform frequency analysis on the text."""
        alpha_only = ''.join(c.lower() for c in text if c.isalpha())
        if not alpha_only:
            return None
        
        freq = Counter(alpha_only)
        total = len(alpha_only)
        return [(char, count, f"{(count/total)*100:.1f}%") 
                for char, count in freq.most_common(5)]

# === INPUT VALIDATION ===
def get_validated_input(prompt, valid_opts=None, input_type=str):
    """Get validated input from user."""
    while True:
        try:
            user_input = input(prompt).strip()
            
            if input_type == int:
                value = int(user_input)
                if valid_opts and value not in valid_opts:
                    print(f"[!] Invalid range. Enter {min(valid_opts)}-{max(valid_opts)}")
                    continue
                return value
            else:
                value = user_input.lower()
                if valid_opts and value not in valid_opts:
                    print(f"[!] Invalid option. Choose: {', '.join(valid_opts)}")
                    continue
                return value
        except ValueError:
            print("[!] Invalid input. Try again.")
        except KeyboardInterrupt:
            print("\n\n[*] vh05t signing off...")
            sys.exit(0)

# === COMMAND MENU ===
def display_commands():
    """Display available commands."""
    print("\n" + "═" * 60)
    print("AVAILABLE COMMANDS:")
    print("  [1] Encrypt text")
    print("  [2] Decrypt text")
    print("  [3] Ghost crack (brute force all shifts)")
    print("  [4] Pattern scan (frequency analysis)")
    print("  [5] Exit terminal")
    print("═" * 60)

# === MAIN TERMINAL ===
def main():
    print(BANNER)
    phantom = PhantomCipher()
    
    print(">> v1rtu3-h05t Cipher Terminal initialized")
    print(">> Cryptographic operations ready\n")
    
    while True:
        display_commands()
        
        cmd = get_validated_input("\n[vh05t@cipher]$ ", 
                                   valid_opts=['1', '2', '3', '4', '5'])
        
        if cmd == '5':
            print("\n[X] Terminal session closed.\n")
            break
        
        if cmd in ['1', '2']:
            operation = 'encode' if cmd == '1' else 'decode'
            message = input(f"\n[>] Enter message to {operation}: ").strip()
            
            if not message:
                print("[!] Empty message.")
                continue
            
            offset = get_validated_input("[>] Offset value (0-25): ", 
                                        valid_opts=range(26), input_type=int)
            
            result = phantom.execute(message, offset, operation)
            
            print("\n" + "─" * 60)
            print(f"[+] {operation.upper()} COMPLETE:")
            print(f"    {result}")
            print("─" * 60)
        
        elif cmd == '3':
            ciphertext = input("\n[>] Enter encrypted text: ").strip()
            
            if not ciphertext:
                print("[!] Empty input.")
                continue
            
            print("\n[*] GHOST CRACK INITIATED - Testing all offsets:")
            print("─" * 60)
            
            possibilities = phantom.ghost_crack(ciphertext)
            for offset, decrypted in possibilities:
                print(f"Offset {offset:2d}: {decrypted}")
            
            print("─" * 60)
        
        elif cmd == '4':
            text = input("\n[>] Enter text for pattern scan: ").strip()
            
            if not text:
                print("[!] Empty input.")
                continue
            
            pattern_data = phantom.pattern_scan(text)
            
            if pattern_data:
                print("\n[*] PATTERN SCAN RESULTS - Top 5 characters:")
                print("─" * 60)
                for char, count, percentage in pattern_data:
                    print(f"   {char.upper()}: {count:3d} hits ({percentage})")
                print("─" * 60)
                print("[i] Intel: 'E' frequency in English ~= 12.7%")
            else:
                print("[!] No alphabetic patterns detected.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[*] vh05t signing off...")
        sys.exit(0)