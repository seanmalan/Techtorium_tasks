
class Car:
  
  def __init__ (self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
    print(f"Car created was {self.make} {self.model} {self.year}")
    
  
  def start_engine(self):
    print("Engine started")
    print(f"{self.make} {self.model} {self.year} is running")
    
  def get_descriptive_name(self):
    long_name = str(self.year) + ' ' + self.make + ' ' + self.model
    return long_name.title()
  
  def __del__(self):
        print('Destructor called, this class was deleted.')
        

class default_car(Car):
  def __init__(self, make="lada", model="ladouwski", year=1981):
    self.make = make
    self.model = model
    self.year = year
    print(f"Default Car created was {self.make} {self.model} {self.year}")


cars = []

print(f"there are {len(cars)} at the start")

my_new_audi = Car('audi', 'a4', 2016)
print(my_new_audi.get_descriptive_name())
my_new_audi.start_engine()

me_new_bmw = Car("Toyota", "Supra", 1996)
my_new_porche = Car("Porsche", "911 GT3RS", 2023)
my_new_toyota = Car("Toyota", "Corolla", 1996)
my_new_toyota.start_engine()
cars.extend([my_new_audi, me_new_bmw, my_new_porche, my_new_toyota])


default = default_car()
default.start_engine()

default_override = default_car("Porsche", "911 GT3RS", 2023)
default_override.start_engine()

cars.extend([default, default_override])

for car in cars:
  print(f"Car is {car.get_descriptive_name()}")

print(f"there are {len(cars)} at the end")