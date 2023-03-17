# Will Gatlin, CPSC 230
# Imports
from itertools import permutations
import random
# List of halloween words
words = ['pumpkin', 'skull','corn', 'ghost', 'scary','zombie','witch','spider','mask','bat','broom', 'fang', 'candy','trick','treat','clown','horror','blood','costume','cat']
def main(points):
    num = random.randint(1, len(words))  # generates a random number to pick between all of the halloween words
    all_permutations = list(permutations(words[num - 1]))  # generates all the permutations of the word picked
    for perms in range(len(all_permutations)): # loops through the list of permutations
        all_permutations[perms] = ''.join(all_permutations[perms][perm] for perm in range(len(all_permutations[perms]))) # puts each permutation together from a list to a string
    hint = random.randint(1, len(all_permutations))  # picks which permutation to give to the user
    guess = input(f'Guess what the word is. ({all_permutations[hint]}): ')
    if guess == 'exit':  # if the guess is "exit", it exits the program
        exit()
    wrong = 0
    answer = True  # Intializes the variable
    while guess != all_permutations[0]: # while loop until the correct guess it given. (correct guess is the first permutation in the list)
        wrong += 1
        if wrong == 3:
            print(f'You have guessed wrong 3 times, the answer is {all_permutations[0]}')
            answer = False
            break
        if guess == 'exit':
            exit() 
        print('Not quite, please geuss again')
        guess = input(f'Guess what the word is. ({all_permutations[hint]}): ')  
    if answer != False:
        points += 1
        print(f'You have guessed correctly and gained 1 point. You now have {points} points!')
    main(points)  # restarts the program after a correct guess while keeping the total amount of points
main(0) # intitalized program with 0 points