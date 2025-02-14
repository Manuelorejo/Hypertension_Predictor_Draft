# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 22:45:54 2025

@author: Oreoluwa
"""

#Import statements
import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

st.title('HYPERTENSION PREDICTOR')



#Assignment of arbitray values to variables   
cp = 0
chol = 286  
restecg = 1
exang = 1
oldpeak = 1.5
slope = 1
cal = 3
thal = 2

#Collecting user input
age = st.number_input('How old are you? ')
age = float(age)

gender = st.radio("What is your gender?",["Male","Female"])
if gender == "Male":
    gender = 1.0
else:
    gender = 0.0
    
bp = st.number_input("What is your resting blood pressure? ")

sugar = st.radio("When fasting, does your blooc sugar exceed 120mg/dl", ["Yes","No"])
if sugar == "Yes":
    sugar = 1
else:
    sugar = 0
    

heart_rate = st.number_input("What is your maximum heart rate achieved? ")


#Reading dataset and dropping missing values
df = pd.read_csv('hypertension_data.csv')

df.dropna(inplace = True)




#Feature selection and splitting
X = df.drop('target',axis =1)
y = df['target']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3, random_state=101 )

#Training model
model = LogisticRegression()

model.fit(X_train,y_train)

#Displaying results
submit = st.button('SUBMIT')
if submit:
    pred = model.predict([[age,gender,cp,bp,chol,sugar,restecg,heart_rate,exang,oldpeak,slope,cal,thal]])
    
    if pred == 1:
        st.write("You are hypertensive")
        
    else:
        st.write("You are not hypertensive")

