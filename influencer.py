#Media Stats
#Initialize
import pandas as pd

data = pd.read_csv('influencer.csv')
month = data['Month'].tolist()
views = data['Views'].tolist()
dislikes = data['Dislikes'].tolist()
subs = data['Subscriber(+-)'].tolist()
revenue = data['Revenue'].tolist()
filter = []

#Functions
def viewer_count(amount):
    for i in range(len(views)):
        if views[i] < amount:
            filter.append([i])
    print(filter)
    filter.clear()

def sub_growth(increase):
    for i in range(len(subs)):
        if subs[i] > increase:
            filter.append([i])
    print(filter)
    filter.clear()

def rev_loss(profit):
    for i in range(len(revenue)):
        if revenue[i] < profit:
            filter.append([i])
    print(filter)
    filter.clear()

#Main
#First Problem
viewer_count(2000)
print(data.loc[[0,1,2,3,4,5,6,7,8,9,10]])
#Second Problem
sub_growth(50000)
print(data.loc[[64,65,66,67,68,69,70,71,72]])
#Third Problem
rev_loss(1)
print(data.loc[[98,107]])
