import pandas as pd
from multiprocessing import Pool
import time

df = pd.read_csv("E:\working datasets\sales.csv")   # Loading the data into pandas dataframe

# function to apply a function over multiple cores

def parallel_apply(Total_Profit, Total_Quantity, w_cores):
    with Pool(w_cores) as p:
        results = p.map(Total_Profit, Total_Quantity)
    return pd.concat(results)

# Core 1

parallel_apply()



