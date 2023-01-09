first_name = input('Enter the first name: ').lower()
second_name = input('Enter the second name: ').lower()
vowels = ['a', 'e', 'i', 'o', 'u']  # sets a list of vowels
for char in first_name[1:]:
    if char not in vowels:
        pos = first_name.index(char)  # Grabs the position of the first consonent
        break
first_letter = first_name[0].upper()  # makes the first letter uppercase
if second_name[0] in vowels:
    second_part = second_name  # if first letter is a vowel, then the second part is the entire name
else:
    second_part = second_name[1:]  # sets 2nd part to everything after the first consonent 
print(first_letter + first_name[1:(pos + 1)] + second_part)  # Adds the first letter of the first name, 2nd letter to first consonent of the 1st name, and the second part