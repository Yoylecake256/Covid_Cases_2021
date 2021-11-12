import pandas as pd
import plotly.express as px
import csv
import math

with open('data.csv', newline='')as a:
    reader= csv.reader(a)
    file_data= list(reader)
    
    print(file_data)
    
file_data.pop(0)

totalcases = 0
totalcountries = len(file_data)

for cases in file_data:
    totalcases += float(cases[1])
    
print(totalcases)

mean = totalcases/totalcountries
print("The mean is: " + str(mean))

df = pd.read_csv("data.csv")
fig = px.histogram(df, x="country", y="cases")

fig.show()