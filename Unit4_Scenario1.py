
import numpy as np
import pandas as pd

# Create a NumPy array of book prices
prices = np.array([250, 450, 600, 750, 350, 900])

# Calculate average book price
average = np.mean(prices)
print("Average Book Price:", average)

# Create a Pandas DataFrame
df = pd.DataFrame({
    "Book Name": ["Python", "Java", "AI", "Data Science",
                  "C Programming", "Machine Learning"],
    "Price": prices
})

# Display all books
print("\nBook Details:")
print(df)

# Display books costing more than Rs. 500
print("\nBooks Costing More Than Rs. 500:")
print(df[df["Price"] > 500])
