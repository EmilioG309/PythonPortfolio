#Data Leak Stats
#Initialize
import pandas as pd

data = pd.read_csv('hacker.csv')
id = data['Log_ID'].tolist()
ip = data['IP_Address'].tolist()
kb = data['Data_KB'].tolist()
time = data['Time'].tolist()
description = data['Description'].tolist()
filter = []

#Functions
def login(notes):
    for i in range(len(description)):
        if notes in description[i] :
            filter.append([i])
    print(filter)
    filter.clear()

def leak(amount):
    for i in range(len(kb)):
        if kb[i] > amount:
            filter.append([i])
    print(filter)
    filter.clear()

def password(change):
    for i in range(len(description)):
        if change in description[i] :
            filter.append([i])
    print(filter)
    filter.clear()

#Main
#Problem One
login("Failed")
print(data.loc[[193,194,195]])
#Problem Two
leak(2000)
print(data.loc[[199]])
#Problem Three
password("Reset")
print(data.loc[[204,205,207,210,214,218,221,222,224,231,235]])
