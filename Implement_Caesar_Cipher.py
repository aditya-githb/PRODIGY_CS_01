def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    while True:
        choice = input("Would you like to encrypt or decrypt a message? (e/d): ").lower()
        if choice in ['e', 'd']:
            message = input("Enter your message: ")
            shift = int(input("Enter the shift value: "))

            if choice == 'e':
                print("Encrypted message:", encrypt(message, shift))
            elif choice == 'd':
                print("Decrypted message:", decrypt(message, shift))
        else:
            print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")

        continue_choice = input("Would you like to process another message? (y/n): ").lower()
        if continue_choice != 'y':
            break

if __name__ == "__main__":
    main()
