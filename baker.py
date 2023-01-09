# Name: Will Gatlin. CPSC 230
# Sources: https://www.allrecipes.com/recipe/6882/french-bread/
# https://www.allrecipes.com/recipes/1798/world-cuisine/european/italian/bread/
# https://www.norbertskitchen.com/farmers-bread-flour-water-time-yeast/
# https://www.allrecipes.com/recipes/349/bread/yeast-bread/sourdough-bread/
bread = input("Which bread would you like: Farmers, Sourdough, Italian, or French?")
grams = float(input('Please enter the weight in grams of flour you would like in your bread.'))
if grams <= 0:
    print(f'{grams} has to be greater than 0!')
    exit()
else:
    if bread.lower() == 'farmer':
        flour = grams
        yeast = grams * 0.02083
        water = grams * 0.5
        salt = grams * 0.04166
    elif bread.lower() == 'sourdough':
        flour = grams
        water = grams * 0.63451
        yeast = grams * 0.2538
        salt = grams * 0.0203
    elif bread.lower() == 'italian':
        flour = grams
        water = grams * 0.444
        salt = grams * 0.03125
        yeast = grams * 0.01041
    elif bread.lower() == 'french':
        flour = grams
        water = grams * 0.33333
        yeast = grams * 0.052
        salt = grams * 0.0052
    else:
        print(f' {bread} is not on the list of breads')
        exit()
    print(f'The recipe for {bread} bread \n ------------------------------- \n Flour: {flour:.2f}g \n Yeast: {yeast:.2f}g \n Water: {water:.2f}g \n Salt: {salt:.2f}g')
