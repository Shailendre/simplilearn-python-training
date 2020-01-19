# exception handling
# equal to try and catch

# syntax similar to java try and catch
"""
    try {}
    catch ( <exception class1> e1 ) {}
    catch ( <exceptiom class2> e2) {}
"""

'''
try:
    print ("6" + 5)
except Exception as e:
    # raise => java 'throw e'
    # raise
    print (str(e)) # str(excetion): => e.getMessage()

'''

# Exceptiom handling
# multiple catches/except
# if none of them is matched with error type
# the general exceptiom is followed

try:
    print (5 + x)
except TypeError as t:
    print (str(t))
except NameError as n:
    print (str(n))
except Exceptiom as e:
    print (str(e))
