__author__ = 'thijn'
prices = {
    'banana': 4,
    'apple': 2,
    'orange': 1.5,
    'pear': 3
}
stock = {
    'banana': 6,
    'apple': 0,
    'orange': 32,
    'pear': 15,
}
for key in stock:
    print key
    print "price: %s" % prices[key]
    print "stock: %s" % stock[key]
    print""

# once  = {'a': 1, 'b': 2}
# twice = {'a': 2, 'b': 4}
# for key in once:
#     print "Once: %s" % once[key]
#     print "Twice: %s" % twice[key]
