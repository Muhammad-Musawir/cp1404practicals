from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi
def main():
    print("Let's drive!")

    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_bill = 0

    while True:
        display_menu(taxis)
        option = input(">>> ").lower()

        if option == 'q':
            break
        elif option == 'c':
            current_taxi = choose_taxi(taxis)
        elif option == 'd':
            fare = drive_taxi(current_taxi)
            total_bill += fare

        print(f"Bill to date: ${total_bill:.2f}")

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)

def display_menu(taxis):
    print("q)uit, c)hoose taxi, d)rive")
    display_taxis(taxis)

def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def choose_taxi(taxis):
    display_taxis(taxis)
    taxi_choice = input("Choose taxi: ")
    try:
        taxi_choice = int(taxi_choice)
        if 0 <= taxi_choice < len(taxis):
            return taxis[taxi_choice]
        else:
            print("Invalid taxi choice")
            return None
    except ValueError:
        print("Invalid option")
        return None

def drive_taxi(taxi):
    if taxi is None:
        print("You need to choose a taxi before you can drive")
        return 0
    distance = float(input("Drive how far? "))
    fare = taxi.drive(distance)
    print(f"Your {taxi.name} trip cost you ${fare:.2f}")
    return fare

if __name__ == "__main__":
    main()
