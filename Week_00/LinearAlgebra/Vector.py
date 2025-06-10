#Creating Vectors from lists

import numpy as np

list1 = [1,2,3,4,5]
list2 = [
    [10],
    [20],
    [30],
    [40],
]

# Convert list1 to a numpy array
array1 = np.array(list1)

# Convert list2 to a numpy array
array2 = np.array(list2)

# Print the numpy arrays
print(f"Array 1:{array1}")
print(f"Array 2:{array2}")   

#######################################################Operations on the vectors
# importing numpy
import numpy as np

# creating a 1-D list (Horizontal)
list1 = [5, 6, 9]

# creating a 1-D list (Horizontal)
list2 = [1, 2, 3]

# creating first vector
vector1 = np.array(list1)

# printing vector1
print("First Vector          : " + str(vector1))

# creating second vector
vector2 = np.array(list2)

# printing vector2
print("Second Vector         : " + str(vector2))

# adding both the vector
# a + b = (a1 + b1, a2 + b2, a3 + b3)
addition = vector1 + vector2

# printing addition vector
print("Vector Addition       : " + str(addition))

# subtracting both the vector
# a - b = (a1 - b1, a2 - b2, a3 - b3)
subtraction = vector1 - vector2

# printing addition vector
print("Vector Subtraction   : " + str(subtraction))

# multiplying  both the vector
# a * b = (a1 * b1, a2 * b2, a3 * b3)
multiplication = vector1 * vector2

# printing multiplication vector
print("Vector Multiplication : " + str(multiplication))

# dividing  both the vector
# a / b = (a1 / b1, a2 / b2, a3 / b3)
division = vector1 / vector2

# printing division vector
print("Vector Division       : " + str(division))

# dot product of both the vector
# a . b = (a1 * b1 + a2 * b2 + a3 * b3)
dot_product = np.dot(vector1, vector2)

# printing dot product
print("Vector Dot Product    : " + str(dot_product))

#scalar multiplication
scalar = 2
scalar_multiplication = scalar * vector1
# printing scalar multiplication
print("Scalar Multiplication : " + str(scalar_multiplication))
