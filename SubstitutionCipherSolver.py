def solve_substitution_cipher(ciphertext: str, key: str) -> str:
    # Create a dictionary to store the mapping from ciphertext characters to plaintext characters
    mapping = {}

    # Iterate through the key and map each ciphertext character to the corresponding plaintext character
    for i in range(len(key)):
        mapping[ciphertext[i]] = key[i]

    # Initialize a string to store the plaintext
    plaintext = ""

    # Iterate through the ciphertext and use the mapping to obtain the corresponding plaintext character
    for c in ciphertext:
        plaintext += mapping[c]

    # Return the plaintext
    return plaintext

# Test the function with a simple ciphertext and key
ciphertext = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
plaintext = solve_substitution_cipher(ciphertext, key)

print(f"Ciphertext: {ciphertext}")
print(f"Key: {key}")
print(f"Plaintext: {plaintext}")
