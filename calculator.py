# Simple Calculator in Python

def calculator():
    print("=====================================")
    print("      Simple Calculator  ✨")
    print("=====================================")
    print("Operations available:")
    print("  1 → Addition       (+)")
    print("  2 → Subtraction    (-)")
    print("  3 → Multiplication (×)")
    print("  4 → Division       (÷)")
    print("=====================================\n")

    # Get first number
    while True:
        try:
            num1 = float(input("Enter first number: "))
            break
        except ValueError:
            print("❌ Please enter a valid number!")

    # Get second number
    while True:
        try:
            num2 = float(input("Enter second number: "))
            break
        except ValueError:
            print("❌ Please enter a valid number!")

    # Get operation choice
    while True:
        try:
            choice = int(input("\nChoose operation (1/2/3/4): "))
            if choice in [1, 2, 3, 4]:
                break
            else:
                print("❌ Please enter 1, 2, 3, or 4!")
        except ValueError:
            print("❌ Please enter a number (1–4)!")

    # Perform calculation
    if choice == 1:
        result = num1 + num2
        operation = "+"
    elif choice == 2:
        result = num1 - num2
        operation = "-"
    elif choice == 3:
        result = num1 * num2
        operation = "×"
    elif choice == 4:
        if num2 == 0:
            print("\n🚫 Error: Division by zero is not allowed!")
            return
        result = num1 / num2
        operation = "÷"

    # Display result nicely
    print("\n" + "=" * 40)
    print(f"  {num1} {operation} {num2}  =  {result}")
    print("=" * 40)

    # Show result with more decimal places if needed
    if result != int(result):
        print(f"  (≈ {result:.4f})")

    print("\nThank you for using the calculator! 💛")


# Run the calculator
if __name__ == "__main__":
    calculator()

    # Optional: ask if user wants to calculate again
    while True:
        again = input("\nCalculate again? (y/n): ").strip().lower()
        if again == 'y':
            print("\n" + "-" * 40 + "\n")
            calculator()
        elif again == 'n':
            print("\nGoodbye! Have a great day! ☀️")
            break
        else:
            print("Please type 'y' or 'n'")