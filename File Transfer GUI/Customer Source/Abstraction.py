
# This demonstrates the concept of abstraction

# Importing the Abstract Base classes (ABC) module
from abc import ABC, abstractmethod

# This is establishing an abstract base class with functions that must be created in each child class
class Ships(ABC):
    # This regular method will be applied to each child class and advises that a second positional argument is required
    def x(self,comm):
        print("\nI love Star Wars!",comm) # Printing to a new line for spacing
    # This is an abstract method; It declares a blueprint for the child classes to follow
    @abstractmethod # This keyword ensures that the method is abstract
    def type_info(self):
        pass

# This creates a child class of 'Ships'
class Starfigher(Ships):
    # This method overrides the abstract method in the parent classe and prints a unique statement to the child class.
    def type_info(self):
        print("Starfighter ships include TIE Fighters, Naboo N-1 Starfighter, TIE Bomber, and of course X-Wings.")

class Cargo(Ships):
    def type_info(self):
        print("Cargo ships include YT-1300 Light Freighters(Millennium Falcon!), J-Type Star Skiffs, and H-Type Nubian Yachts.")

class Battleship(Ships):
    def type_info(self):
        print("Battleships include Imperial Star Destroyers, Separatist Dreadnoughts, MC85 Star Cruisers, and Trade Federation Battleships.")

class Super_Weapon(Ships):
    def type_info(self):
        print("Super Weapons (that are also ships) include the Death Star and the Death Star II.")


# This is creating objects out of the child classes above to manipulate and print
a = Starfigher()
# This pass a string argument through the regular method defined in the parent class, appending a unique statement to the created object
a.x("Starfighters are some of the most recognizable ships in the SW universe.")
# This prints the newly manipulated child class object that is distinctive from the others
a.type_info()

b = Cargo()
b.x("Cargo ships are cooler than you think! You might be familiar with one...")
b.type_info()

c = Battleship()
c.x("I would steer clear of these behemoths. Watch out for that tractor beam!")
c.type_info()

d = Super_Weapon()
d.x("Super Weapons are the ace card of the Empire. Mezmerizingly frightening.")
d.type_info()
