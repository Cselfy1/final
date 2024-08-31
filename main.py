import random
import string
from deep_translator import GoogleTranslator #pip install googletrans

def print_ascii_hello(): 
    hello_art = """
  _   _      _ _
 | | | |    | | |
 | |_| | ___| | | ___
 |  _  |/ _ \ | |/ _ \\
 | | | |  __/ | | (_) |
 \_| |_/\___|_|_|\___/
"""
    print(hello_art)

# PASSWORD GENERATOR
def generate_password():
    while True:
        print("-------------------------------")
        try:
            length = int(input("Enter the desired password length: "))
            include_symbols = input("Include symbols? (y/n): ").lower() == 'y'
            include_numbers = input("Include numbers? (y/n): ").lower() == 'y' 

            characters = string.ascii_letters
            if include_numbers:
                characters += string.digits
            if include_symbols:
                characters += string.punctuation

            password = ''.join(random.choice(characters) for i in range(length)) #length + characters
            print(f"Generated password: {password}")
            break
        except ValueError:
            print("Please enter a valid number for the password length.")

# TRANSLATOR
def interactive_translator():
    while True:
        print("-------------------------------")
        text = input("Enter text to translate: ")
        target_language = input("Enter target language (e.g., 'en' for English, 'fr' for French): ")

        try:
            translated = GoogleTranslator(source='auto', target=target_language).translate(text)
            print(f"Translated text: {translated}")
            break
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

def main():
    print_ascii_hello()
    while True:
        print("-------------------------------")
        print("\nChoose a function:")
        print("1) Password Generator")
        print("2) Interactive Translator")
        print("3) Exit")

        choice = input("Your choice: ")

        if choice == '1':
            generate_password()
        elif choice == '2':
            interactive_translator()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

        back_to_menu = input("\nWould you like to return to the main menu? (y/n): ").lower()
        if back_to_menu != 'y':
            print("Exiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main() 
    