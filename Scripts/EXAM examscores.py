#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:18:06 2023

@author: norakolve
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 15:11:59 2023

@author: norakolve
"""
# %%
# Importering av data
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
filename = "/Users/norakolve/Documents/2022:2023/GitHub/examgrades/Data/exams.csv"
df = pd.read_csv(filename)

filter_male = df["gender"] == "male"
df_male = df[filter_male]

mean_mathscore_male = df_male["math score"].mean()

filter_female = df["gender"] == "female"
df_female = df[filter_female]

mean_mathscore_female = df_female["math score"].mean()


#%%
#GRAF MEAN math score vs gender
f, ax = plt.subplots()
Y = [mean_mathscore_female, mean_mathscore_male]
X = ["Female", "Male"]

ax.bar(X, height=Y, color="purple")
ax.set_ylabel("Mean math exam score")

#%%
#GRAF MEAN writing score vs gender

mean_writingscore_male = df_male["writing score"].mean()
mean_writingscore_female = df_female["writing score"].mean()

f, ax = plt.subplots()
Y = [mean_writingscore_female, mean_writingscore_male]
X = ["Female", "Male"]

ax.bar(X, height=Y, color="black")
ax.set_ylabel("Mean writing exam score")

#%%
#GRAF MEAN reading score vs gender

mean_readingscore_male = df_male["reading score"].mean()
mean_readingscore_female = df_female["reading score"].mean()

ax.bar(X, height=Y, color="blue")
ax.set_ylabel("Mean reading exam score")

#%%

