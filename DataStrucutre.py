import numpy as np
import os
os.system('cls')

# list

himpunan = [10,20,30,40,50]
print('\nList')
print(himpunan)
print(type(himpunan))

# Vector

vector_1 = np.array(himpunan)
print('\nVector')
print(vector_1)
print(type(vector_1))

# Matriks
print('\n')
a = [[1,2,3],[3,4,5],[1,0,1]]     
#                                  [1 2 3]
#                                  [3 4 5]
#                                  [1 0 1]
print(a)
print(type(a))

# but if you want to make it simple just use numpy library
print('\n')
b = np.array(a)
print(b)
print(type(b))

# factor