from Crypto.Util.number import long_to_bytes
import math

def solve_challenge():
    # Load challenge
    with open("challenge_data.txt") as f:
        N = int(f.readline())
        e = int(f.readline())
        c = int(f.readline())

    # Factorization is easy: sqrt(N) ~ P
    P = int(math.isqrt(N))
    # Because next_prime(P) is very close to P
    while N % P != 0:
        P += 1
    Q = N // P

    phi = (P - 1) * (Q - 1)
    d = pow(e, -1, phi)
    m = pow(c, d, N)
    plaintext = long_to_bytes(m)
    print("Decrypted message:", plaintext)

if __name__ == "__main__":
    solve_challenge()
