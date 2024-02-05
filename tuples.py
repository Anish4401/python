# Tuples are immutable they cannot be changed but lists are mutable.
#a=('anihs','manish','jhaji')
#a[0]='anish'
#print(a)    # so here it doesnot support it

#work process is almost similar with lists

#lets know more about the sets & dictionary
'''sets are represented by {} and it does not repeat the string ,int or any 
value and specially it doesnot assign the index value because data is 
not present is systametic order'''

marks={'anish':33,'manish':44,'ramesh':55}
marks['anish']=34                 #updating the values (same key then only values getting updated)
print(marks ['anish'])          #calling the marks of anish

for i in marks:            #for loop /itreating in dictionary 
    print(marks[i])
