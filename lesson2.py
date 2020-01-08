# lesson 2

# variable;
a = 10
print(a);

# while loop
while a < 100:
    a *= 2
    print(a)

# for loop

list = [1, 2, 3, 5]
for a in list:
    print(a)

for a in range(1,11):  # last is exlusive
    print(a)

# if construct
a = 9
b = 0
c = 1
if a > 10 or b > 0:
    print("if a is", a)
elif a < 10 and b == 0:
    print("elif a is", a)
else: print("else is", a)
