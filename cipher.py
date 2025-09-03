# Vigenere Cipher Implementation

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def vigenere(message, key, direction=1):
    key_index = 0
    final_message = ''
    for char in message:
        if char.isalpha():
            is_upper = char.isupper()
            char_lower = char.lower()
            key_char = key[key_index % len(key)]
            offset = alphabet.index(key_char.lower())
            index = alphabet.index(char_lower)
            new_index = (index + offset * direction) % len(alphabet)
            new_char = alphabet[new_index]
            final_message += new_char.upper() if is_upper else new_char
            key_index += 1
        else:
            final_message += char
    return final_message

def encrypt(message, key):
    return vigenere(message, key, 1)

def decrypt(message, key):
    return vigenere(message, key, -1)

if __name__ == "__main__":
    text = "mrttaqrhknsw ih puggrur"
    custom_key = "happycoding"
    print(f"\nEncrypted text: {text}")
    print(f"Key: {custom_key}")
    decrypted = decrypt(text, custom_key)
    print(f"Decrypted text: {decrypted}\n")
