class Vehicle:
  def __init__ (self, name = "Petrol"):
    self.name = name
    
    
  def start_engine(self):
    print(f"{self.name} Vehicle engine started")
      
      
class Car(Vehicle):
  pass
      
class ElectricCar(Vehicle):
  def charge_battery(self):
    print(f"{self.name} Battery charging")
    



car = Car()
car.start_engine()

electric_car = ElectricCar("Electric")
electric_car.start_engine()

electric_car = ElectricCar("Nissan Leaf")
electric_car.charge_battery()

vehicle = Vehicle()
vehicle.start_engine()