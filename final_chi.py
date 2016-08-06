import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv('Energy_Usage_2010.csv')
#
# df = df.dropna(axis=0)
#
# for i,val in enumerate(df["GAS ACCOUNTS"]):
#     if type(val) != int and type(val) != float:
#             if "Less" in val:
#                 df["GAS ACCOUNTS"][i] = 2
#     else:
#          df["GAS ACCOUNTS"][i] = int(val)

for i,val in enumerate(df["GAS ACCOUNTS"]):
    try:
        int(val)
    except Exception as e:
        print str(e)
        print "error at", i,val
        break

X = df[[
# 'KWH TOTAL SQFT',
# 'THERMS TOTAL SQFT',
# 'CENSUS BLOCK',
# 'TOTAL POPULATION',
# 'TOTAL UNITS',
# 'AVERAGE HOUSESIZE',
# 'OCCUPIED UNITS',
# 'OCCUPIED HOUSING UNITS',
# 'RENTER-OCCUPIED HOUSING UNITS'
'GAS ACCOUNTS',
#'ELECTRICITY ACCOUNTS',
#'BUILDING_SUBTYPE'
]]

Y = df['TOTAL THERMS']

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=.70, random_state=4444)

#logistic regression
model = LogisticRegression().fit(X_train, Y_train)
Y_test_pred = model.predict(X_test)

logit_accuracy = accuracy_score(Y_test, Y_test_pred)
print 'Logistic Regression accuracy: %.9f' % logit_accuracy
