import numpy as np
arr1=np.array(([1,2,3],[4,5,6],[7,8,9]))

#creation of fixed value array
arr=np.ones((3,4)) #3*4 array of 1
arr2=np.zeros((3,4))
arr3=np.full((3,4),7) #3*4 arr of 7 val

#identity mat
idmat=np.eye(4)

#make array of fixed order
mat=np.arange(1,100,10) #[1,1+10=11,11+10=21...91]

#make array of size 5 vlues are evenely spaced betn 1 to 100.
a=np.linspace(1,100,5)

#Changing datatype
myarr=np.array(([1,2,3],[4,5,6],[7,8,9],[10,11,12]) , dtype=int)
myarr.astype('float64') #convert myarr into float

#Reshaping Array
print(myarr.shape) # 4*3
myarr=myarr.reshape((6,2))
print(myarr.shape)
myarr=myarr.flatten() #convert 2D into 1D array
print(myarr)

#common functions
# print("no of elements :- ",arr.size)
# print("Shape :- ",arr.shape)
# print("Dimensions :- ",arr.ndim)
# print("Data Type :- ",arr.dtype)