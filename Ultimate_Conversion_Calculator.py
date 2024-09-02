# Generates headings (eg: ----- Heading -----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("Details and Instructions", "-")

    print('''
    aa

    ''')


def get_unit():

    while True:
        response = input("Unit: ")

        # check for 'i' or the exit code
        if response == "xxx":
            break

        # check if it's time
        elif response in ['s', 'h' 'hour']:
            return "time"

        # check for an image...
        elif response in []:
            return ""

        # check for text
        elif response in ["text", 'txt', 't']:
            return "text"

        # if the response is invalid output an error
        else:
            print("Please enter a valid file type")


# Display instruction if requested
want_instructions = input("\nPress <enter> to read the instruction "
                          "or any key to continue ")

if want_instructions == "":
    instructions()
