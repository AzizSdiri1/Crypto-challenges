# RSA3 Challenge

## Description
This is a multi-prime RSA challenge with 7 consecutive primes:

- N = P1 * P2 * P3 * P4 * P5 * P6 * P7  
- e = 65537  
- Ciphertext c is provided.

The primes are consecutive (next prime after the previous), which makes factorization possible if you approximate the roots.

## Hints
- Estimate the 7th root of N to get a starting point for P1.  
- Use bidirectional prime search to factor N.  
- Once all primes are found, compute φ(N) = (p1-1)*(p2-1)*...*(p7-1).  
- Derive the private exponent d and decrypt using m = c^d mod N.

## Files
- `challenge.py` → generates multi-prime N and encrypts the flag  
- `solver.py` → solves the challenge  

## Difficulty
Medium
