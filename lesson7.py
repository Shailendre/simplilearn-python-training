from statistics import mean

# define users map in tghe system
# in mem system
users       = {"admin":"admin", "user1":"useer1"}
students    = {"soniya": [77, 78 , 98], "gunjan" : [55, 65, 62], "sadaf" : [45, 52, 42]}

# exception handling in  number input
def floatGradeInput():
    try:
        return float(input("add grade: "))
    except Exception as e:
        print(str(e))
        # try again to enter valid number
        floatGradeInput()

# helper function
def getStudentsList():
    ll = [];
    for u in students:
        ll.append(u)
    return ll

# 1 action
def enterGrades():
    name = input("enter student name: ")
    if name in students:
        grade = floatGradeInput()
        print("adding grade ...")
        students[name].append(grade)
        # print name, new numbers list
        print(name, students[name])
    else:
        print(name, "not found in system")


# 2 choice
def removeStudent():
    name = input("enter student name to be removed from system: ")
    if name in students:
        print("removing", name, "...")
        del students[name]
        print("refreshing students list, ", getStudentsList())
    else:
        print(name, "not present in system.")

# 3 choice
def getStudentsAvg():
    name = input("enter name of the student to get his/her avg: ")
    if name in students:
        marksll = students[name]
        print(name, marksll)
        # round (float, number of decimal places) -> returns float decimal
        print(name + "'s", "avg. marks:", round(mean(marksll), 2))
    else:
        print(name, "not present in system!")


# login function
def login():
    login  = input("enter your username: ")
    passwd = input("enter your password: ")
    # 'in' in map returns list of keys
    if login in users:
        if users[login] == passwd:
            print("welcome,", login)
            return True
        else:
            print("invalid password for,", login, ". exiting ...")
            return False
            # try try & try again!
            # login()
    else:
        print("access denined!!")
        return False


# no action logoutq
def logout():
    print("bye!")

# take action input, once access granted to system
def action():
    # for printing string in multiple lines, use """
    print("""

    Welcome to Central Student Grades System:

    [1] - enter grades
    [2] - remove a student
    [3] - student average grades
    [4] - logout

    """)
    # the variable here cannot be "input",
    # looks like method names are also reserved??!
    choice = input("Enter your choice: ")
    # choices
    # wtf, py has no switch cases
    if choice == '1':
        enterGrades()
    elif choice == '2':
        removeStudent()
    elif choice == '3':
        getStudentsAvg()
    elif choice == '4':
        logout()
        return
    else:
        # take the actiojn again
        print("invalid choice, try again!")
        action()

    # call this driver actoin method, until logout
    action()

# driver function
def main():

    # login to start
    print("""welcome to central grade system. login to proceed""")
    if login():
        action()

main()
