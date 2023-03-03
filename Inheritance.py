






#Creating the parent class for a basic character template that both child classes will inherit
class Toon_Temp:
    name = ' ' 
    health = 100 #Starting health for each character
    speed = 50 #Starting spped for each character
    intell = 50 #Starting intelligence for each charater 
        


#This will creat an 'Alliance' child lass that inherits the basic character template of 'Toon_Temp'
class Ally_Faction(Toon_Temp):
    start_loc = 'Albion' #Denotes the starting location for an Alliance character
    starting_mount = True #Alliance characters start with a mount
    light_bonus = 5 #Alliance characters start with a 'light' bonus of +5
    starting_shield = 15 #Alliance characters have a starting shield of +15
    
    
    

#This will create an 'Horde' child class that inherits the basic character template of 'Toon_Temp'

class Horde_Faction(Toon_Temp):
    start_loc = 'Shadowlands'#Denotes the starting location for a Horde character
    flight = True #Horde characters start with the flight ability
    dark_bonus = 5 #Horde charaters start with a 'dark' bonus of +5
    starting_minion = 'Glo-Bat' #Hord characters start with the 'Glo-Bat' minion
    
