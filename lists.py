alist=['anish','manish','shubash']     #reversing the list.
alist.reverse()
del alist[1]          # deleting the item on  alist
print(alist)

'''' list comprehension is an elegent and concise way to create a new list 
from an existing list in pyhton 
   new_list =[expression    for item in list   if condition] '''
a=[x for x in range(50) if x%3==0]
#print(a)
b=[3**i for i in range(12)]
#print(b)

v=[422,1,3,24,345,624]
v.sort()
print(v)
v.insert(3,'anish')
print(v)
v.extend('anishh')
print(v)
v.pop(-8)
print(v)

print(len(v))

#for loop on lists
for element in v:
    print(element ,end= " ")