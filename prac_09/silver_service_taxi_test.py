from silver_service_taxi import SilverServiceTaxi

def main():
    bently_taxi = SilverServiceTaxi("Bentley", 100, 3)
    print(bently_taxi)
    print(f"Total fare for the trip = ${bently_taxi.get_fare(20):.2f}")

if __name__ == "__main__":
    main()
