class Samochod:

    def __init__(self, marka, model, rok_produkcji, przebieg):
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji
        self.przebieg = przebieg

    def __str__(self):
        return f"Marka: {self.marka}, Model: {self.model}, Rok produkcji: {self.rok_produkcji}, Przebieg: {self.przebieg} "

    def __lt__(self, other):
        if self.przebieg < other.przebieg:
            return True
        else:
            return False

s1 = Samochod("Opel", "Astra", 2005, 250000)
s2 = Samochod("VW", "Passat", 2007, 194000)
s3 = Samochod("Citroen", "C4", 2008, 188000)
print(s1)
print(s2)
print(s3)

print(s2 < s1)
print(s1 < s3)
print(s3 < s2)
