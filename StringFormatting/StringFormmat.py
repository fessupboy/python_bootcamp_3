print('This is a string {}'.format('INSERTED'))
print('The {2} {1} {0}'.format('fox','brown','quick'))
print('The {0} {0} {0}'.format('fox','brown','quick'))
print('The {q} {b} {f}'.format(f='fox',b='brown',q='quick'))

result = 104.12345
print(result)
print("The result was {r:1.2f}".format(r=result))

# f strings
name = 'Jose'
print(f'Hello, his name is {name}')

name = 'Sam'
age = 3
print(f'{name} is {age} years old')