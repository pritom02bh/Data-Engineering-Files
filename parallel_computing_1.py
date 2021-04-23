import pandas as pd
from multiprocessing import Pool  

df = pd.read_csv("E:\working datasets\sales.csv")   # reading the data set

# function to apply a function over multiple cores

def parallel_apply(Total_Profit, Total_Quantity, w_cores):
    with Pool(w_cores) as p:
        results = p.map(Total_Profit, Total_Quantity)
    return pd.concat(results)



