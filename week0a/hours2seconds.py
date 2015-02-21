__author__ = 'thijn'
# Compute the number of seconds in a given number of hours, minutes, and seconds.

###################################################
# Hours, minutes, and seconds to seconds conversion formula
# Student should enter statement on the next line.
###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#26497
# Write a Python statement that calculates and prints the number of
# seconds in 7 hours, 21 minutes and 37 seconds.
hours = 7
minutes = 21
seconds =37

hrs = 3600
min = 60

total_secs = hours * hrs + minutes * min + seconds
print "there are %s seconds total" % total_secs