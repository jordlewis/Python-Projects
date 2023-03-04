

#parent class for Star Wars characters

class Character:
    def sw_verbiage(self): #This will show umodified when printed for each child class and will print the paragraph on a new line.
        print("\nA long time ago in a galaxy far, far away....")
    def change(self): #This method will vary based upon the child class. It is polymorphic.
        print("Good and evil was divided into the Light and Dark sides of The Force")

#below are the child classes of the parent class 'Characters;
class Jedi(Character):
    def change(self): #This will overwrite the parent method to print a statement about the Jedi. It is polymorphic.
        print("The Jedi were protectors of the galaxy, forming the Light side of The Force")
    def names(self): #This will print another statement that is specific to the Jedi child class
        print("Obi-Wan, Yoda, Master Windu and Luke Skylwalker are to name a few...")

class Sith(Character):
    def change(self): #This will overwrite the parent method to print a statement about the Sith. It is polymorphic.
        print("The Sith sought to fulifill their own desires, fallen to the Dark side..")
    def names(self): #This will print another statement that is specific to the Sith child class
        print("Darth Vader, Lord Palpatine, and Count Dooku were a notable sort..")

#Below will assign a variable to each class

a = Character() 
b = Jedi()
c = Sith()

#Below will call both methods inside the Character class (a) and print general Star Wars information to the console

a.sw_verbiage()
a.change()

#Below will call both methods inside the Jedi class (b) and print general Jedi information to the console

b.sw_verbiage()
b.change()
b.names()

#Below will call both methods inside the Sith class (C) and print general Sith information to the console

c.sw_verbiage()
c.change()
c.names()
