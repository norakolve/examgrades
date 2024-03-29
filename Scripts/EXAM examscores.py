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
# %% Importing data and additional packages that I am going to use in the coding

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

filename = "/Users/norakolve/Documents/2022:2023/GitHub/examgrades/Data/exams.csv"
df = pd.read_csv(filename)

#%% Making a filter for gender (male and female) so that we can analyse them as seperate variables

filter_male = df["gender"] == "male"
df_male = df[filter_male]

filter_female = df["gender"] == "female"
df_female = df[filter_female]

#%% Making variables that I will use later in the analysis

mean_mathscore_male = df_male["math score"].mean()  #This is the mean mathscore for males on the exam
mean_mathscore_female = df_female["math score"].mean() #This is the mean mathscore for females on the exam

mean_writingscore_male = df_male["writing score"].mean() #This is the mean writingscore for males on the exam
mean_writingscore_female = df_female["writing score"].mean() #This is the mean writingscore for females on the exam

mean_readingscore_male = df_male["reading score"].mean() #This is the mean readingscore for males on the exam
mean_readingscore_female = df_female["reading score"].mean() #This is the mean readingscore for females on the exam

#%% Making bargraph with mean exam score for female and male

f, ax = plt.subplots()
Y = [mean_mathscore_male, mean_mathscore_female]
X = ["Male", "Female"]

ax.bar(X, height = Y, color = "grey")
ax.grid(axis = "y")
ax.set_title("Mean math exam score for female and male", weight = "bold")
ax.set_ylabel("Mean math exam score")

#GRAF MEAN math score vs gender
f, ax = plt.subplots()
Y = [mean_mathscore_male, mean_mathscore_female]
X = ["Female", "Male"]

ax.bar(X, height=Y, color= "mediumpurple" )

ax.set_title("Mean math exam score for male and female", weight = "bold")
ax.set_ylabel("Mean math exam score")
ax.grid(axis = "y")
 
#%% Making a bargraph with mean writing score for female and male

f, ax = plt.subplots()
Y = [mean_writingscore_female, mean_writingscore_male]
X = ["Female", "Male"]

ax.bar(X, height = Y, color = "pink")
ax.grid(axis = "y")
ax.set_title("Mean writing exam score for female and male", weight = "bold")
ax.set_ylabel("Mean writing exam score")

#%% Making a bargraph for mean reading score for female and male

f, ax = plt.subplots()
Y = [mean_readingscore_female, mean_readingscore_male]
X = ["Female", "Male"]

ax.grid(axis = "y")
ax.bar(X, height = Y, color = "indianred")
ax.set_title("Mean reading exam score for female and male", weight = "bold")
ax.set_ylabel("Mean reading exam score")

#%% Making standard lunch and free/reduced lunsh into two different groups 

filter_standardlunch = df["lunch"] == "standard"
df_standardlunch = df[filter_standardlunch]


filter_freelunch= df["lunch"] == "free/reduced"
df_freelunch = df[filter_freelunch]

#%%
#Making vaiables for the two different lunch types and their math exam scores 

mean_mathscore_standardlunch = df_standardlunch["math score"].mean()
mean_mathscore_freelunch = df_freelunch["math score"].mean()

#%% Making a violin plot over math score and lunch type
fig, ax = plt.subplots()

ax.violinplot([df_standardlunch["math score"],  df_freelunch["math score"]], [0,0.5])
ax.set_title('Math exam score and lunch type', weight = "bold")
ax.set_ylabel('Math exam score')
 
ax.grid(axis = "y")
ax.set_xticks([0, 0.5])
ax.set_xticklabels(['Standard lunch', 'Free/reduced lunch'])

#%%
#Making two groups, one for those that completed the test preparation course, and one for those that did not complete none

filter_preparation_c = df["test preparation course"] == "completed"
df_preparation_c = df[filter_preparation_c]


filter_preparation_n = df["test preparation course"] == "none"
df_preparation_n = df[filter_preparation_n]

