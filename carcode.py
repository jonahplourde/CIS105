class Car:
    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self.__year = year

    def get_description(self):
        return f"{self.get_year()} {self._make} {self._model}"
    
    def start_engine(self):
        print(f"{self._make} engine started.")

    def get_year(self):
        return self.__year
    
    def set_year(self, year):
        if year > 1885:
            self.__year = year
        else:
            print("Please enter a valid year.")

class eCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def get_description(self):
        base_desc = super().get_description()
        return f"{base_desc} with a {self.battery_size}-kWh battery"

    def start_engine(self):
        print(f"{self._make} electric engine started silently.")

    def charge_battery(self):
        print(f"Charging the {self.battery_size}-kWh battery.")

class gasCar(Car):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def start_engine(self):
        print(f"{self._make} {self.fuel_type} engine started with a roar.")

    def refuel(self):
        print(f"Refueling the {self.fuel_type} tank.")

def start_car(car: Car):
    car.start_engine()

tesla = eCar("Tesla", "Model S", 2020, 100)
mustang = gasCar("Ford", "Mustang", 1967, "gasoline")

start_car(tesla) # Can also do tesla.start_car()
start_car(mustang)

print(tesla.get_description())
print(mustang.get_description())
