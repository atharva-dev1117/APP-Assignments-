import pandas as pd

# Create Series
data = pd.Series([15, 25, 35, 45], index=['p', 'q', 'r', 's'])
print(data)

# Update elements
s = pd.Series([150, 250, 350], index=['m', 'n', 'o'])

s['n'] = 550
s[['m', 'o']] = [222, 888]

print(s)

# Convert Series
s = pd.Series([5, 10, 15], index=['x', 'y', 'z'])

list_data = s.tolist()
dict_data = s.to_dict()
array_data = s.to_numpy()

print("\n \n List:", list_data)
print("Dictionary:", dict_data)
print("NumPy Array:", array_data)

# Sorting
s = pd.Series([70, 20, 50, 40], index=['g', 'b', 'e', 'd'])

sorted_values = s.sort_values()
sorted_index = s.sort_index()

print("Sorted by Values:")
print(sorted_values)

print("\nSorted by Index:")
print(sorted_index)
