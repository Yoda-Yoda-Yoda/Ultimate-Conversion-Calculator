# Generates headings (eg: ----- Heading -----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


statement_generator("Welcome to the Ultimate Conversion Calculator", "-")


# Displays instructions
def instructions():
    statement_generator("Details and Instructions", "-")

    print('''
Ultimate Conversion Calculator - Step-by-Step Guide\n

1. Enter the "From" Unit:
When prompted, type the unit you want to convert from (e.g., cm for centimeters, g for grams).
Press Enter.
2. Enter a Number:
After selecting the "from" unit, you’ll be asked to input the number you wish to convert (e.g., 100).
Type the number and press Enter.
3. Enter the "To" Unit:
Next, you will be prompted to enter the unit you want to convert to (e.g., m for meters, kg for kilograms).
Type the "to" unit and press Enter.


    ''')


def get_unit():

    while True:
        response = input("Type: ")

        # check for 'i' or the exit code
        if response == "xxx":
            return "exit"

        # check if it's time
        elif response in ['s', 'seconds', 'm', 'minutes' 'h', 'hour', 'd', 'day', 'time']:
            return "time"

        # check for an Distance ...
        elif response in ['mm', 'cm', 'm', 'km', 'dist', 'distance']:
            return "distance"

        # check for text
        elif response in ['mg', 'g', 'kg', 'mass', 'weight']:
            return "mass"

        elif response in ['ml', 'l', 'liquid']:
            return "liquid"

        elif response in ['b', 'kb', 'mb', 'gb', 'data']:
            return "data"

        # if the response is invalid output an error
        else:
            print("Please enter a valid file type")


def distance():
    distance_dict = {
        "mm": 1000,
        "cm": 100,
        "m": 1,
        "km": .001
    }

    # Get amount and unit (assume they are valid)
    amount_dist = float(input("how much?  "))
    from_unit_dist = input("From unit?  ")
    to_unit_dist = input("To Unit?  ")

    # multiply to get to our standard value...
    multiply_by = distance_dict[to_unit_dist]
    standard = amount_dist * multiply_by

    # Divide to get to our desired value
    divide_by = distance_dict[from_unit_dist]
    answer = standard / divide_by

    print(f"There are {answer} {to_unit_dist} in {amount_dist} {from_unit_dist}")


def time():
    time_dict = {
        "s": 86400,
        "seconds": 86400,
        "m": 1440,
        "minutes": 1440,
        "h": 24,
        "hour": 24,
        "d": 1,
        "day": 1
    }
    # Get amount and unit (assume they are valid)
    amount_time = float(input("how much: "))
    from_unit_time = input("From unit?  ")
    to_unit_time = input("To unit?")

    # multiply to get to our standard value...
    multiply_by = time_dict[to_unit_time]
    standard = amount_time * multiply_by

    # Divide to get to our desired value
    divide_by = time_dict[from_unit_time]
    answer = standard / divide_by

    print(f"There are {answer} {to_unit_time} in {amount_time} {from_unit_time}")


def mass():
    mass_dict = {
        "mg": 1000000,
        "g": 1000,
        "kg": 1
    }

    # Get amount and unit (assume they are valid)
    amount_mass = float(input("how much: "))
    from_unit_mass = input("From unit?  ")
    to_unit_mass = input("To unit?")

    # multiply to get to our standard value...
    multiply_by = mass_dict[to_unit_mass]
    standard = amount_mass * multiply_by

    # Divide to get to our desired value
    divide_by = mass_dict[from_unit_mass]
    answer = standard / divide_by

    print(f"There are {answer} {to_unit_mass} in {amount_mass} {from_unit_mass}")


def volume_liquid():
    liquid_dict = {
        "ml": 1000,
        "l": 1

    }

# Get amount and unit (assume they are valid)
    amount = float(input("how much: "))
    from_unit = input("From unit?  ")
    to_unit = input("To unit?")

    # multiply to get to our standard value...
    multiply_by = liquid_dict[to_unit]
    standard = amount * multiply_by

    # Divide to get to our desired value
    divide_by = liquid_dict[from_unit]
    answer = standard / divide_by

    print(f"There are {answer} {to_unit} in {amount} {from_unit}")


def data():
    data_dict = {
        "b": 1000000,
        "kb": 1000,
        "mb": 1,
        "gb": 0.001,

    }

# Get amount and unit (assume they are valid)
    amount = float(input("how much: "))
    from_unit = input("From unit?  ")
    to_unit = input("To unit?")

    # multiply to get to our standard value...
    multiply_by = data_dict[to_unit]
    standard = amount * multiply_by

    # Divide to get to our desired value
    divide_by = data_dict[from_unit]
    answer = standard / divide_by

    print(f"There are {answer} {to_unit} in {amount} {from_unit}")


# Display instruction if requested
want_instructions = input("\nPress <enter> to read the instruction "
                          "or any key to continue ")

if want_instructions == "":
    instructions()


while True:
    unit_type = get_unit()

    if unit_type == "distance":
        distance()

    elif unit_type == "time":
        time()

    elif unit_type == "mass":
        mass()

    elif unit_type == "liquid":
        volume_liquid()

    elif unit_type == "data":
        data()

    elif unit_type == "exit":
        break
