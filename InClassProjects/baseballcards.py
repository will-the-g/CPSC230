
def ebay_price_grab():
    price = 0
    # uses data scraping to grab the price of a card
    return price
def ebay():
        pricing = []
        price = ebay_price_grab()
        # will run the ebay_price_grab function multiple times to see multiple prices the card sold at, then appends it to the list
        pricing.append(price)
        return pricing


class card:
    def __init__(self, name=str, year=int, brand=str, code=str):
        self.name = name
        self.year = year
        self.brand = brand
        self.code = code
        self.price = 0

    def __str__(self) -> str:
        return f"The Card is {self.name} from {self.year} {self.brand} with the code {self.code}"
    def get_price(self):
        print('Now looking up price....')
        prices = ebay()
        # calculates the prices using advanced math formulas that gives the average price, discounting outliers, calculating accuracy based on image matching etc.
        # if there is enough data on the card. It will output as "final_price" variable below
        final_price = 0
        self.price = final_price
    def sell(self):
        pass
    def save(self):
        pass

# Using OpenCV and image identification to grab the details of the card
card('Fernado Tatis Jr.', 2019, 'Topps', '203')



        
        
