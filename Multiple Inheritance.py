class Person:
  def __init__ (self, name, age):
    self.name = name
    self.age = age
    print ("Person created")
    print(f"Person created was {self.name} and {self.age} years old")
    
    
class Skills(Person):
  def __init__ (self, name, age, programming_skills, communication_skills):
    super().__init__(name, age)
    self.programming_skills = programming_skills
    self.communication_skills = communication_skills
    print ("Skills created")
    print(f"Skills created was {self.programming_skills} & {communication_skills}")
    
    
class Employee(Skills):
  def __init__ (self, name, age, programming_skills, communication_skills, company, position):
    super().__init__(name, age, programming_skills, communication_skills)
    self.company = company
    self.position = position
    print ("Employee created")
    print(f"Employee created was {self.company} & {self.position}")
    

Employee1 = Employee("John", 25, "Python", "Good", "Google", "Software Engineer")
