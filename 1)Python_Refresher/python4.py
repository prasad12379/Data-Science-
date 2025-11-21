#Set 
a=set() #declaration of empty set not a={}
s={1,3,4,5,6}
s.add(2)
s.pop() #remove 1st element
s.clear() #remove all elmnt
s.update([1,4,3,2]) #use to add more than 1 value in set

#Operations in set
set1={1,2,3,4,4}
set2={3,4,5,6,7}
p=set1.union(set2)
r=set1.intersection(set2)
print()
