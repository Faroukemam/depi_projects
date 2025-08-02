
import numpy as np

a =np.array([1, 2, 3], dtype = 'int8')
b = np.array([[4, 5, 6], [7, 8, 9]], dtype = 'int16')
c = np.array([[10, 11], [12, 13], [14, 15]], dtype = 'int32')

'''
## Displaying the properties of the arrays
# array a
print('=' * 20)
print(a.dtype)
print(a.size)
print(a.itemsize)
print(f"total bytes: {a.nbytes}")
print(a.ndim)
print(a.shape)


# array b
print('=' * 20)
print(b.dtype)
print(b.size)
print(b.itemsize)
print(f"total bytes: {b.nbytes}")
print(b.ndim)
print(b.shape)


# array c
print('=' * 20)
print(c.dtype)
print(c.size)
print(c.itemsize)
print(f"total bytes: {c.nbytes}")
print(c.ndim)
print(c.shape)
print('=' * 20)
'''
# Displaying the properties of the arrays
print('=' * 20)
print(b)
print(b[0,:])

a= np.random.randint(0, 100, size=(3, 3))
print(a)

