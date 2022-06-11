# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 13:03:38 2022

@author: Arfiah
"""

#Latihan-1
import numpy as np
a = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
a = np.array([[1 , 2, 3, 4],[9, 10, 11, 12]])



#Latihan-2
import numpy as np
print (np.zeros(6))
print (np.ones(6))
print (np.empty(6))
print(np.arange(4))
print(np.arange(0,10,2)) # (start, stop, step)
print(np.arange(2,29,5))


#Latihan-3
arr = np.array([1,2,3,4,5,6,7])
#np_append(Penambahan)
print(np.append(arr,[1,2]))
#np.delete(arr,1)
print(np.delete(arr,0))
#np.Sort asscending
print(np.sort(arr))


#Latihan-4

array_example = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]]])

print(array_example)
print(array_example.ndim)
print(array_example.size)
print(array_example.shape)

arr_one = np.array([[1, 2, 3, 4, 5]])
print(arr_one.ndim)
print(arr_one.size)
print(arr_one.shape)

a = np.arange(6)
print(a)

b = a.reshape(3,2)
print(b)

b= a.reshape(6,1)
print(b)

b = a.reshape(2,3)
print(b)



#Latihan14

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(a.shape)
###
a2 = a[np.newaxis]
print(a2.shape)
print(a2)
###
row_vector = a[np.newaxis, :]
print(row_vector.shape)
print(row_vector)
###
col_vector = a[:, np.newaxis]
print(col_vector.shape)
print(col_vector)
###
a = np.array([1, 2, 3, 4, 5, 6])
a.shape
b = np.expand_dims(a, axis=1)
print(b.shape)
b = np.expand_dims(a, axis=0)
print(b.shape)

#Latihan-15

data = np.array([1,2,3,3,4,5,6,7,8,9])

print(data)
print(data[0])
print(data[1])
print(data[0:2])
print(data[1:])
print(data[-2:])
print(data[5:])
print(data[:5])

####
a=np.array([1,2,3,4,5,6])
b=sorted(a, reverse=True)
print(b[0:])


#Latihan-16

a = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
print(a[a>=5])

five_up = (a >= 5)
print(a[five_up])
print(a[a>=5])

divisible_by_2 = a[a%2==0]
print(divisible_by_2)

c = a[(a > 2) & (a < 11)]
print(c)


#Latihan-17

arr = np.array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
arr1 = arr[3:8]
print(arr1)

####
a_1 = np.array([[1, 1],
                [2, 2]])
a_2 = np.array([[3, 3],
                [4, 4]])
print(np.vstack((a_1, a_2)))
print(np.hstack((a_1, a_2)))
###
arrsplit = np.array([[1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12],
                     [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]])

print(arrsplit)
print(np.hsplit(arrsplit,3))

###
a = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
###
b=a.view()
print(b)
###
c=a.copy()
print(c)

##
a = np.array([1, 2, 3, 4])

# Add all of the elements in the array
print(a.sum())
###
b = np.array([[1, 1], [2, 2]])
print(b)

###
bsplit = np.array([1,2,3,4,5,6])
print(np.hsplit(bsplit,3))

#Latihan-18
a=np.array([[1,2,3,4],
           [5,6,7,8],
           [9,10,11,12]])
print(a)

a.sum(axis=0)
print(a.sum(axis=0))

a.sum(axis=1)
print(a.sum(axis=1))

ones = np.ones(3)
print(ones)

print(a)

a*a
a/a

###Latihan-19
A = np.array([[0.45053314, 0.17296777, 0.34376245, 0.5510652],
              [0.54627315, 0.05093587, 0.40067661, 0.55645993],
              [0.12697628, 0.82485143, 0.26590556, 0.56917101]])

print(A)

print(A.sum())
print(A.min())

###Latihan-20
a_1 = np.array([[1, 2, 3], [4, 5, 6]])
print(a_1)
print(a_1.shape)

a_2 = np.array([[7, 8], [9, 10], [11, 12]])
print(a_2)
print(a_2.shape)

print(np.dot(a_1, a_2))

###

data = np.array([[1, 2], [3, 4], [5, 6]])

print(data)
print(data[0])
print(data[1])
print(data[2])
print(data[0,1])
print(data[1:3])
print(data[0:2,1])




































