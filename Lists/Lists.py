my_list = [1,2,3]
my_list = ['STRING',100,23.2]
print(len(my_list))

mylist = ['one','two','three']
print(mylist[0])
print(mylist[1:])

anotherlist = ['four','five']

new_list = mylist + anotherlist
print(new_list)

new_list.append('six')
print(new_list)
new_list.append('seven')
print(new_list)

print(new_list.pop())
print(new_list)

popped_item = new_list.pop()
print(popped_item)
print(new_list)

print(new_list.pop(0))
print(new_list)

new_list = ['a','e','x','b','c']
num_list = [4,1,8,3]
new_list.sort()
print(new_list)

my_sorted_list = new_list.sort()
print(type(my_sorted_list))

new_list.sort()
my_sorted_list = new_list
print(my_sorted_list)

num_list.reverse()
print(num_list)