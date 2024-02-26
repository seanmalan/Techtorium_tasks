class Animal:
    def __init__ (self, sound = "default bark"):
        self.sound = sound
        print("inside the animal class")
        
        
        
    def make_sound(self):
        print(self.sound)
        ("inside the animal class")          
        return "default bark"
            
            
            
class Dog(Animal):
    def __init__ (self, sound = "bark"):
        super().__init__(sound)
        print("inside the dog class")
        

dog2 = Dog()
dog2.make_sound()
dog_bark = Dog("woof")
dog_bark.make_sound()

#dog_bark.make_sound()

# The code above will print "bark" to the console.

