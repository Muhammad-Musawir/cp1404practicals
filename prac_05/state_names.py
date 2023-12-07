"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

for state_code in CODE_TO_NAME:
    try:
        user_input = input("Enter a state code: ").upper()
        name = CODE_TO_NAME[state_code]
        print(f'{state_code: <4} is {name}')
    except KeyError:
        print(f'Error: {state_code} is not a valid state abbreviation')


for state_code, state_name in CODE_TO_NAME.items():
    print(f"{state_code: <4} is {state_name}")


