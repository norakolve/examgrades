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
#GRAF
f, ax = plt.subplots()
Y = [mean_mathscore_female, mean_mathscore_male]
X = ["female", "male"]

ax.bar(X, height=Y, color="black")
ax.set_ylabel("Math exam score")

