'''
Zach Elias
Regrex Homework 4/2/18
'''
##### Problem #####
##### CNS-380/597 - Ryan Haley####


#Write a regular expression to fit the following:

#1 Phone number in the format of
#  xxx-xxx-xxxx
'''
^\d{3}-\d{3}-\d{4}$
'''

#2 Phone number in the format of
#  (xxx) xxx-xxx
'''
^\(\d{3}\)\s\d{3}-\d{4}$
'''



#3 Phone number in the format of
#  +x xxx.xxx.xxxx
'''
^\+\d{1}\s\d{3}\.\d{3}\.\d{4}$
'''



#4 SSN in the format of
#  xxx-xx-xxxx or xxxxxxxxx
'''
^\d{3}\-?\d{2}\-?\d{4}$
'''



