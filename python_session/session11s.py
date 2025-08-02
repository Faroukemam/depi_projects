# Import necessary libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# tips ,flights , titanic

# Load the tips dataset
df = sns.load_dataset('tips')
print (df.head())
print(df.tail())
# Display basic information about the dataset
print(df.info())
print(df.describe())