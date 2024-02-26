#python object clean up

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person created was {self.name} {self.age}")
        
        
    '''def print_user(self):
        print(f"user {self.name} is {self.age} years old")'''

    def __del__(self):
        print('Destructor called, this class was deleted.')

def delete_object(p1):
    del p1
    print("object deleted")
    
        
p1 = Person('John', 36)

print(p1.name)
delete_object(p1)



# print(p1) #this will cause an error because the object has been deleted
        

