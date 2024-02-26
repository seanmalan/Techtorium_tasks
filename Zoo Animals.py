class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Generic animal sound")

class Mammal(Animal):
    def __init__(self, name, species, fur_color):
        super().__init__(name, species)
        self.fur_color = fur_color

    def give_birth(self):
        print(f"{self.name} is giving birth")

class Bird(Animal):
    def __init__(self, name, species, feather_color):
        super().__init__(name, species)
        self.feather_color = feather_color

    def fly(self):
        print(f"{self.name} is flying")


Cockatoo = Bird("Cockatoo", "Parrot", "White")
print(f"{Cockatoo.name} is a {Cockatoo.species} with {Cockatoo.feather_color} feathers")

seal = Mammal("Seal", "Mammal", "Grey")
print(f"{seal.name} is a {seal.species} with {seal.fur_color} fur")



#Scenario 2: School Subjects
class Subject:
    def __init__(self, name):
        self.name = name

    def study(self):
        print(f"Studying {self.name}")

class Math(Subject):
    def __init__(self, name, difficulty_level):
        super().__init__(name)
        self.difficulty_level = difficulty_level

    def solve_problem(self):
        print(f"Solving a {self.difficulty_level} math problem")

class Language(Subject):
    def __init__(self, name, language_type):
        super().__init__(name)
        self.language_type = language_type

    def practice_language(self):
        print(f"Practicing {self.language_type} language")
        
math = Math("Geometery", "Hard")
print(f"{math.name} is a {math.difficulty_level} subject")
calculus = Math("Calculus", "Very Hard")
print(f"{calculus.name} is a {calculus.difficulty_level} subject")


Spanish = Language("Spanish", "Foreign")
print(f"{Spanish.name} is a {Spanish.language_type} language")