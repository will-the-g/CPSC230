
user_input = input('Enter a number:')
try:
    # code to run that might throw an error
    user_input = int(user_input)
    print(user_input * 100)
except:
    # code runs if an error happened in the try
    print('You did not enter a real number')
else:
    # code runs if there is no error in the try
    print('Thank you for following directions')
finally:
    # code runs either way
    print('Thank you and goodbye')
