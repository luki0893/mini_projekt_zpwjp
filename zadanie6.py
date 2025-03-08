class Car:

    def __init__(self, make, model, year, mileage, price):
        self.make = make
        self.model = model
        self.year = year
        self._mileage = mileage
        self._price = price

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, value):
        if value >= self._mileage:
            self._mileage = value
        else:
            raise ValueError("Mileage cannot be decreased")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            raise ValueError("Price must be greater than zero")

    def __str__(self):
        return f"Make: {self.make}, model: {self.model}, year: {self.year}, mileage: {self.mileage}, price: {self.price}"

    def drive(self, distance):
        self.mileage += distance

    def calculate_depreciation(self, current_year):
        age = current_year - self.year
        depreciation_variable = 0.06 # zmienna przedstawiajaca roczny spadek wartosci auta o 6%
        mileage_depreciation_variable = 0.03 # zmienna zmiejszajaca wartosc o 3%
        depreciation = (age * depreciation_variable * self.price) + (self.mileage * mileage_depreciation_variable)
        new_value =  max(0, self.price - depreciation)
        return new_value

c1 = Car("Opel", "Astra", 2014, 240000, 96000)
c2 = Car("VW", "Golf", 2017, 192000, 101000)
c3 = Car("BMW", "M3", 2019, 155000, 213000)

# Car 1
print(c1.price)
print(c1.mileage)
c1.drive(20000)
print(f"Car's data after mileage update:\n {c1}")
new_price_c1 = c1.calculate_depreciation(2025)
print(f"New price: {new_price_c1} zl")

# Car 2
print(c2.price)
print(c2.mileage)
c2.drive(11000)
print(f"Car's data after mileage update:\n {c2}")
new_price_c2 = c2.calculate_depreciation(2025)
print(f"New price: {new_price_c2} zl")
