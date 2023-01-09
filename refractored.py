# Will Gatlin,  CPSC 230 session 06

passwords = {}  # Intializes passwords dictionary
# Encryption and Decryption Dictionaries
encryption = {'a':'g','b':'p','c':'m','d':'b','e':'q','f':'z','g':'u','h':'a','i':'r','j':'c','k':'h','l':'w','m':'o','n':'x','o':'f','p':'k','q':'v','r':'d','s':'j','t':'l','u':'y','v':'e','w':'s','x':'t','y':'i','z':'n','1':'7','2':'4','3':'5','4':'0','5':'1','6':'9','7':'8','8':'2','9':'3','0':'6'}
decryption = {'g': 'a', 'p': 'b', 'm': 'c', 'b': 'd', 'q': 'e', 'z': 'f', 'u': 'g', 'a': 'h', 'r': 'i', 'c': 'j', 'h': 'k', 'w': 'l', 'o': 'm', 'x': 'n', 'f': 'o', 'k': 'p', 'v': 'q', 'd': 'r', 'j': 's', 'l': 't', 'y': 'u', 'e': 'v', 's': 'w', 't': 'x', 'i': 'y', 'n': 'z', '7': '1', '4': '2', '5': '3', '0': '4', '1': '5', '9': '6', '8': '7', '2': '8', '3': '9', '6': '0'}


# Function to check if they all the characters in the username and password are in the alphabet or a number.
def alphanumeric(input1, type1=str):  # Input1 is the username/password that the function is checking, and the type1 tells whether it is a username or password.
    alpha_numeric = False
    while alpha_numeric is False:  # Keeps check the input and asking for a new one until an input with only alpha-numeric characters is given.
        count = 0
        for character in input1:
            if character not in encryption.keys():  #Checks if the characters are in the alphabet or a number. If not it adds 1 to the count
                count += 1
        if count > 0:  # if the count is greater than 1, then the username/password contains a non alpha-numeric character, and the program asks the user to enter another user/pass.
            input1 = input(f'{type1} contains a character that is not alpha-numeric. Please enter another {type1}\n')
            alpha_numeric = False
        else:
            alpha_numeric = True
                    
    return input1

# Function to check if the service inputted is in the dictionary of services.    
def service_check(option): 
    service = input(f'Which service would you like to {option}? ({", ".join(s for s in passwords.keys())}) \n').lower()
    while service not in passwords:
        service = input(f'Which service would you like to {option}? ({", ".join(s for s in passwords.keys())}) \n ').lower() # keeps asking until a service in the list of passwords is given or the user exits.
        if service == 'exit': # breaks loop if the user enters exit
            break  
    if service == 'exit': # returns the variable as "exit" to exit the option wherever the function is used.
        return 'exit'
    else:
        return service


option = input('What would you like to do? (Add, View, Update, Exit)\n')
while option != 'exit': # while the option is not exit, it keeps asking the user for input


    if option.lower() == 'add':  # adds a service with a username and password
        service = input('Which service are you adding login information for?').lower()
        username = input('What is the username?').lower()
        username = alphanumeric(username, "username")
        password = input('What is the password?').lower()
        password = alphanumeric(password, "password")
        encrypted_pass = ''.join(encryption[character] for character in password) # loops through each character and turns each into the encrypted character and converts it into a string
        encrypted_user = ''.join(encryption[character] for character in username)
        passwords[service] = {'Username': encrypted_user, 'password': encrypted_pass} # stores the username and password in a dictionary under the service name
        print(f'Username and Password for {service} added')


    if option.lower() == 'view':  # view the username and password for a service
        if len(passwords) > 0:  #Checks if a service has been added
            service = service_check('view')
            if service != 'exit':
                decrypted_user = ''.join(decryption[character] for character in passwords[service]['Username'])  # decrypts the username and password so it can be printed
                decrypted_pass = ''.join(decryption[character] for character in passwords[service]['password'])
                print('Service: ', service, '\nUsername: ', decrypted_user, '\nPassword: ', decrypted_pass)
        else:
            print('No services have been added yet')



    if option.lower() == 'update':  # updates the username and password for a service
        if len(passwords) > 0:  # Checks if a service has been added
            service = service_check('update')
            if service != 'exit':
                username = input('What would you like to change your username to?')  # asks what the user would like to change to username and password to
                username = alphanumeric(username, 'username')
                password = input('What would you like to change your password to?')
                password = alphanumeric(password, 'password')
                encrypted_pass = ''.join(encryption[character] for character in password)  # encrypts the username and password
                encrypted_user = ''.join(encryption[character] for character in username)
                passwords[service]['Username'] = encrypted_user # updates the username and password in the dictionary
                passwords[service]['password'] = encrypted_pass 
                print('Username and Password updated')
        else:
            print('No services have been added yet')
        

    option = input('What would you like to do? (Add, View, Update, Exit)\n')  # asks the user for another input then loops back again if the option is not exit.
print('Exiting program......')
