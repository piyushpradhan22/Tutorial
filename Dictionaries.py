dict1 = {'Name': 'Piyush', 'Age': 32, 'Class': 'Engineer'}
dict1['State'] = 'Odisha'
print(dict1)
del dict1['Age']
print(dict1)
dict1.clear()
print(dict1)
dict2 = {'Name':'Piyush','Name': 'John'}
print(dict2)
print(dict2['Name'])
# Dictionary keys is not allowed with ['Key'] types
dict = {'Name': 'Zara', 'Age': 7};
print ("Equivalent String : %s" % str (dict))
print(type(dict2))
z=['Hello','Hi','GoodBye']
print(type(z))
dix={}
dix=dix.fromkeys(z,20)
print(dix)
dix2={'hello':222,'ji':502}
print(dix2['hello'])
print(dix2.get('jjjj','default'))
print(dix2.items())
print(dix2.setdefault('set','oOOOoo'))
print(dix2)
print(dix2.keys())