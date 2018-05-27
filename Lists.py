x = ["Mathematics", "physics", "chemistry", "IT", "English", "Odia"]
print(x[1:6])
x[2] = "CM"
print(x)
del x[2]
print(x)
x += [95, 80, 75, 80, 73, 88]
print(x * 2)
for a in x:
    print(a)
y = ['Hello', 'Hi', 'Good Morning', ['Helllllll', 'ShutUp']]
y.append("What's up")
print(y[3][1])
print(y)
y.extend("How are you")
print(y)
print(y.index('o'))
y.insert(2, 'Good eve')
print(y)
print(y.pop(2))
print(y)
# Tuples
print('--------------------------------------------')
Tp1=(20,20,30,'Hello')
Tp2=('abc')
print(Tp1)
print(Tp2)
print(Tp1*2)
print('Hello' in Tp1)
Tp3=5,6
print(Tp3)
