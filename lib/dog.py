#!/usr/bin/env python3
class Dog:

    APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
 ]


    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        
    def get_name (self):
        
        return self.name
    
    def breed (self):
        return self.breed
    
    
    def set_name (self, new_name):
        if isinstance(new_name, str) and (1<= len(new_name) <= 25):
            print(f"setting name to {new_name}.")
            self.name = new_name
        else:
            print("Name must be string of 1 to 25 characters")  

    new_name = property(get_name, set_name,)   

    def set_breed (self, new_breed):
        if new_breed in self.APPROVED_BREEDS:
            print (new_breed) 
            self.breed = new_breed
        else:
            print ("Breed must be in the list of approved breeds")  

    new_breed = property (breed,set_breed,)            

dog= Dog("fido", "Beagle")
print(dog.name)
print(dog.breed)
dog.new_name = "woof"*30
dog.new_breed = "wolverine"

