def calculator_AimanAsghar():
    print("--- Smart Calculator ---")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        addition = num1 + num2
        subtraction = num1 - num2
        multiplication = num1 * num2
        if num2 != 0:
            division = num1 / num2
        else:
            division = "Undefined (cannot divide by zero)"
        print(f"\nResults for {num1} and {num2}:")
        print(f"Addition: {addition}")
        print(f"Subtraction: {subtraction}")
        print(f"Multiplication: {multiplication}")
        print(f"Division: {division}")
    except ValueError:
        print("\nError: Invalid input! Please enter numeric values only.")
def guessing_game_UswaFatima():
    print("\n[!] The Guessing Game feature is currently under construction by the teammate.")
def main_menu():
    while True:
        print("\n==========================")
        print("   PYTHON PROJECT MENU    ")
        print("==========================")
        print("1. Smart Calculator ")
        print("2. Guessing Game ")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            calculator_AimanAsghar()
        elif choice == '2':
            guessing_game_UswaFatima()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
if __name__ == "__main__":
    main_menu()