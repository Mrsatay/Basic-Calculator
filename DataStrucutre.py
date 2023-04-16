
import os
os.system('cls')

# list


# Vector

import numpy as np
import random
import math

# 1. Buatlah sebuah fungsi yang dapat menghitung mean dari sebuah vektor numerik.

def calculate_mean(num1,num2):

total = num1.sum() + num2.sum()

return f'Mean from those vector is: {total/(len(num1) + len(num2))}'

a = np.array([[1,2,3,4,5],[6,7,8,9,10]])
b = np.array([[1,4,9,16,25] , [36,49,64,81,100]])



# 2. Buatlah sebuah fungsi yang dapat menghitung median dari sebuah vektor numerik.

def calculate_median(num):

    sorting_vect = np.sort(num)

    if len(num)%2 == 0:
        return f'from {sorting_vect} \nmedian is: {(sorting_vect[4] + sorting_vect[5])/2}'

    else:
        return f'from {num} \nmedian is: {sorting_vect[int(len(num)/2)]}'

a = np.array([random.randint(1,50) for i in range(10)])
print(calculate_median(a))

# 3. Buatlah sebuah fungsi yang dapat menghitung modus dari sebuah vektor numerik.

def calculate_modus(num):
    
    mode = num[0]

    for i in range(len(num) - 1):
        
        if np.count_nonzero(num == mode) < np.count_nonzero(num == num[i + 1]):
            mode = num[i + 1]
        else:
            pass

    return f'from {num} \nmode is: {mode}'
    
a = np.array([random.randint(1,30) for i in range(10)])
print(calculate_modus(a))   
    # this code it's not done yet because it just done for show 1 mode value, but
    # what if there is more than one mode value?



# 4. Buatlah sebuah fungsi yang dapat menghitung variance dari sebuah vektor numerik.

def calculate_variance_singleData(num):

    avg = np.mean(num)
    res = 0
    n = len(num)

    for i in range(n):
        res = (num[i] - avg) ** 2
    
    return f'from {num} \nvariance single data is: {round(res/n,2)}'

a = np.array([random.randint(1,30) for i in range(10)])
print(calculate_variance_singleData(a))


# 5. Buatlah sebuah fungsi yang dapat menghitung standard deviation dari sebuah vektor numerik.

def calculate_standard_deviation(num):

    avg = np.mean(num)
    res = 0
    n = len(num)

    for i in range(n):
        res = (num[i] - avg) ** 2

    std = round(math.sqrt(res/n),2)

    return f'from {num} \nstandard deviation is: {std}'

a = np.array([random.randint(1,30) for i in range(10)])
print(calculate_standard_deviation(a))

# 6. Buatlah sebuah fungsi yang dapat menghitung covariance matrix dari dua vektor numerik.

def covariance_matrix(num1,num2):

    avg_x = np.mean(num1)
    avg_y = np.mean(num2)   
    Xi_Xavg = []
    Yi_Yavg = []
    product = []
    n = len(num1)

    for i in range(n):
        Xi_Xavg.append(num1[i] - avg_x)
        Yi_Yavg.append(num2[i] - avg_y)
        product.append(Xi_Xavg[i] * Yi_Yavg[i])

    product = np.array(product)
    covariance = round(product.sum() / (n - 1),2)
    return f'from\t{num1}\n\t{num2} \nCovariance is: {covariance}'


a = np.array([random.randint(1,30) for i in range(10)])
b = np.array([random.randint(1,30) for i in range(10)])
print(covariance_matrix(a,b))

# 7. Buatlah sebuah fungsi yang dapat menghitung correlation matrix dari dua vektor numerik.



# 8. Buatlah sebuah fungsi yang dapat menghitung euclidean distance antara dua vektor numerik.
# 9. Buatlah sebuah fungsi yang dapat menghitung cosine similarity antara dua vektor numerik.
# 10. Buatlah sebuah fungsi yang dapat menghitung dot product antara dua matriks.

# Matriks
# factor
