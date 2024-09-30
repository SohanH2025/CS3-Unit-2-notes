import numpy as np
import pandas as pd


#panda series object
#series are 10 arrays of index data
data = pd.Series([1, 2,3,4,5, 6, 7, 8, '9.0',10])
print(data.values) #looks like list
print(data.index) #range computed for inicies 

print(f"\ndata at value 1 is {data[1]}\n\nmultiple values shows indicies")
print(data[1:5])

#series are like arrays but with specific indexs d
data = pd.Series([1,2,3],index=['a', 'b', 'c'])
print(data)