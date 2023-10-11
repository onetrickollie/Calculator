import json
from calculator import add, subtract, multiply, divide

def get_float_input(prompt):
    valid_input = False
    while not valid_input:
        try:
            num = float(input(prompt))
            valid_input = True
            return num
        except ValueError:
            print("Invalid input. Please enter a valid floating-point number.")

def main():
    print("Welcome to the Calculator App")

    num1 = get_float_input("Enter the first number: ")
    num2 = get_float_input("Enter the second number: ")

    results = {
        "num1": num1,
        "num2": num2,
        "addition": add(num1, num2),
        "subtraction": subtract(num1, num2),
        "multiplication": multiply(num1, num2)
    }

    try:
        results["division"] = divide(num1, num2)
    except ZeroDivisionError:
        results["division"] = "Error: Division by zero is not allowed."

    output_file = input("Enter the name of the JSON file to save the results: ")

    try:
        with open(output_file, 'w') as json_file:
            json.dump(results, json_file)
        print("Results saved to", output_file)
    except Exception as exc:
        print("Error: Failed to save results to the JSON file.", str(exc))

if __name__ == "__main__":
    main()
