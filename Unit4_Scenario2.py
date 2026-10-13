
import numpy as np
import pandas as pd

# Create a NumPy array of course fees
fees = np.array([20000, 30000, 45000, 25000, 35000])

# Calculate average, maximum, and minimum fees
print("Average Course Fee:", np.mean(fees))
print("Maximum Course Fee:", np.max(fees))
print("Minimum Course Fee:", np.min(fees))

# Create a Pandas DataFrame
data = {
    "Course": ["Python", "Java", "Data Science", "Web Development", "AI & ML"],
    "Fee": fees
}

df = pd.DataFrame(data)

# Display the DataFrame
print("\nCourse Fee Details:")
print(df)

# Display courses whose fee is greater than ₹25,000
print("\nCourses with Fees Greater than ₹25,000:")
print(df[df["Fee"] > 25000])
