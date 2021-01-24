# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 13:57:16 2021

@author: thebe
"""

import pandas as pd
import numpy as np
import csv
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.models import BayesianModel
from pgmpy.inference import VariableElimination

# Read the attributes
lines = list(csv.reader(open('heart.csv', 'r')))
attributes = lines[0]   
print(attributes)

# Read the Cleveland Heart Disease data
heartDisease = pd.read_csv('heart.csv', names= attributes)
heartDisease = heartDisease.replace('?', np.nan)              # Handling missing values

# View the data
print('Few examples from the dataset are given below- ')
print(heartDisease.head())
print('\nAttributes and data types-')
print(heartDisease.dtypes)

# Model a Bayesian Network
model = BayesianModel([('age', 'trestbps'), ('age', 'fbs'), ('sex', 'trestbps'),
('exang', 'trestbps'), ('trestbps', 'heartdisease'),
('fbs', 'heartdisease'), ('heartdisease', 'restecg'), ('heartdisease', 'thalach'),
('heartdisease', 'chol')])

# Learning CPD's (Conditional Probability Distribution) using Maximum Likelihood Estimators
print('\nLearning CPDs using Maximum Likelihood Estimators...')
model.fit(heartDisease, estimator=MaximumLikelihoodEstimator)

#Deducing with Bayesian Network
print('\nInferencing with Bayesian Network:')
HeartDisease_infer = VariableElimination(model)

print('\n1.Probability of HeartDisease given Age = 20') 
q = HeartDisease_infer.query(variables=['heartdisease'], evidence={'age': 20})
print(q)
