# Frequency Analysis Challenge

## Description
This challenge consists of two files:

- `ciphered_flag.txt` → the flag encrypted using a monoalphabetic substitution cipher.
- `ciphered_text.txt` → a short story encrypted with the same cipher.

Your goal is to decrypt the text and discover the flag.

## Instructions
1. Run `solver.py` to interactively solve the cipher:
    ```bash
    python solver.py
    ```
2. Enter your guesses in the format:
    ```
    cipher_letter=plain_letter
    ```
   Example: `e=s`  
3. The script will display:
    - The **decrypted text so far** (with `-` for unknown letters).  
    - The **cipher text letters** below.  
    - **Letter frequencies** to help you analyze which letters are most common.  
4. Keep entering guesses until the text is fully decrypted.

## Hints
- Start by mapping the most frequent cipher letters to the most common letters in English (`e`, `t`, `a`, `o`, etc.).  
- Use context clues from the story to guess words.  
- The flag is hidden in `ciphered_flag.txt` and uses the same substitution.

## Files
- `creator.py` → generates ciphered text and flag.  
- `solver.py` → interactive frequency analysis tool.  
- `ciphered_text.txt` → the encrypted story.  
- `ciphered_flag.txt` → the encrypted flag.
