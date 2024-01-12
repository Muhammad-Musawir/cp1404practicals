from prac_06.car import Car
from prac_09.taxi import Taxi
def main():
    my_taxi = Taxi("Prius 1",100)
    my_taxi.drive(40)
    print(f"Taxi details: {my_taxi}\n"
          f"Current far: {my_taxi.get_fare()}")

    my_taxi.start_fare()
    my_taxi.drive(100)
    print(f"Taxi details: {my_taxi}\n"
          f"Current far: {my_taxi.get_fare()}")

main()