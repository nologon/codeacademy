__author__ = 'thijn'
#
# Write a Python expression that combines the string "Joe Warren is 52 years old."
# from the string "Joe Warren" and the number 52 and then prints the result
# (Hint: Use the function str to convert the number into a string.)

# Compute the statement about a person's name and age, given the person's name and age.
###################################################
# Name and age formula
# Student should enter statement on the next line.
###################################################
# Expected output
# Student should look at the following comments and compare to printed output.
#Joe Warren is 52 years old.

name = "Joe Warren"
age = 52
age = str(age)
print "%s name is %s years old." % (name, age)

