def calculate_division(x, y):
    try:
        result = x/y 
        print("Result of division:", result)
    except ZeroDivisionError:
        print("Error: Can't Divide by Zero.")
    except ValueError:
        print("Erorr: please enter valid numbers.")
    except OverflowError:
        print("Error: result is too large to compute.")
    except Exception as E:
        print("An expected error occured:", E)

try:
    numerator = int(input("Enter the Numerator: "))
    denomerator = int(input("Enter the denomerator: "))
    calculate_division(numerator,denomerator)
except ValueError:
    print("Erorr: please enter valid numbers.")

