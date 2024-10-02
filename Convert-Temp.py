def convert_temperature(value, from_scale, to_scale):
    try:
        # Ensure the input value is a number
        value = float(value)

        # Perform conversion based on input scales
        if from_scale == 'C':
            if to_scale == 'F':
                result = (value * 9/5) + 32
            elif to_scale == 'K':
                result = value + 273.15
            elif to_scale == 'C':
                result = value
            else:
                raise ValueError("Invalid target scale.")
        elif from_scale == 'F':
            if to_scale == 'C':
                result = (value - 32) * 5/9
            elif to_scale == 'K':
                result = (value - 32) * 5/9 + 273.15
            elif to_scale == 'F':
                result = value
            else:
                raise ValueError("Invalid target scale.")
        elif from_scale == 'K':
            if to_scale == 'C':
                result = value - 273.15
            elif to_scale == 'F':
                result = (value - 273.15) * 9/5 + 32
            elif to_scale == 'K':
                result = value
            else:
                raise ValueError("Invalid target scale.")
        else:
            raise ValueError("Invalid source scale.")

        return result
    except ValueError as ve:
        print(f"Error: {ve}")
    except TypeError:
        print("Error: Invalid type for temperature value.")
    except OverflowError:
        print("Error: Temperature value out of range.")
    return None


def get_temperature(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number.")


# Interactive session begins
print("Temperature Conversion Tool")
continue_converting = True

while continue_converting:
    # Get the temperature value from the user
    value = get_temperature("Enter the temperature value: ")

    # Get the source and target scales
    from_scale = input("Enter the source scale (C/F/K): ").upper()
    to_scale = input("Enter the target scale (C/F/K): ").upper()

    # Perform the conversion and handle exceptions
    result = convert_temperature(value, from_scale, to_scale)

    if result is not None:
        print(f"The converted temperature is: {result:.2f} {to_scale}")

    # Ask if the user wants to perform another conversion
    cont = input("Do you want to convert another temperature? (yes/no): ").lower()
    continue_converting = (cont == 'yes')


