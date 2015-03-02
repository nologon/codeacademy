shopping_list = ["banana", "pear", "apple"]
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
    total_price = 0
    for item in food:
        in_stock = stock[item] > 0
        if in_stock == True:
            total_price = total_price+ + prices[item]
    print total_price

def compute_bill(foods):
    # for item in foods:
    #     # print item
    #     current_stock = stock[item]
    #     # print "We have %s %s in stock" % (current_stock,item)
    #     stocked = stock[item]
    #     if stocked > 0:
    #         stocked = stock[item] -1
    #         # print stocked
    total = 0
    for item in foods:
        in_stock = stock[item] > 0
        if in_stock == True:
            total_price = total  + prices[item]
        return total

        # instock = 0
        # instock = stock.get(item)
        # print instock
        # if stock.get(item) > 0:
        #     print stock.get(item)
        # return stock
    #     # print prices[item]
    #         total = total + prices.get(item)
    # return total
    # # print total
print compute_bill(shopping_list)
