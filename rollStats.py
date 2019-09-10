#RefresherApp
#Imports
import random
import sys

#Variables
name = ""
stats = [0]*9
sentinel = 1

#Input Name
print ("Input Name")
name = input()
print ("Welcome ",name)


#Function Roll 3 6 sided Dice
def roll3D6():
    roll = 0
    #Random Number Between 1 & 6 * 3
    for _ in range(3):
        roll += random.randint(1,6)
    roll = 5 * roll
    return roll

#Roll 2 6 sided Dice & add 6
def roll2D6():

    roll = 0
    for _ in range(2):
        roll += random.randint(1,6)
    roll = 5 * (roll +6)
    return roll

#While 0 is not entered Reroll Stats
while sentinel != 0:
    #Roll Stats
    stats[0] = roll3D6()
    stats[1] = roll3D6()
    stats[2] = roll2D6()
    stats[3] = roll3D6()     
    stats[4] = roll3D6()
    stats[5] = roll2D6()
    stats[6] = roll3D6()
    stats[7] = roll2D6()
    stats[8] = roll3D6()
    #Print stats
    print ("Str: ",stats[0])
    print ("Con: ",stats[1])
    print ("Siz: ",stats[2])
    print ("Dex: ",stats[3])
    print ("App: ",stats[4])
    print ("Int: ",stats[5])
    print ("Pow: ",stats[6])
    print ("Edu: ",stats[7])
    print ("Lck: ",stats[8])
    #Reroll or Exit
    print ("Input 0 to Exit or any key to Reroll")
    sentinel = int(input())
    print ("Exited")
