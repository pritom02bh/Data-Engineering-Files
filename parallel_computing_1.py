import pandas as pd
from multiprocessing import pool

df = pd.read_csv("E:\working datasets\sales.csv")

def parallel_apply()