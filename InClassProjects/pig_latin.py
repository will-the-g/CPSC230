

vowels = ['a','e','i','o','u']
def word_to_pig(lines=str):
    if '\n' in word:
        if word[0] in vowels:
            return f'{word[:-1]}yay\n'
        else:
            return f'{word[1:-1]}{word[0]}ay\n'
    else:
        if word[0] in vowels:
            return f'{word}yay'
        else:
             return f'{word[1:]}{word[0]}ay'



file = open("piglatin.txt", "r")
for lines in file:
    words = lines.split(' ')
    for word in words:
        print(word_to_pig(word), end=' ')
