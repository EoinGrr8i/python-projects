shopping_list = ["banana", "orange", "apple", "pear"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!

        
def compute_bill(food):
    total = 0
    for n in food:
        if stock[n] >0:
            total += prices[n]
            stock[n] -= 1
        else:
            print "not in"
    return total
