import string
import random

def create_password(length, include_letters, include_digits, include_special_chars):
    """Creating a random password based on user-specified criteria."""
    char_pool = ''
    if include_letters:
        char_pool += string.ascii_letters
    if include_digits:
        char_pool += string.digits
    if include_special_chars:
        char_pool += string.punctuation
    
    if not char_pool:
        raise ValueError("At least one character type must be selected.")
    
    generated_password = ''.join(random.choice(char_pool) for _ in range(length))
    return generated_password

def get_user_choices():
    """Prompting the user to specify password preferences."""
    while True:
        try:
            pwd_length = int(input("Enter desired password length: "))
            if pwd_length <= 0:
                raise ValueError("Password length must be greater than zero.")
            break
        except ValueError as ve:
            print(ve)
    
    letters_choice = input("Include letters (y/n)? ").strip().lower() == 'y'
    digits_choice = input("Include numbers (y/n)? ").strip().lower() == 'y'
    special_chars_choice = input("Include special characters (y/n)? ").strip().lower() == 'y'
    
    return pwd_length, letters_choice, digits_choice, special_chars_choice

def display_password():
    """Main function to run the password generation process."""
    print("Password Generator")
    pwd_length, letters_choice, digits_choice, special_chars_choice = get_user_choices()
    
    try:
        password = create_password(pwd_length, letters_choice, digits_choice, special_chars_choice)
        print(f"Generated Password: {password}")
    except ValueError as error:
        print(error)

if __name__ == "__main__":
    display_password()
    