def test1():
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

def test2():
    fruits = ['apple','banana','orang','pear']
    selection = input('enter the # of the fruit you want:')
    try: 
        selection = int(selection)
        selected_fruit = fruits[selection]
        print('You selected' + selected_fruit)
    except ValueError:
        print('You did not enter a number')
    except IndexError:
        print('You entered a number but it was not a valid fruit')
    except:
        print('Something else went wrong')
