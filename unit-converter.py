def convert_length(value, choice):
    if choice == "km":
        return value*0.621371
    elif choice == "miles":
        return value*1.60934
    else:
        return None

def convert_temperature(value, choice):
    if choice == "celsius":
        return (value * 9/5) + 32
    elif choice == "fahrenheit":
        return (value - 32) * 5/9
    else:
        return None

def convert_weight(value, choice):
    if choice == "lbs":
        return value*2.20462
    elif choice == "kg":
        return value/2.20462
    else:
        return None
    

def main():
    print("\n--- Welcome to Unit Converter ---")
    print("Menu: ")
    print("1. Length")
    print("2. Temperature")
    print("3. Weight")


    try: 
        dimension = int(input("Select dimension number: "))
        value = float(input("Enter value to be converted: "))
        choice = input("Enter unit of value to be converted: ").lower()
        if dimension == 1:
            result = convert_length(value, choice)
            if result is None:
                print("Invalid unit")
            else:
                print(result)
        elif dimension == 2:
            result = convert_temperature(value, choice)
            if result is None:
                print("Invalid unit")
            else:
                print(result)
        elif dimension == 3:
            result = convert_weight(value, choice)
            if result is None:
                print("Invalid unit")
            else:
                print(result)

    except ValueError:
        print("Enter a valid number!")
        

if __name__ == '__main__':
    main()