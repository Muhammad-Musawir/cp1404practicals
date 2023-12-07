COLOUR_TO_CODE = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff", "Alizarin crimson": "#e32636",
                "Baby Blue": "#89cff0", "Cadet Grey": "#91a3b0", "Barn Red": "#7c0a02"}
print(COLOUR_TO_CODE)

while True:
    try:
        user_input = input("Enter a colour name: ").upper()
        name = COLOUR_TO_CODE[user_input]
        print(f'{user_input: <4} is {name}')
        break
    except KeyError:
        print(f"{user_input} is not a valid state code. Please try again.')