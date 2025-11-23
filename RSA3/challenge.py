from Crypto.Util.number import getPrime, isPrime, bytes_to_long
from functools import reduce
import operator

FLAG = b"Securinets{rsa3_multi_prime}"
KEY_BITS = 512   # bits per prime
E = 65537
OUTFILE = "rsa3.txt"
SAVE_PRIMES = False  # set True if you want primes saved (not secure!)

def next_prime_after(x):
    candidate = x + 1
    if candidate % 2 == 0:
        candidate += 1
    while not isPrime(candidate):
        candidate += 2
    return candidate

def generate_rsa3(flag_bytes=FLAG, num_primes=7, key_bits=KEY_BITS, e=E):
    if num_primes < 2:
        raise ValueError("num_primes should be at least 2 for multi-prime RSA")
    
    primes = []
    p1 = getPrime(key_bits)
    primes.append(p1)
    
    for _ in range(num_primes - 1):
        primes.append(next_prime_after(primes[-1]))
    
    N = reduce(operator.mul, primes, 1)
    m = bytes_to_long(flag_bytes)
    if m >= N:
        raise ValueError("Message too large for modulus; increase KEY_BITS or shorten flag")
    
    c = pow(m, e, N)
    
    return {
        "primes": primes,
        "N": N,
        "e": e,
        "ciphertext": c
    }

def save_to_file(info, filename=OUTFILE, save_primes=SAVE_PRIMES):
    with open(filename, "w") as f:
        f.write(f"public exponent e: {info['e']}\n\n")
        f.write(f"modulus N:\n{info['N']}\n\n")
        f.write(f"ciphertext (decimal):\n{info['ciphertext']}\n\n")
        if save_primes:
            f.write("primes (decimal, from p1 to pN):\n")
            for i, p in enumerate(info['primes'], start=1):
                f.write(f"p{i}: {p}\n")
    print(f"Wrote RSA3 challenge to {filename}")

def main():
    info = generate_rsa3()
    save_to_file(info)

if __name__ == "__main__":
    main()
