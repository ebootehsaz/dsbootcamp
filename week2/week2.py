# Practice Questions for numpy
# q1: Define two custom numpy arrays, say A and B. Generate two new numpy arrays by stacking A and B vertically and horizontally.
# q2: Find common elements between A and B. [Hint : Intersection of two sets]
# q3: Extract all numbers from A which are within a specific range. eg between 5 and 10. [Hint: np.where() might be useful or boolean masks]
# q4: Filter the rows of iris_2d that has petallength (3rd column) > 1.5 and sepallength (1st column) < 5.0

# url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])

import numpy as np
import pandas as pd

def q1():
    # create two arrays size 20 with random numbers
    A = np.random.randint(0, 10, 20)
    B = np.random.randint(0, 10, 20)
    return (A, B)

def q2(A, B):
    # find common elements between A and B
    C = np.intersect1d(A, B)
    return C

def q3(A):
    B = A[(A > 5) & (A < 10)]
    return B

def q4():
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
    # remove the rows of iris_2d that has petallength (3rd column) > 1.5 and sepallength (1st column) < 5.0
    iris_2d = iris_2d[(iris_2d[:, 2] < 1.5) & (iris_2d[:, 0] > 5.0)]
    return iris_2d

# A, B = q1()
# print(A, B)
# print(q2(A, B))
# print(q3(A))
# print(q4())

    
# Practice Questions for Pandas

def practice1():
    # From df filter the 'Manufacturer', 'Model' and 'Type' for every 20th row starting from 1st (row 0).
    df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
    df = df.iloc[::20, [0, 1, 2]]
    return df

def practice2():
    # Replace missing values in Min.Price and Max.Price columns with their respective mean.
    df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
    df['Min.Price'].fillna(df['Min.Price'].mean(), inplace=True)
    df['Max.Price'].fillna(df['Max.Price'].mean(), inplace=True)
    return df

def practice3():
    df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
    df = df[df.sum(axis=1) > 100]
    df['sum'] = df.sum(axis=1) # add a col to quickly verify
    return df 

# print(practice1())
# print(practice2())
# print(practice3())
