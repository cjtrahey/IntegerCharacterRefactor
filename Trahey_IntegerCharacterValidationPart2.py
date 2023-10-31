# Christopher-John Trahey
# Chapter 6 Homework (Part II)
# October 16, 2023
# This program refactors the previous assignment. It provides the same service without redundant code.
# Developed using Visual Studio Code.

# Print Menu Function Here

def print_menu():
    print('')
    print("*******************************************")
    print("* DATA VALIDATION MENU *")
    print("* *")
    print("* 1 - Validate Integer *")
    print("* 2 - Validate Character (bonus) *")
    print("* 3 - Exit Program *")
    print("* *")
    print("*******************************************")
    print('')

#Validate Integer Function Here

def validateInteger(prompt):
    valid_integer = False
    while not valid_integer:
        userInput = input(prompt)
        if userInput.isdigit():
            integerValue = int(userInput)
            if integerValue >= 0:
                print(f"You entered integer: {integerValue}")
                valid_integer = True
        if not valid_integer:
            print("Invalid Entry. Try again.")

#Validate Character Function Here

def validateChars(prompt, lowerBound, upperBound):
    validchars = [chr(i) for i in range(ord(lowerBound), ord(upperBound) + 1)]
    valid_char = False

    while not valid_char:
        charinput = input(prompt)
        if len(charinput) == 1 and charinput in validchars:
            charinput = charinput.upper()  # Convert to uppercase
            print(f"You entered character: {charinput}")
            valid_char = True
        if not valid_char:
            print("Invalid Entry. Try again.")

# Main Function goes here

def main():
    while True:
        print_menu()
        choice = input("Select a menu item: ")
        
        if choice == '1':
            validateInteger("Enter a positive integer >= 0: ")
        elif choice == '2':
            validateChars("Enter a character between 'a' and 'd' (upper or lower case): ", 'a', 'd')
        elif choice == '3':
            print("Exiting the program.")
            break  # To exit the main menu loop
        else:
            print("Invalid choice. Please select a valid menu option.")

# Invoke the main function here. In this way, when the program runs,
# it recognizes all the functions, but must have a starting point.
# This is that starting point (by invoking the main function).

if __name__ == "__main__":
    main()
