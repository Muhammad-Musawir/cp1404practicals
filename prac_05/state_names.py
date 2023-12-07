"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

while True:
    try:
        user_input = input("Enter a state code: ").upper()  # Convert to uppercase for case-insensitivity
        name = CODE_TO_NAME[user_input]
        print(f'{user_input: <4} is {name}')
        break
    except KeyError:
        print(f'Error: {user_input} is not a valid state code. Please try again.')


for state_code, state_name in CODE_TO_NAME.items():
    print(f"{state_code: <4} is {state_name}")


