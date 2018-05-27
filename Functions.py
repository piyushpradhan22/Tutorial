def func1(str):
    print("Hello " + str + "!.")
    return


func1("Piyush")


def nameage(name, age=35):
    print("Hello", name, "\b. You are", age, "years old.")
    return


nameage("Piyush")
nameage("Piyush", 26)
nameage(input("Enter your name "), input("Enter your age "))


def vartuple(arg1, *vartuple):
    print(arg1)
    for var in vartuple:
        print(var)
    return


vartuple(5, 2, 5, 8, 5, 6, 5)
vartuple(5)

sums = lambda num1, num2: num1 + num2
print(sums(50, 80))
print(sums(80, 90))


def returntest(arg1, arg2):
    return arg1 + arg2


print(returntest(50, 90))
# Local variable - Inside a function; Global variable - Outside a function
total = 0


def localglobal(arg1, arg2):
    global total;
    total = arg1 + arg2
    print(total)
    return


localglobal(20, 30)
print(total)
