import csv
import pandas as p
import random
import plotly.figure_factory as pff
import statistics

df = p.read_csv("data.csv")
data = df["average"].tolist()
tem_mean = statistics.mean(data)
tem_std_dev = statistics.stdev(data)
fig = pff.create_distplot([data],["average"],show_hist=False)
fig.show()
print("mean: ",tem_mean)
print("std_dev: ",tem_std_dev)