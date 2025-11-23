import string
from collections import Counter

CIPHER_FILE = "ciphered_text.txt"

def load_cipher_text():
    with open(CIPHER_FILE) as f:
        return f.read()

def display_progress(cipher_text, mapping):
    # Show partially decrypted text
    revealed = []
    for ch in cipher_text:
        lower = ch.lower()
        if lower in mapping:
            repl = mapping[lower]
            if ch.isupper():
                repl = repl.upper()
            revealed.append(repl)
        else:
            if ch.isalpha():
                revealed.append("-")
            else:
                revealed.append(ch)
    print("\nCurrent Decryption:")
    print("".join(revealed))

    # Show cipher text letters with - for unknown
    print("\nCipher text legend:")
    legend = []
    for ch in cipher_text:
        if ch.isalpha():
            legend.append(ch)
        else:
            legend.append(ch)
    print("".join(legend))

    # Show frequency table
    letters_only = [c.lower() for c in cipher_text if c.isalpha()]
    freq = Counter(letters_only)
    print("\nLetter frequency (cipher text):")
    for l, count in sorted(freq.items(), key=lambda x: -x[1]):
        print(f"{l}: {count}", end="  ")
    print("\n")

def main():
    cipher_text = load_cipher_text()
    mapping = {}  # guessed letters: cipher -> plain

    while True:
        display_progress(cipher_text, mapping)
        inp = input("Enter your guess (format: e=s) or 'quit' to exit: ").strip()
        if inp.lower() == "quit":
            break
        if "=" not in inp or len(inp.split("=")) != 2:
            print("Invalid format. Use e=s")
            continue
        cipher, plain = inp.lower().split("=")
        if len(cipher) != 1 or len(plain) != 1:
            print("Please enter single letters.")
            continue
        mapping[cipher] = plain

if __name__ == "__main__":
    main()
