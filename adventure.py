# Name: Will Gatlin,  CPSC 230
# Imports
import random
import time
# Starting Input
entry = input('You are standing at the door of a castle and walk in. Which room would you like to go in? (Throne Room, Storage, Dining Hall, Kitchen)  ')

def death(): 
    time.sleep(1)
    num = random.randint(0,100) 
    if num > 95:  # If the number is more than 95 (5% chance) then you will die after entering a room
        num1 = random.randint(0,2)  # Gives 3 different scenarios for dying
        if num1 == 0:
            print('You stepped on a trapdoor and fell to your death')
        if num1 == 1:
            print('You were suspected as a spy and executed')
        if num1 == 2:
            print("\nYou didn't call the king", '"majesty"', 'so you were killed')
        exit()

def treasure(location, max=int):  # location gives a different string output depending on the room, and the max gives a different probability of finding treasure based off the current room.
    time.sleep(0.5)
    print('You check the room for treasure...')
    time.sleep(2)
    num = random.randint(0, max)  # random integer from 0 to max
    if num == 0:
        print(f"You don't notice it at first but after examining the room throughly, {location}. \n \n Congrats!! \n You have beat the game! ") 
        exit()
    else:
        print('Sadly there is nothing to be found')

def ThroneRoom():  # Script for the Throne Room
    print('Entering Throne Room....\n You see giant arches. There is a long red carpet through the middle of the room, leading to a giant throne made of silver and gold')  # Entry Script
    death()  # Death function
    treasure('You look in the unlikely place of behind the door and find the hidden treasure!', 30)  # treasure function with the script, then the probability of it happening
    time.sleep(1)  # program sleeps for 1 second to make the script not output all at once
    print('Which room would you like to go in now? (Storage, Dining Hall, Upstairs, Exit)')
def Storage():  # Script for the Storage room
    print('Entering Storage Room....\n You see tons of barrels and boxes. They are filled with all sorts of materials, food, and weapons')
    death()
    treasure('You search every inch of the room, but then you notice a lose cieling tile. You move it away and find the hidden treasure!', 10)
    time.sleep(1)
    print('Which room would you like to go in now? (Throne Room, Kitchen, Dungeon)')
def Dungeon():  # Script for the Dunegeon room
    print('Entering the Dungeon....\n You go down the dark creepy staircase in a hallway filled with chains and bars going into each cell')
    death()
    treasure('You quietly look around the dungeon, until you notice a slight shine underneath a stack of hay. You quietly walk past the prisoner and find the hidden treasure!', 100)
    time.sleep(1)
    print('The only place to go now is back where you came, so you walk back up to the storage room')
    time.sleep(1)
def Kitchen():  # Script for the Kitchen 
    print('You walk into a big kitchen with tons of pots, pands, overs, grills, and more. The type of kitchen in a 5 star restaurant.')
    death()
    treasure('You look in the fridge, and dig out all the food in it. Then you find it, the hidden treasure!', 20)
    time.sleep(1)
    print('Which room would you like to go in now? (Storage, Dining Hall, Exit)')
def DiningHall():  # Script for the dining hall
    print('Entering the dining hall....\n You see a big dining table with tons of extravagant decorations and a chandelier hanging over. There are plates, glasses, and silverware neatly placed on the table.')
    death()
    treasure('You are eating your dinner when notice unusual shine from a particular spot in the chandelier. You wait until everyone has left to stack up chairs to look inside and find the hidden treasure!', 50)
    time.sleep(1)
    print('Which room would you like to go in now? (Kitchen, Throne Room, Exit)')
def Upstairs(num):  # Script for the Upstairs Hallway
    if num == 0:
        print('Entering Upstairs Hallway....\n You walk up the spiral staircase into a hallway with many rooms')
    if num == 1:
        print('Entering Upstairs Hallway...')
    death()
    treasure('For some reason there is a chest in the middle of the hallway so you look inside. You found the hidden treasure?!', 200)
    time.sleep(1)
    print('Which room would you like to go in now? (Master Bedroom, Guest Bedroom, Bathroom, Downstairs)')
