from Crypto.Util.number import getPrime, bytes_to_long, next_prime

def generate_challenge(bits=512):
    P = getPrime(bits)
    Q = next_prime(P)
    N = P * Q
    e = 65537
    plaintext = b"Secret Message RSA2"
    m = bytes_to_long(plaintext)
    c = pow(m, e, N)

    print(f"N = {N}")
    print(f"e = {e}")
    print(f"c = {c}")

    with open("challenge_data.txt", "w") as f:
        f.write(f"{N}\n{e}\n{c}\n")

if __name__ == "__main__":
    generate_challenge()
