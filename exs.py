print('hello, world')

x = [1, 2,  5, 8, 13]

if 1 in x:
    print('1')
else:
    if 2 in x:
        print('2')
    else:
        print('other')

if 1 in x:
    print('1')
elif 2 in x:
    print('2')
else:
    print('other')

if 3 > 2:
    print('Its true')
else:
    print('False')

print()
print()


print()


print()

def hi(name):
        print('Hello, ' + name + '. How a u?')

girls = ['Natali', 'Ola', 'Reichel', 'Sveta']
for name in girls:
    hi(name)
    print('Next girl')
for i in range(1,6):
    print(i)