def MasterBedroom():  # Script for the Master Bedroom
    print('Entering Master Bedroom...\n You see a double king size bed, with tons of decorations, extravagant clothes, and more.')
    death()
    treasure('You are creeping around and hear a different noise coming from the floorboard you stepped on. You take it out, and find the hidden treasure!', 7)
    time.sleep(1)
    print('Which room would you like to go in now? (Hallway, Bathroom)')
def GuestBedroom():  # Script for the Guest Bedroom
    print('You walk into a decent sized room with a king sized bed, and many decorations')
    death()
    treasure('The previous guest seems to have found the treasure before you but left it on the bed?! You found the hidden treasure!!', 250)
    time.sleep(1)
    print('You get bored, and walk back into the hallway')
    time.sleep(1)
def Bathroom():  # Script for the Bathroom
    print('You walk into the bathroom covered in marble with nice looking bathtube and shower')
    death()
    treasure('You notice a lose brick in the bathroom, so you start hammering the wall to break through it. It reveals a hidden compartment, and you find the hidden treasure!', 50)
    time.sleep(1)
    print('Which room would you like to go in now? (Master Bedroom, Hallway)')

def WrongOption(choice, room1, room2=None, room3=None, room4=None, room5=None):  # Takes 1-5 rooms as options, and puts them into a list
    List = [room1, room2, room3, room4, room5]
    choices = []
    for n in List:  # Filters out all of the None types in the List
        if n is not None:
            choices.append(n)
    print_options = ', '.join(str(i) for i in choices)  # Creates a string with all of the rooms
    while choice.lower() not in choices:  
        choice = input(f'That is not an option! Options: ({print_options}) \n')  # A while loop to keep asking for another option if one of the listed options is not inputted
    main(choice)

def main(input1):
    if input1.lower() == 'throne room' or input1.lower() == 'downstairs':  # If input is throne room or downstairs (since it how you get room the upstairs hallway), 
        ThroneRoom()  # plays the script for the throne room
        choice = input('')
        WrongOption(choice, "storage", "dining hall", "upstairs", "exit")  # Rooms accessible from the throne room
    if input1.lower() == 'exit':  # if exit is inputed then it exits the program
        print('Exiting Castle....')
        exit()
    if input1.lower() == 'storage':  
        Storage()
        choice = input('')
        WrongOption(choice, "throne room", "kitchen", "dungeon", "exit")  
    if input1.lower() == 'kitchen':
        Kitchen()
        choice = input('')
        WrongOption(choice, "storage", "dining hall", "exit") 
    if input1.lower() == 'dungeon':
        Dungeon()
        time.sleep(3)  # stops program for 3 seconds to make the script flow better
        input1 = 'storage'  # Since the only way to access the dungeon is from the storage, the only way to go, is back up to the storage, so there's no need to ask which room to go to next. 
        main(input1)
    if input1.lower() == 'dining hall':  
        DiningHall()
        choice = input('')
        WrongOption(choice, "kitchen", "throne room", "exit") 
    if input1.lower() == 'upstairs':  
        Upstairs(0)
        choice = input('')
        WrongOption(choice, "master bedroom","bathroom","guest bedroom","downstairs","exit")  
    if input1.lower() == 'hallway':
        Upstairs(1)
        choice = input('')
        WrongOption(choice, "master bedroom","bathroom","guest bedroom","downstairs","exit")
    if input1.lower() == 'master bedroom':  
        MasterBedroom()
        choice = input('')
        WrongOption(choice, "bathroom","hallway","exit")  
    if input1.lower() == 'guest bedroom':  
        GuestBedroom()
        time.sleep(3)
        input1 = 'hallway'
        main(input1)
    if input1.lower() == 'bathroom':  
        Bathroom()
        choice = input('')
        WrongOption(choice, "hallway","master bedroom","exit")  


WrongOption(entry, "throne room", "storage", "dining Hall", "kitchen", "exit")  # Checks the first input for a correct option
main(entry)

