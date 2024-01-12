from prac_09.taxi import Taxi
class SilverServiceTaxi(Taxi):
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self, distance):
        base_fare = super().get_fare()
        total_fare = base_fare + self.flagfall + (distance * self.price_per_km)
        return total_fare
    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"