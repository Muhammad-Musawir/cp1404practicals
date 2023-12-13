from prac_06.guitar import Guitar
def main():
    print("My guitars!")

    guitars = []
    while True:
        name = input("Name: ")
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
    guitars = [
        Guitar("Gibson L-5 CES", 1922, 16035.40),
        Guitar("Line 6 JTV-59", 2010, 1512.9),
        Guitar("Fender Stratocaster", 2014, 765.4)
    ]

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage(2022) else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:,.2f}{vintage_string}")


main()