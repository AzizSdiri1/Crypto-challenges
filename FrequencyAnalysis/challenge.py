import random
import string

FLAG = "Flag{FrequencyAnalysisFlag}"
TEXT = """It is a period of civil wars in the galaxy. A brave alliance of underground freedom fighters has challenged the tyranny and oppression of the awesome GALACTIC EMPIRE.

Striking from a fortress hidden among the billion stars of the galaxy, rebel spaceships have won their first victory in a battle with the powerful Imperial Starfleet. The EMPIRE fears that another defeat could bring a thousand more solar systems into the rebellion, and Imperial control over the galaxy would be lost forever.

To crush the rebellion once and for all, the EMPIRE is constructing a sinister new battle station. Powerful enough to destroy an entire planet, its completion spells certain doom for the champions of freedom.
"""

def generate_cipher_mapping():
    letters = list(string.ascii_lowercase)
    shuffled = letters[:]
    while True:
        random.shuffle(shuffled)
        if all(a != b for a, b in zip(letters, shuffled)):
            break  # simple derangement to avoid letters mapping to themselves
    return dict(zip(letters, shuffled))

def encrypt_text(text, mapping):
    result = []
    for ch in text:
        if ch.isalpha():
            lower = ch.lower()
            enc = mapping[lower]
            if ch.isupper():
                enc = enc.upper()
            result.append(enc)
        else:
            result.append(ch)
    return "".join(result)

def main():
    mapping = generate_cipher_mapping()
    # Encrypt flag and text
    enc_flag = encrypt_text(FLAG, mapping)
    enc_text = encrypt_text(TEXT, mapping)
    with open("ciphered_flag.txt", "w") as f:
        f.write(enc_flag)
    with open("ciphered_text.txt", "w") as f:
        f.write(enc_text)
    print("Ciphered files created: ciphered_flag.txt, ciphered_text.txt")
    print("Cipher mapping (keep secret for solver):")
    print(mapping)

if __name__ == "__main__":
    main()
