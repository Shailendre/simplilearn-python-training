# file
data = "some text"
# mode: w : write
# file is always new, existing data file will be overridden
file = open('lesson5.txt', 'w')
file.write(data)
# need to close to flush the buffer
file.close()


# mode: a: append mode
# file will be created new if not present, else will be appended
data2 = "\nmoredata"
file = open('lesson5.txt', 'a');
file.write(data2)
# close the buffer stream
file.close();


# read from file
data3 = open('lesson5.txt', 'r').read();
print(data3)

# split operation, using delimeter
# same method as java8 split using delimeter,
# returns list of lines
print(data3.split("\n"))


# readlines(), basically wrapper for split(\n)
# returns list of lines, with last "\n" character
print(open('lesson5.txt','r').readlines())
