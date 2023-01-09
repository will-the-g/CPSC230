# Will Gatlin CPSC 230-06
# creates variable for the text file
filename = 'shows&movies.txt'
# Creates the class 'show' which has 4 attributes, and 1 function to save the show/movie to the text file.
class show():  
    def __init__(self, name=str, rating=float, start=str, finish=str):
        self.name = name
        self.rating = rating
        self.start = start
        self.finish = finish
    def save(self):
        file = open(filename, 'a')
        file.write(f'{self.name}:{self.rating}:{self.start}:{self.finish}\n')
        file.close()
# Function to find show in the text file    
def findshow(show1, returnline=False):  # show1 is the name of the show, returnline is if I want to return the line of the file the show was found on
    file = open(filename, 'r')
    lines = file.readlines() # grabs content of the file
    file.close()
    count = 0
    for i in range(len(lines)):
        content = lines[i].split(':')  # loops through every line and splits the lines into list so the name of the show/movie is the 0th element of the list
        if show1 == content[0]:  # if the show is found it returns a set with True, the content, and the line(if specified)
            if returnline is True:
                return (True, content, i)
            else:
                return (True, content)
        else:
            count += 1
    if count == len(lines):  # if the count reaches the number of lines, the show hasn't been found, and it returns False. (None for it to be a set)
        return (False, None)
# Checks the format of the Start or Finish date that the user inputted
def formatcheck(input1):
    # tries to see if the character in position 1,2,3,4,6,7,9,10 are numbers, if not it returns False
    try: 
        for i in range(4):
            number = int(input1[i])
        for i in range(5,7):
            number = int(input1[i])
        for i in range(8,10):
            number = int(input1[i])
    except:
        return False
    else:
        if input1[4] != '-' or input1[7] != '-':  # checks if it has the dash in the right spot
            return False
        elif len(input1) > 10:  # checks if the input is less than 11 characters
            return False
        else:
            return True  # returns True if it passes all the conditions

# Checks if the rating entered is a number between 0 and 10
def ratingcheck(rating):
    passable = False
    while passable is False:
        try:
            rating = float(rating)
        except:
            print('Please enter a number')
            passable = False
            rating = input('What is the rating of the show? Please enter out of 10\n')
        else:
            if rating < 0 or rating > 10:
                print('Please enter a number 0 through 10')
                rating = input('What is the rating of the show? Please enter out of 10\n')
            else:
                passable = True  
    return rating
