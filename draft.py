import string

BANNER = r"""
 ██████╗ ███████╗ █████╗ ███████╗ █████╗ ██████╗ 
██╔════╝ ██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗
██║      █████╗  ███████║███████╗███████║██████╔╝
██║      ██╔══╝  ██╔══██║╚════██║██╔══██║██╔══██╗
╚██████╗ ███████╗██║  ██║███████║██║  ██║██║  ██║
 ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
            CAESAR CIPHER TERMINAL
"""

print(BANNER)

alphabet = list(string.ascii_lowercase)

#  ===CAESAR FUNCTION===
def caesar(text, shift, mode):
    output = ""

    # Flip shift for decode
    if mode == "decode":
        shift = -shift

    for char in text:
        if char not in alphabet:
            output += char
        else:
            old_index = alphabet.index(char)
            new_index = (old_index + shift) % len(alphabet)
            output += alphabet[new_index]

    print(f"\nHere is the {mode}d result: {output}\n")

# ===MAIN LOOP===
should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    restart = input("Type 'yes' to go again. Otherwise type 'no':\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye!")
