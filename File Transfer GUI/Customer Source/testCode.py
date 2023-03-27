

mySentence = 'loves the color'

color_list = ['red', 'blue', 'pink', 'teal', 'black']

def color_function(name):
    lst = []
    for i in color_list:
        msg = "{0} {1} {2}".format(name,mySentence,i)
        lst.append(msg)
    return lst


lst = color_function('jordy')
for i in lst:
    print(i)

def get_name():
    go = True
    while go:
        name = input('What is your name? ')
        if name == '':
            print('You need to provide your name')
        else:
            go = False
    lst = color_function(name)
    for i in lst:
        print(i)

get_name()

def my_function(name):
    print("My name is " + name)

my_function("Jordyn")

half_year = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']
for x in half_year:
    print(x)

o = half_year.count("apr")
print(o)

half_year.sort()
print(half_year)

x = lambda a, b, c: a * b - c
print(x(10, 1, 5))


fName = "Jordyn"
lName = "Lewis"
print(fName + " " + lName)

print("Hello {} {}, welcome to Python!".format(fName,lName))

txt = "The utilizes an align.... {:>8} ...to the right."
print(txt.format("-->"))

q = format(954569, '+')
print(q)

def getSum(num1, num2):
    answer = num1 + num2
    print("The answer is {}.".format(answer))

j = getSum(2, 4)
print(j)

myAdd = getSum
k = myAdd(2, 4)

print(k)

truth1 = True
truth2 = False
print("The truth is always {}.".format(truth2))

num1 = 3
num2 = 1
answer = "The answer is {}.".format(num1 + num2)
print(answer)