#%%
#Making vaiables for the two different test preperation groups and their math exam scores 

mean_mathscore_preparation = df_preparation_c["math score"]
mean_mathscore_nonepreparation = df_preparation_n["math score"]

#%% Making a violin plot over math score and lunch type
fig, ax = plt.subplots()

ax.violinplot([df_preparation_c["math score"],  df_preparation_n["math score"]], [0,0.5])
ax.set_title('Math exam score and preparation course', weight = "bold")
ax.set_ylabel('Math exam score')
 
ax.set_xticks([0, 0.5])
ax.grid(axis = "y")
ax.set_xticklabels(['Preparation course completed', 'None preparation course'])

#%% Mean exam scores all three for the two genders

data = [[63.196687370600415, 71.88819875776397, 71.7080745341615],[69.38491295938104, 66.30560928433269, 64.02901353965184]]

X = np.arange(3)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
space = 0.2
width = 0.35

ax.bar(X - space, data[0], color = 'palevioletred', width = width, label = "Female")
ax.bar(X + space, data[1], color = 'steelblue', width = width, label = "Male")

ax.set_title("Mean exam scores for male and female on all three exams", weight = "bold")
ax.set_ylabel("Mean exam score")
ax.set_xticks(X)
ax.set_xticklabels(["Math exam","Reading exam", "Writing exam"])
ax.grid(axis = "y")
ax.legend(loc = "upper right")
ax.set_xlim([-0.6, 3])

#%% Filtering parental level of education intro different groups
 
filter_high_schoollll = df["parental level of education"] == "high school"
df_high_school = df[filter_high_school]

filter_some_high_school = df["parental level of education"] == "some high school"
df_some_high_school = df[filter_some_high_school]

filter_some_college = df["parental level of education"] == "some college"
df_some_colleg = df[filter_some_college]


filter_bachelors_degree = df["parental level of education"] == "bachelor's degree"
df_bachelors_degree = df[filter_bachelors_degree]
                         
filter_some_high_school= df["parental level of education"] == "some high school"
df_some_high_school = df[filter_some_high_school]

filter_masters= df["parental level of education"] == "master's degree"
df_masters = df[filter_masters]

filter_associates= df["parental level of education"] == "associate's degree"
df_associates = df[filter_associates]

#%% Exam score on the reading exam in a graph with parental level of education
#Making variables of the parental level of educations that I have choosen to look into and reading scores on the exam

readingscore_high_school = df_high_school["reading score"]
readingscore_bachelors_degree = df_bachelors_degree["reading score"]
readingscore_masters_degree = df_masters["reading score"]

# Making the violin plot

fig, ax = plt.subplots()

ax.violinplot ([readingscore_high_school, readingscore_bachelors_degree, readingscore_masters_degree],[0, 0.5, 1])
ax.set_title('Reading exam score and parental level of education', weight = "bold")
ax.set_ylabel('Reading exam score')

 
ax.set_xticks([0, 0.5, 1])
ax.grid(axis = "y")
ax.set_xticklabels(['High school', "Bachelor´s degree", 'Master´s degree'])

#%% Exam score on the math exam in a graph with parental level of education 
# Making variables of the parental level of educations that I have choosen to look into and scores on the math exam
mathscore_high_school = df_high_school["math score"]
mathscore_bachelors_degree = df_bachelors_degree["math score"]
mathscore_masters_degree = df_masters["math score"]

# Making the violin plot

fig, ax = plt.subplots()

ax.violinplot ([mathscore_high_school, mathscore_bachelors_degree, mathscore_masters_degree],[0, 0.5, 1])
ax.set_title('Math exam score and parental level of education', weight = "bold")
ax.set_ylabel('Math exam score')

 
ax.set_xticks([0, 0.5, 1])
ax.grid(axis = "y")
ax.set_xticklabels(['High school', "Bachelor´s degree", 'Master´s degree'])
