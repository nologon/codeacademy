__author__ = 'thijn'
# Given p dollars, the future value of this money when compounded yearly at a
# rate of r percent interest for y years is p(1+0.01r)y.
# Write a Python statement that calculates and prints the value of 1000 dollars
# compounded at 7 percent interest for 10 years.

# Compute the future value of a given present value, annual rate, and number of years.
###################################################
# Future value formula
# Student should enter statement on the next line.
###################################################
# Expected output
# Student should look at the following comments and compare to printed output.
# 1967.15135729

p = 1000
years = 7
# percentage = (p / 100) * 7
p = float(p)
for i in range(1,11):
    percentage = (p / 100) * 7
    p = p + percentage
print "Total value: %s" % p