# main function
def main():
    option = input('Would you like to add, view, change, or delete a show/movie to your list?\n')
    while option != 'exit':
        # "add" allows the user to add a show/movie to their list
        if option.lower() == 'add':
            name = input('What is the name of the show/movie that you are adding?\n')
            found = findshow(name) # finds the show in the file
            if found[0] is True:
                print('This show is already on your list')  # if it's already in the file it prints and restarts, else it continues
            else:
                rating = input('What is the rating of the show? Please enter out of 10\n')
                ratingcheck(rating)  # checks if the rating is a number between 0 and 10
                start = input("What date did you start watching? Please enter in the form of YYYY-MM-DD. (Enter skip if you don't want to put anything)\n")
                if start.lower() == 'skip':  # if the user puts skip, it makes the start date default to YYYY-MM-DD
                    start = 'YYYY-MMM-DD'
                    format = True
                else:
                    format = formatcheck(start)  # Checks the format of the date the user inputted
                while format is False:  # Keeps asking until the put the right format or put skip
                    print('You have entered the date in the wrong format. Please use "YYYY-MM-DD" format')
                    start = input("What date did you start watching? Please enter in the form of YYYY-MM-DD. (Enter skip if you don't want to put anything)\n")
                    if start.lower() == 'skip':
                        start = 'YYYY-MM-DD'
                        format = True
                    else:
                        format = formatcheck(start)
                # same as the start date code
                finish = input("What date did you finish watching Please enter in the form of YYYY-MM-DD.(Enter skip if you don't want to put anything)\n")
                if finish.lower() == 'skip':
                    finish = 'YYYY-MM-DD'
                    format = True
                else:
                    format = formatcheck(finish)
                while format is False:
                    print('You have entered the date in the wrong format. Please use "YYYY-MM-DD" format')
                    finish = input("What date did you finish watching Please enter in the form of YYYY-MM-DD.(Enter skip if you don't want to put anything)\n")
                    if finish.lower() == 'skip':
                        finish = 'YYYY-MM-DD'
                        format = True
                    else:
                        format = formatcheck(finish)
                show1 = show(name, rating, start, finish) # creates a object out of the show and saves it to the text file
                show1.save()
                print(f'{name} added to your list')
            option = input('Would you like to add, view, change, or delete a show/movie to your list?\n')
        # "view" displays the information of a show on the user's list or their list entirely
        elif option.lower() == 'view':
            view_choice = input('Would you like to view your whole list or the specific information of a show/movie? (Type "list" or "show/movie")\n')
            if view_choice.lower() == 'show/movie':
                show1 = input('Which show/movie would you like to view?\n')
                found = findshow(show1)
                if found[0] is True:  # prints out show information if it was found
                    print(f'------------------------------\nName: {found[1][0]}\nRating: {found[1][1]} out of 10\nStart: {found[1][2]}\nFinish: {found[1][3][:-1]}\n------------------------------')
                else:
                    print('The show/movie you entered is not on your list!')
            # prints out the name of every show on the user's list
            elif view_choice.lower() == 'list':
                file = open(filename, 'r')
                lines = file.readlines() # grabs the information from the text file
                show_list = []
                for line in lines:
                    show2 = line.split(':')  # grabs the name of every show
                    show_list.append(show2[0])  # appends the names to a list
                for shows in range(len(show_list) - 1):
                    print(show_list[shows], end=', ')  # prints out the list in a user friendly output
                print(show_list[-1])                   
            option = input('Would you like to add, view, change, or delete a show/movie to your list?\n') 
        # changes allows the user to change information of a show that is already on the user's list
        elif option.lower() == 'change':
            show1 = input('Which show/movie would you like to change?\n')
            found = findshow(show1, True)  # finds show, and grabs the line of the text file the show is on
            if found[0] is True:
                change_choice = input(f'{found[1][0]} was found. What would you like to change? (Rating or Watch Dates)\n')
                # changes the rating of the show
                if change_choice.lower() == 'rating':
                    rating = input('What would you like to change the rating to?\n')
                    rating = ratingcheck(rating)
                    file = open(filename, 'r')
                    lines = file.readlines()  # opens the file to read it
                    file.close()
                    lines[found[2]] = f'{found[1][0]}:{rating}:{found[1][2]}:{found[1][3]}'  # replaces the old line to the new line with the changed information
                    file = open(filename, 'w')  # writes all the information with the changed lines back into the file, replacing the old information
                    file.writelines(lines)
                    file.close()
                    print(f'{show1} Updated!') 
                # same process with ratings, just with watch dates
                elif change_choice.lower() == 'watch dates':
                    start = input('What would you like to change the start date to? (Use "YYYY-MM-DD" format)\n')
                    if start.lower() == 'skip':
                        start = 'YYYY-MMM-DD'
                        format = True
                    else:
                        format = formatcheck(start)
                    while format is False:
                        print('You have entered the date in the wrong format. Please use "YYYY-MM-DD" format')
                        start = input("What date did you start watching? Please enter in the form of YYYY-MM-DD. (Enter skip if you don't want to put anything)\n")
                        if start.lower() == 'skip':
                            start = 'YYYY-MM-DD'
                            format = True
                        else:
                            format = formatcheck(start)
                    finish = input('What would you like to change the finish date to? (Use "YYYY-MM-DD" format)\n')
                    if finish.lower() == 'skip':
                        finish = 'YYYY-MM-DD'
                        format = True
                    else:
                        format = formatcheck(finish)
                    while format is False:
                        print('You have entered the date in the wrong format. Please use "YYYY-MM-DD" format')
                        finish = input("What date did you finish watching Please enter in the form of YYYY-MM-DD.(Enter skip if you don't want to put anything)\n")
                        if finish.lower() == 'skip':
                            finish = 'YYYY-MM-DD'
                            format = True
                        else:
                            format = formatcheck(finish)
                    file = open(filename, 'r')
                    lines = file.readlines()
                    file.close()
                    lines[found[2]] = f'{found[1][0]}:{found[1][1]}:{start}:{finish}\n'
                    file = open(filename, 'w')
                    file.writelines(lines)
                    file.close()
                    print(f'{show1} Updated!') 
                else:
                    print('That is not a choice!')  
                
            else:
                print(f'The {show1} you entered is not on your list!')
            option = input('Would you like to add, view, change, or delete a show/movie to your list?\n')
        # deletes a show on the user's list
        elif option == 'delete':
            show1 = input('Which show would you like to delete?\n')
            found = findshow(show1, True)
            if found[0] is True:  # same process above with the change code, just replacing the line with nothing so it will delete
                file = open(filename, 'r')
                lines = file.readlines()
                file.close()
                lines[found[2]] = ''
                file = open(filename, 'w')
                file.writelines(lines)
                file.close()
                print(f'{show1} was deleted!')
            else:
                print(f'{show1} is not on your list!')
            option = input('Would you like to add, view, change, or delete a show/movie to your list?\n')
        else:
            option = input('That is not an option!\nWould you like to add, view, change, or delete a show/movie to your list?\n')


main()

