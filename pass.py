import random
import string


def generate_password(length=12, use_upper=True, use_numbers=True, use_symbols=True):
    # Define character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_upper else ""
    digits = string.digits if use_numbers else ""
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/" if use_symbols else ""

    # Combine all allowed characters
    all_chars = lowercase + uppercase + digits + symbols

    if not all_chars:
        return "Error: No character types selected!"

    # Generate password
    password = []
    # Guarantee at least one character from each selected category
    if use_upper and uppercase:
        password.append(random.choice(uppercase))
    if use_numbers and digits:
        password.append(random.choice(digits))
    if use_symbols and symbols:
        password.append(random.choice(symbols))

    # Fill the rest randomly
    remaining_length = length - len(password)
    password += [random.choice(all_chars) for _ in range(remaining_length)]

    # Shuffle to avoid predictable pattern
    random.shuffle(password)

    return ''.join(password)


def main():
    print("======================================")
    print("     Strong Password Generator      ")
    print("======================================\n")

    while True:
        try:
            length = int(input("How many characters? (8-32 recommended): "))
            if 4 <= length <= 64:
                break
            print("Please choose a length between 4 and 64.")
        except ValueError:
            print("Please enter a number.")

    print("\nInclude these character types? (y/n)")

    upper = input("Uppercase letters (A-Z)    ? ").lower().startswith('y')
    numbers = input("Numbers       (0-9)        ? ").lower().startswith('y')
    symbols = input("Special chars (!@#$%^ etc) ? ").lower().startswith('y')

    # At least lowercase is always included
    if not (upper or numbers or symbols):
        print("\nNote: Using only lowercase letters.")

    password = generate_password(
        length=length,
        use_upper=upper,
        use_numbers=numbers,
        use_symbols=symbols
    )

    print("\n" + "=" * 40)
    print("Generated password:")
    print(f"  →  {password}")
    print(f"  Length: {len(password)} characters")
    print("=" * 40)

    print("\nImportant:")
    print("• Don't share this password with anyone")
    print("• Consider using a password manager")


if __name__ == "__main__":
    try:
        main()
        while input("\nGenerate another password? (y/n): ").lower().startswith('y'):
            print("\n" + "-" * 40 + "\n")
            main()
    except KeyboardInterrupt:
        print("\n\nGoodbye! Stay safe online.")