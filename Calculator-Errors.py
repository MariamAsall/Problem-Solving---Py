def perform_operation(a, b, operation):
    try:
        if operation == '+':
            result = a + b
        elif operation == '-':
            result = a - b
        elif operation == '/':
            result = a / b
        elif operation == '*':
            result = a * b
        else:
            raise ValueError("Invalid operation.")
        
        # Print the result here
        print(f"The result of {a} {operation} {b} is: {result}")
    
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except OverflowError:
        print("Error: Overflow error occurred.")
    except TypeError:
        print("Error: Invalid type error.")
    except ValueError as ve:
        print(f"Error: {ve}")

def get_number(prompt): # function to ask user for input 
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number.")

def calculator():
    print("Welcome to the simple interactive calculator.")
    
    #This keeps the calculator running, allowing the user to perform multiple operations in a single session.

    while True:
        a = get_number("Enter the first number: ")
        b = get_number("Enter the second number: ")
        operation = input("Enter the operation (+, -, *, /): ").strip() #removes any extra spaces using strip()

        # Perform the selected operation
        perform_operation(a, b, operation)

        # Check if user wants to continue
        cont = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if cont != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break

# Run the calculator program
calculator()
