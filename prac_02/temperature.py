"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion

MENU = "C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"
display "MENU"
get choice
while choice != "Q":
    if choice == "C":
        get celsius
        fahrenheit = celsius * 9.0 / 5 + 32
        display "fahrenheit"
    elif choice == "F":
        # TODO: Write this section to convert F to C and display the result
        get fahrenheit
        celsius = 5 / 9 * (fahrenheit - 32)
    else:
        display "Invalid option"
    display "MENU"
    get choice
display "Thank You"
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            fahrenheit = convert_celsius()
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            celsius = convert_fahrenthiet()
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_fahrenthiet():
    fahrenheit = float(input("fahrenheit:"))
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def convert_celsius():
    celsius = float(input("Celsius:"))
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit