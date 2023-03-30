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

f, ax = plt.subplots()
Y = [mean_readingscore_female, mean_readingscore_male]
X = ["Female", "Male"]

ax.bar(X, height=Y, color="blue")
ax.set_ylabel("Mean reading exam score")

#%%
# GROUPED bar chart with all exam grades
#import trompy as tp
m_writing = list(df_male["writing score"])
f_writing = list(df_female["writing score"])
m_reading = list(df_male["reading score"])
f_reading = list(df_female["reading score"])
m_math = list (df_male["math score"])
f_math = list(df_female["math score"])

#tp.barscatter([m_writing,f_writing])
#tp.barscatter([[m_writing,f_writing],[m_reading,f_reading],[m_math, f_math]])

#%%
#Making standard lunch and free/reduced lunsh into two different groups


filter_standardlunch = df["lunch"] == "standard"
df_standardlunch = df[filter_standardlunch]


filter_freelunch= df["lunch"] == "free/reduced"
df_freelunch = df[filter_freelunch]

#%%
#   lunch types and math scores 
mean_mathscore_standardlunch = df_standardlunch["math score"].mean()
mean_mathscore_freelunch = df_freelunch["math score"].mean()

#%% Violin plot over math score and lunch types
fig, ax = plt.subplots()

ax.violinplot([df_standardlunch["math score"],  df_freelunch["math score"]], [0,1])
ax.set_title('Math exam score and lunch types')
ax.set_ylabel('Math exam score')
   
ax.set_xticks([0, 1])
ax.set_xticklabels(['Standard lunch', 'Free/reduced lunch'])

#%%
#Test preparation course, making two groups: completed and none

filter_preparation_c = df["test preparation course"] == "completed"
df_preparation_c = df[filter_preparation_c]


filter_preparation_n = df["test preparation course"] == "none"
df_preparation_n = df[filter_preparation_n]

#%% Mean exam scores all three for the two genders

data = [[63.196687370600415, 71.88819875776397, 71.7080745341615],
[69.38491295938104, 66.30560928433269, 64.02901353965184]]


X = np.arange(3)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
space = 0.2
width = 0.4

ax.bar(X - space, data[0], color = 'pink', width = width, label = "Female")
ax.bar(X + space, data[1], color = 'grey', width = width, label = "Male")

ax.set_title("Mean exam scores for male and female on all three exams", weight = "bold")
ax.set_ylabel("Mean exam score")
ax.set_xticks(X)
ax.set_xticklabels(["Math exam","Reading exam", "Writing exam"])
ax.grid(axis = "y")
ax.legend(loc = "upper right")
ax.set_xlim([-0.6, 3])
 

