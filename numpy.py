import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[0])



import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])




import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)




import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)

# Data
# Exploration
# np.shape(data)
# → Get the dimensions of your dataset.
#
# np.size(data)
# → Total number of elements.
#
# np.mean(data, axis=0)
# → Column-wise mean (e.g., average salary).
#
# np.median(data, axis=0)
# → Column-wise median.
#
# np.std(data, axis=0)
# → Column-wise standard deviation.
#
# np.min(data, axis=0)
# → Minimum values per column.
#
# np.max(data, axis=0)
# → Maximum values per column.




# Data Analysis
#
# np.percentile(data[:, 1], 75)
# → 75th percentile of a specific column (e.g., salary column).
#
# np.unique(data[:, 2])
# → Unique values in a column (e.g., job titles if categorical and encoded).
#
# np.argsort(data[:, 1])
# → Indices that would sort the salary column.
#
# np.sort(data, axis=0)
# → Sort each column individually.



# Data manipulation

# np.where(data[:, 1] > 50000)
# → Find rows where salary > 50K.
#
# np.delete(data, [0], axis=0)
# → Delete the first row (e.g., headers if mistakenly loaded).
#
# np.concatenate([data, new_data], axis=0)
# → Combine datasets.
#
# np.reshape(data, (-1, data.shape[1]))
# → Reshape the data for modeling or batching.


import numpy as np
import os

# Step 1: Set file path to your Desktop (adjust username or path if needed)
file_path = os.path.expanduser('~/Desktop/salaries.csv')

# Step 2: Load the data (assuming it has a header and numeric columns)
data = np.genfromtxt(file_path, delimiter=',', skip_header=1)

# Step 3: Explore the data using NumPy functions

print("Shape of data:", data.shape)                     # 1. Dimensions
print("Total size:", data.size)                         # 2. Total number of elements
print("Column-wise Mean:", np.mean(data, axis=0))       # 3. Mean
print("Column-wise Median:", np.median(data, axis=0))   # 4. Median
print("Standard Deviation:", np.std(data, axis=0))      # 5. Standard deviation
print("Minimum values:", np.min(data, axis=0))          # 6. Min
print("Maximum values:", np.max(data, axis=0))

# Analyzing specific columns (example: column 1 = salary)
print("75th Percentile of column 1:", np.percentile(data[:, 1], 75))  # 8. Percentile

# Unique values in column 2
print("Unique values in column 2:", np.unique(data[:, 2]))           # 9. Unique

# Sorting and filtering
sorted_indices = np.argsort(data[:, 1])                               # 10. Argsort
print("Indices to sort column 1:", sorted_indices)

print("Sorted data by column 1:\n", data[sorted_indices])            # 11. Sort rows by column

# Filter example: salaries > 50000
high_salary_indices = np.where(data[:, 1] > 50000)                   # 12. Where
print("High salary rows:\n", data[high_salary_indices])

# Delete first row if needed
data_cleaned = np.delete(data, 0, axis=0)                            # 13. Delete

# Example: combine with another array (mock example)
dummy_data = np.ones((1, data.shape[1]))
combined = np.concatenate([data, dummy_data], axis=0)               # 14. Concatenate
print("Combined shape:", combined.shape)

# Reshape (e.g., for batching)
reshaped = np.reshape(data, (-1, data.shape[1]))                    # 15. Reshape
print("Reshaped data shape:", reshaped.shape)
