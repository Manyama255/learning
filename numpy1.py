import numpy as np

arr = np.array([1, 2, 3, 4,5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

arr = np.array([1, 2, 3, 4, 5])
y = arr.view()
arr[0] = 42

print(arr)
print(y)

z = arr.view()
z[0] = 31

print(arr)
print(z)

print(x.base)
print(y.base)

print(z.base)