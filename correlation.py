import csv
import plotly.express as px
import numpy as np
MarksInPercentage=[]
DaysPresent=[]
with open('Data.csv') as f:
    reader = csv.DictReader(f)
    for i in reader:
        MarksInPercentage.append(float(i["MarksInPercentage)"]))
        Time.append(float(i["DaysPresent"]))
correlation=np.corrcoef(MarksInPercentage,DaysPresent)
print(correlation)