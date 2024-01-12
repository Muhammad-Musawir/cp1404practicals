class Band:
    def __init__(self, name, musicians):
        self.name = name
        self.musicians = musicians

    def play(self):
        print(f"{self.name} is playing:")
        for musician in self.musicians:
            if musician.instruments:
                print(f"{musician.name} ({', '.join(str(inst) for inst in musician.instruments)}) is playing.")
            else:
                print(f"{musician.name} needs an instrument!")
