import numpy as np
num= np.arange(1, 11)
print("Original Array:")
print(num)
print("First five elements:")
print(num[:5])
print("Elements from index 2 to 6:")
print(num[2:7])
print("Every second element:")
print(num[::2])
print("Sum:", np.sum(num))
print("Mean:", np.mean(num))
print("Maximum:", np.max(num))
print("Minimum:", np.min(num))
modified_array = num + 5
print("Array after broadcasting (adding 5):")
print(modified_array)
modified_arr2 = num * 2
print("Array after broadcasting (multiplying by 2):")
print(modified_arr2)

"""
=======Output=======
Original Array:
[ 1  2  3  4  5  6  7  8  9 10]
First five elements:
[1 2 3 4 5]
Elements from index 2 to 6:
[3 4 5 6 7]
Every second element:
[1 3 5 7 9]
Sum: 55
Mean: 5.5
Maximum: 10
Minimum: 1
Array after broadcasting adding 5:
[ 6  7  8  9 10 11 12 13 14 15]
Array after broadcasting multiplying by 2:
[ 2  4  6  8 10 12 14 16 18 20]
===================
"""