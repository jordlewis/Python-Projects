

# Demonstrating private and protected variables within the same class

class Characters:
    def __init__(self,name,age,power):
        self.name = name #This is a public variable, accessible inside/outside of the Characters class
        self._age = age #This is a protected variabe, only accessible within the Character class and (potential) child classes
        self.__power = power #This is a private variable, only accessible from within the Character class

# This function will display the object that has been instantiat
    def display(self):
        print("You chose", self.name, "who is", self._age, "years old with the power of", self.__power)

# This function utilizes the 'get' method to access the private variable 'power'
    def get_Priv(self):
        return self.__power

# This function utilizes the 'set' method to change the private variable 'power'
    def set_Priv(self,priv):
        self.__power = priv
        return priv

    


        
# Creating a Chewbacca object of the Characters class 
chewy_obj = Characters("Chewy", 234, "rrrooaarrgghh!")

# Displyaing the Chewbacca object that we instantiated
chewy_obj.display()

# This is manipulating the public name variable "Chewy" to "Yoda"
chewy_obj.name = "Yoda"

# This is accessing the protected variable 'age' and changing it from 234 to 900
chewy_obj._age = 900

# This is accessing the private variable 'power'
chewy_obj.get_Priv

# This is setting the private variable 'power' from "rrrooaarrgghh!" to "The Force"
chewy_obj.set_Priv("The Force")

# This is displaying the freshly manipulated object 'chewy_obj', with newly assigned characteristics
chewy_obj.display()




