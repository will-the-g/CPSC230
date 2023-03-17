def Q6():
    input1 = int(input('Enter a number'))
    for i in range(0, input1 + 1):  # loops through all the numbers from 1 to the number inputted
        remainder = i % 2  # gives the remainder of each number when divided by 2
        if remainder == 0:  # if remaineder is 0 then the number is even
            print(i, end=" ")  

def Q5():
    import random
    def main():
        input1 = input('Ask a question')
        num = random.randint(0,3)
        if num == 0:
            print('Yes')
            main()
        if num == 1:
            print('No')
            main()
        if num == 2:
            print('There is a good probability')
            main()
        if num == 3:
            print('Maybe')
            main()
        if input1 == 'exit':
            exit()
    main()

def Q4():
    import random
    num = random.randint(0,100)
    def main():
        input1 = int(input("I'm thinking of a number between 0 and 100."))
        if input1 == num:
            print('You are correct!')
        else:
            print('Please guess again')
            main()
    main()

def Q3():
    input1 = int(input('Enter a grade'))
    total = 0
    while input1 != -1:
        total += input1
        input1 = int(input('Enter another grade (to exit type: -1)'))
    print(total)

def Q2():
    input1 = input('Please enter a word')
    for char in input1[:-1]:
        print(char, end='-')
    print(input1[-1])
Q2()

def Q1():
