#list and methods

li=[1,2,3,"prasad",33.2,[4,5,6]]

# for i in li:
#     print(i)
    
# print(li[5])
# b=li[5]
# print(b[0]) #4

li.append(10)

l2=[121,12]
li.extend(l2)

li.pop(3)  #pop(index)
l2.sort()

print(l2.index(121)) #return first index of occurence of no.

l2.reverse()

l2.insert(1,22)

print(l2.count(22)) #count no of occurence

a="p.r.a.s.a.d"
c=a.split('.')  #split string into list instead .
print(c)


#***Tuple****
#Tuple is same as list but it is immutable

a={1,2,3}
a[1]=3 #error
