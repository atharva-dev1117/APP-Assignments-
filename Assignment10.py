import numpy as np

# Create a one-dimensional array from 1 to 10
arr = np.arange(1, 11)

print("Original Array:")
print(arr)

# Slicing operations
print("\nFirst five elements:")
print(arr[:5])

print("\nElements from index 2 to 6:")
print(arr[2:7])

print("\nAlternate elements:")
print(arr[::2])

# Statistical measures
print("\nStatistical Measures:")
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# Broadcasting
# Add 5 to every element
arr = arr + 5

print("\nArray after broadcasting (adding 5):")
print(arr)
