from prac_09.unreliable_car import UnreliableCar
def main():
    my_unreliable_car = UnreliableCar("limo",100,50)
    for i in range(10):
        distance = 20
        distance_driven = my_unreliable_car.drive(distance)

        if distance_driven > 0:
            print(f"Successfully drove {distance_driven} km.")
        else:
            print("Your Car is not reliable.")

        # Print the details of the unreliable car
    print(f"\nUnreliable Car details: {my_unreliable_car}")

main()