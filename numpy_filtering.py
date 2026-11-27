import numpy as np

data = np.array([10, 25, 35, 50, 65, 80, 95])

print("Original Data:")
print(data)

print("\nValues greater than 50:")
print(data[data > 50])

print("\nValues less than 50:")
print(data[data < 50])

print("\nValues equal to 50:")
print(data[data == 50])

threshold = 70

print(f"\nValues greater than {threshold}:")
print(data[data > threshold])
