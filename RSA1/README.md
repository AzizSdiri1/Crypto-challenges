# RSA2 Challenge

## Description
This RSA variant uses two primes that are extremely close:

- N = P * next_prime(P)  
- e = 65537  
- Ciphertext c is provided.

Your task is to decrypt the message.

## Hints
- Factorization is trivial: try numbers around sqrt(N) to find P.  
- Once P and Q are known, compute φ(N) = (P-1)*(Q-1) and derive d.  
- Decrypt using m = c^d mod N.

## Files
- `challenge.py` → generates N, e, c  
- `solver.py` → solves the challenge  

## Difficulty
Easy to Medium
