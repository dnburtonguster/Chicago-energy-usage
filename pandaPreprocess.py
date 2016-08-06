import pandas as pd
import sys

path = sys.argv[1]

def binifyCol(df,colName):
    bins = pd.get_dummies(df[colName])
    df = df.join(bins,rsuffix='_sub')
    df = df.drop(colName,1)
    return df

#'/home/energy/Energy_Usage_2010.csv'
print "reading csv...\n"
df = pd.read_csv(path)

print "removing rows containing NaN...\n"
df = df.dropna(axis=0)

print "replacing string values in GAS ACCOUNTS...\n"
df = df.replace({"GAS ACCOUNTS":{"Less than 4":2}})
print "doing the same for ELECTRIC ACCOUNTS...\n"
df = df.replace({"ELECTRICITY ACCOUNTS":{"Less than 4":2}})

badCols = ('COMMUNITY AREA NAME','BUILDING TYPE','BUILDING_SUBTYPE')

for colName in badCols:
    print "binifying %s..." % colName
    df = binifyCol(df,colName)

print "writing to ./Energy_Usage_2010.preprocessed.csv..."
df.to_csv('Energy_Usage_2010.preprocessed.csv')
