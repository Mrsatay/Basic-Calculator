
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

def correlation_two_vector(num1,num2):
    mean_x = np.mean(num1)
    mean_y = np.mean(num2)
    simpangan_x = 0
    simpangan_y = 0

    for i in range(len(num1)):
        simpangan_x += (num1[i] - mean_x) ** 2 
        simpangan_y += (num2[i] - mean_y) ** 2
        

    
    simpanganbaku_x = math.sqrt((1 / (len(num1) - 1)) * simpangan_x)
    simpanganbaku_y = math.sqrt((1 / (len(num2) - 1)) * simpangan_y)

    correlation = 0

    for i in range(len(num1)):
        correlation += ((num1[i] - mean_x) / simpanganbaku_x) * ((num2[i] - mean_y) / simpanganbaku_y) 
    correlation *= (1 / (len(num1) - 1))

    return f'from\t{num1}\n\t{num2} \nCorrelation is: {round(correlation,3)}'

a = np.array([random.randint(1,30) for i in range(10)])
b = np.array([random.randint(1,30) for i in range(10)])
print(correlation_two_vector(a,b))

# 8. Buatlah sebuah fungsi yang dapat menghitung euclidean distance antara dua vektor numerik.

def euclideanDistance(num1,num2):
    x = (num1[0] - num1[1]) ** 2
    y = (num2[0] - num2[1]) ** 2
    distance = math.sqrt(x + y)

    return f'from\t{num1}\n\t{num2} \neuclidean distance is: {round(distance,2)}'

variable_x = np.array([random.randint(1,30) for i in range(2)])
variable_y = np.array([random.randint(1,30) for i in range(2)])
print(euclideanDistance(variable_x,variable_y))

# 9. Buatlah sebuah fungsi yang dapat menghitung cosine similarity antara dua vektor numerik.

def cosine_similarity(num1,num2):
    pembilang = 0
    norm_a = 0 # ||a||
    norm_b = 0 # ||b||

    for i in range(len(num1)):
        pembilang += num1[i] * num2[i]
        norm_a += num1[i] ** 2
        norm_b += num2[i] ** 2
    
    norm_a = math.sqrt(norm_a)
    norm_b = math.sqrt(norm_b)

    penyebut = norm_a * norm_b
    hasil = pembilang / penyebut
    return f'from\t{num1}\n\t{num2} \neuclidean distance is: {round(hasil,4)}'


a = np.array([random.randint(1,30) for i in range(5)])
b = np.array([random.randint(1,30) for i in range(5)])
print(cosine_similarity(a,b))

# 10. Buatlah sebuah fungsi yang dapat menghitung dot product antara dua matriks.

def dot_product(num1,num2,degre):
    panjang_a_b = 0
    degre = math.cos(degre)

    for i in range(len(num1)):
        panjang_a_b += num1[i] * num2[i]
    hasil = panjang_a_b * degre

    return f'from\t{num1}\n\t{num2} \ndot product is: {round(hasil,2)}'

a = np.array([random.randint(1,30) for i in range(5)])
b = np.array([random.randint(1,30) for i in range(5)])
degre = 60
print(dot_product(a,b,degre=degre))


# Matriks
# factor
