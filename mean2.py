import csv
import pandas as p
import random
import plotly.figure_factory as pff
import statistics

df = p.read_csv("data.csv")
data = df["publication"].tolist()

def random_set_of_mean(counter):
    dataset = []
    for i in range((counter)):
        random_Index = random.randint(0, len(data)-1)
        value = data[random_Index]
        dataset.append(value)
    tem_mean = statistics.mean(data)
    return tem_mean

def show_Figure(mean_list):
    df = mean_list
    fig = pff.create_distplot([df],["publication"],show_hist=False)
    fig.show()

def set_up():
    mean_list = []
    for i in range(0,100):
        set_of_mean = random_set_of_mean(100)
        mean_list.append(set_of_mean)
    show_Figure(mean_list)

set_up()