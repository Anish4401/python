'''so in case of string on python the 
indexing is same as another language 
but it has reverse indexing also.
which start from the end and goes like (-1,..... till -n)'''

fruit='apple'
#print(fruit[4])
#print(fruit[-1])

my_char=fruit[2]
#print(my_char) # here we hold the vlaue of character with using the indexing

#slicing
d="adjkcnjadsk"
print(d[3:8]) #here starting is inclusive and ending is exclusive.
print(d[3:8:2]) #the 3rd element implies the step/jump between them.
print(d[:8])#it will print the first 8th index.
print(d[3:])#it will print the upcoming index including the 3rd index.
print(d[::-1])#it just reverse the string.
print(d[3:8:-1])# it means the indexing direction and iterating direction is difitferent.
print(d[-1:0:-1])#it also does the same but exclude the ending element.
print(d[-1:0:1])# itmeans the indexing direction and iterating direction is difitferent

a='abs'
b='cid'
c=a+b   # so here we can do concatination with help of + oprator also.
c*=2
c*=4    # we can do multiplication also after that.
print(c)

a="rbi"
for a_char in a:
    print(a_char*2)   # so in case of loop it will itrerate on with each char and then move forward.


print(d) # string remains same because it is immutable

#String oprator 
password="abn2sd"
print(password.isalnum()) #it hold alpha and number both but it should have atleast one char and num doesnt matter
num='2314'
print(num.isdigit())
print(password.islower())
print(password.isidentifier())
print (password.upper())

x="   nkfaks   "
print(x.lstrip())

print(x.rstrip())