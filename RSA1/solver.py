from Crypto.Util.number import long_to_bytes
import math

def solve_challenge():
    # Load challenge
    with open("challenge_data.txt") as f:
        N = int(f.readline())
        e = int(f.readline())
        c = int(f.readline())

    # Vulnerability: N = P^2, so P = sqrt(N)
    P = int(math.isqrt(N))
    phi = P * (P - 1)  # phi(N) for N=P^2
    # Compute private key
    d = pow(e, -1, phi)

    # Decrypt
    m = pow(c, d, N)
    plaintext = long_to_bytes(m)
    print("Decrypted message:", plaintext)

if __name__ == "__main__":
    solve_challenge()
