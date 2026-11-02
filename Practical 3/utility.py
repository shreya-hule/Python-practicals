"""MCA Semester I - Python Programming
Practical 3: Control Flow & Utility Functions
Menu-driven CLI calculator.
"""


def show_menu():
    print("\n=== Utility Calculator ===")
    print("1. Add numbers")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Show summary")
    print("6. Average of three numbers")   # Extension Task A
    print("0. Exit")


def get_number(prompt="Enter a number: "):
    # Default argument: prompt. Loops until the user types a valid number.
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Enter a numeric value.")


def add(*args):
    # *args collects any number of positional values into a tuple.
    return sum(args)


def calculate(a, b, operation="+"):
    # Default argument: operation defaults to "+".
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
    else:
        raise ValueError("Unsupported operation.")


def average(*numbers):
    # Extension Task A: reusable function, works for any count of numbers.
    if not numbers:
        raise ValueError("average() needs at least one number.")
    return sum(numbers) / len(numbers)


def show_summary(**kwargs):
    # **kwargs collects named values into a dictionary.
    print("\n--- Summary ---")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def main():
    history = []                                  # local to main()
    format_result = lambda value: f"{value:.2f}"  # lambda: 2 decimal places

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "0":
            print("Goodbye!")
            break
        elif choice not in {"1", "2", "3", "4", "5", "6"}:
            print("Invalid menu choice. Try again.")
            continue
        elif choice == "5":
            show_summary(
                total_calculations=len(history),
                last_result=history[-1] if history else "No calculations yet"
            )
            continue
        elif choice == "6":
            x = get_number("First number: ")
            y = get_number("Second number: ")
            z = get_number("Third number: ")
            result = average(x, y, z)
            print(f"Result (average): {format_result(result)}")
            history.append(result)
            continue

        a = get_number("First number: ")
        b = get_number("Second number: ")

        if choice == "1":
            result = add(a, b)
            label = "addition"
        elif choice == "2":
            result = calculate(a, b, "-")
            label = "subtraction"
        elif choice == "3":
            result = calculate(a, b, "*")
            label = "multiplication"
        else:
            try:
                result = calculate(a, b, "/")
            except ZeroDivisionError as error:
                print("Error:", error)
                continue
            label = "division"

        print(f"Result ({label}): {format_result(result)}")
        history.append(result)


if __name__ == "__main__":
    main()
