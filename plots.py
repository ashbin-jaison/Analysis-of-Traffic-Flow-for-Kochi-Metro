# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 21:00:44 2020

@author: ME
"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
import warnings
warnings.filterwarnings("ignore")

mydata = pd.read_csv("C:/Users/ME/Desktop/MSc Project/Problem Study/problem_study.csv")

train_data = mydata[0:2944]
test_data=mydata[2944:]

train_data.date_time = pd.to_datetime(train_data.date_time)

train_data['year'] = train_data['date_time'].dt.year
train_data['month'] = train_data['date_time'].dt.month
train_data['day'] = train_data['date_time'].dt.day
train_data['dayofweek'] = train_data['date_time'].dt.dayofweek.replace([0,1,2,3,4,5,6],['monday','tuesday','wednesday','thursday','friday','saturday','sunday'])
train_data['hour'] = train_data['date_time'].dt.hour
train_data.head()


plt.figure(figsize=(10,7))
sns.lineplot(x=train_data['hour'],y=train_data['Count'], markers=True, dashes=False,)

plt.figure(figsize=(10,7))
sns.lineplot(x=train_data['hour'],y=train_data['Count'],hue=train_data['dayofweek'], markers=True, dashes=False)

plt.figure(figsize=(10,7))
sns.lineplot(x=train_data['hour'],y=train_data['Count'],hue=train_data.query("dayofweek in ['saturday','sunday']")['dayofweek'], markers=True, dashes=False)

plt.figure(figsize=(10,7))
sns.lineplot(x=train_data['day'],y=train_data['Count'],  markers=True, dashes=False)