# import

ll = [1,2,3]

# import, alias to class
# 1
# methods need to be referenced from dot operator
# like sql query alias
'''
import statistics as s
print(s.mean(ll))
'''

# 2
# way to import functions from module
# more like static imports from class in java
'''
from statistics import mean
print(mean(ll))
'''

# 3
# shorter way, importing methods as alias, not class
'''
from statistics import mean as m
print(m(ll))
'''

# 4
# import all methods from the class
# same as static imports in java
'''
from statistics import * # => from statistics import mean,median,mode, <all methods>
print(mean(ll))
'''
