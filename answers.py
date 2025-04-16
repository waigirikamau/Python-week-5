# QUESTION 1
class superhero:    
def __init__(self, name, power, level):    
          self.name = name
          self.power = power
          self.level = level
def introduce(self):
        print(f"Hello, my name is {self.name}. I have the power of {self.power} and my level is {self.level}.")
   
# Subclass 1: Super Strength
class SuperStrength(superhero):
     def __init__(self, name, power, level, strength):
        super().__init__(name, power, level)    
         self.strength = strength

     def introduce(self):
         print(f"Hello, my name is {self.name}. I have the power of {self.power}, my level is {self.level}, and my strength is {self.strength}.")
# #Example usage
 SuperStrength_hero = SuperStrength("Super Strength", "Super Strength", 5, 100)
 SuperStrength_hero.introduce()  

 #Subclass 3: Telekinetic
 class Telekinetic(superhero):
     def __init__(self, name, power, level, levitation, force_field):
         super().__init__(name, power, level)    
         self.levitation = levitation
         self.force_field = force_field

     def introduce(self):
         print(f"Hello, my name is {self.name}. I have the power of {self.power}, my level is {self.level}, I can levitate: {self.levitation}, and I can create force fields: {self.force_field}.")

# Example usage
 telekinetic_hero = Telekinetic("Telekinetic", "Levitation", 5, True, True)
 telekinetic_hero.introduce()


# QUESTION 2
class Vehicle:
    def move(self):
        return("This vehicle moves in its own way.")
# Subclass 1
class Car(Vehicle):
    def move(self):
        return("Driving on the road ")

# Subclass 2
class Plane(Vehicle):
    def move(self):
        return("Flying in the sky ")

# Subclass 3
class Boat(Vehicle):
    def move(self):
        return("Sailing on water")

# Subclass 4
class Train(Vehicle):
    def move(self):
        return ("Running on tracks")
#subclass 5
class Bicycle(Vehicle):
        def move(self):
            return ("Pedaling on the road")
# Example usage
for vehicle in [Car(), Plane(), Boat(), Train(),Bicycle()]:
        print(vehicle.move())

 



