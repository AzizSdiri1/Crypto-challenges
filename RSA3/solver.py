import gmpy2
from gmpy2 import mpz, iroot, next_prime, prev_prime, invert, powmod
from Crypto.Util.number import long_to_bytes

INFILE = "rsa3.txt"

def load_challenge(filename=INFILE):
    with open(filename) as f:
        lines = f.readlines()
    N = mpz(lines[2].strip())
    e = mpz(lines[0].split()[-1])
    c = mpz(lines[6].strip())
    return N, e, c

def solve_rsa3(num_primes=7):
    N, e, c = load_challenge()
    
    # Step 1: approximate first prime
    p_approx = iroot(N, num_primes)[0]
    
    factors = []
    remaining = N
    p_forward = next_prime(p_approx)
    p_backward = prev_prime(p_approx)
    
    while len(factors) < num_primes:
        found = False
        for _ in range(50):
            if remaining % p_forward == 0:
                factors.append(p_forward)
                remaining //= p_forward
                found = True
                break
            p_forward = next_prime(p_forward)
        if not found:
            for _ in range(50):
                if remaining % p_backward == 0:
                    factors.append(p_backward)
                    remaining //= p_backward
                    found = True
                    break
                p_backward = prev_prime(p_backward)
        if not found:
            p_forward = next_prime(p_forward)
    
    # Step 2: compute phi
    phi = mpz(1)
    for p in factors:
        phi *= p - 1
    
    # Step 3: compute private exponent
    d = invert(e, phi)
    
    # Step 4: decrypt ciphertext
    m = powmod(c, d, N)
    msg_bytes = int(m).to_bytes((m.bit_length() + 7) // 8, 'big')
    print("Decrypted message:", msg_bytes)

if __name__ == "__main__":
    solve_rsa3()
