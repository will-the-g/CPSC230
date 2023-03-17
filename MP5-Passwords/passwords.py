# Will Gatlin,  CPSC 230 session 06

passwords = {}  # Intializes passwords dictionary
# Encryption and Decryption Dictionaries
encryption = {'a':'g','b':'p','c':'m','d':'b','e':'q','f':'z','g':'u','h':'a','i':'r','j':'c','k':'h','l':'w','m':'o','n':'x','o':'f','p':'k','q':'v','r':'d','s':'j','t':'l','u':'y','v':'e','w':'s','x':'t','y':'i','z':'n','1':'7','2':'4','3':'5','4':'0','5':'1','6':'9','7':'8','8':'2','9':'3','0':'6'}
decryption = {'g': 'a', 'p': 'b', 'm': 'c', 'b': 'd', 'q': 'e', 'z': 'f', 'u': 'g', 'a': 'h', 'r': 'i', 'c': 'j', 'h': 'k', 'w': 'l', 'o': 'm', 'x': 'n', 'f': 'o', 'k': 'p', 'v': 'q', 'd': 'r', 'j': 's', 'l': 't', 'y': 'u', 'e': 'v', 's': 'w', 't': 'x', 'i': 'y', 'n': 'z', '7': '1', '4': '2', '5': '3', '0': '4', '1': '5', '9': '6', '8': '7', '2': '8', '3': '9', '6': '0'}
option = input('What would you like to do? (Add, View, Update, Exit)\n')
while option != 'exit': # while the option is not exit, it keeps asking the user for input
    if option.lower() == 'add':  # adds a service with a username and password
        service = input('Which service are you adding login information for?').lower()
        username = input('What is the username?').lower()
        password = input('What is the password?').lower()
        encrypted_pass = ''.join(encryption[character] for character in password) # loops through each character and turns each into the encrypted character and converts it into a string
        encrypted_user = ''.join(encryption[character] for character in username)
        passwords[service] = {'Username': encrypted_user, 'password': encrypted_pass} # stores the username and password in a dictionary under the service name
        print(f'Username and Password for {service} added')
    if option.lower() == 'view':  # view the username and password for a service
        service = input('Input the service you would like to view the password for').lower() 
        if service not in passwords.keys():  # checks if the service is in the dictionary
            print('service not detected')
        else:
            decrypted_user = ''.join(decryption[character] for character in passwords[service]['Username'])  # decrypts the username and password so it can be printed
            decrypted_pass = ''.join(decryption[character] for character in passwords[service]['password'])
            print('Service: ', service, '\nUsername: ', decrypted_user, '\nPassword: ', decrypted_pass)
    if option.lower() == 'update':  # updates the username and password for a service
        service = input('Which service would you like to update').lower()
        if service not in passwords.keys():
            print('service not detected')  # Checks if the service is in the dictionary
        else:
            username = input('What would you like to change your username to?')  # asks what the user would like to change to username and password to
            password = input('What would you like to change your password to?')
            encrypted_pass = ''.join(encryption[character] for character in password)  # encrypts the username and password
            encrypted_user = ''.join(encryption[character] for character in username)
            passwords[service]['Username'] = encrypted_user # updates the username and password in the dictionary
            passwords[service]['password'] = encrypted_pass 
            print('Username and Password updated')
    option = input('What would you like to do? (Add, View, Update, Exit)\n')  # asks the user for another input then loops back again if the option is not exit.
print('Exiting program......')
