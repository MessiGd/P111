import statistics
import random
import csv
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go 

read = pd.read_csv("data.csv")
data = read["reading_time"].tolist()

fig = ff.create_distplot([data],["reading time"], show_hist= False)
fig.show()

mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)
std0 = statistics.stdev(data)

print("Mean of raw data:", mean)
print("Mode of raw data", mode)
print("Median of raw data:", median)
print("Standard Deviation of raw data:", std0)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0,100):
    set_of_means = random_set_of_mean(30)
    mean_list.append(set_of_means)

mean = statistics.mean(mean_list)
std = statistics.stdev(mean_list)

print("Mean of sampling distribution:", mean)
print("Standard Deviation of sampling distribution:", std)

fig = ff.create_distplot([mean_list],["students marks"], show_hist= False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.20], mode = "lines", name = "mean of sampling data"))
fig.show()

first_standarddeviation_start, first_standarddeviation_end = mean - std, mean + std
second_standarddeviation_start, second_standarddeviation_end = mean - (2*std), mean + (2*std)
third_standarddeviation_start, third_standarddeviation_end = mean - (3*std), mean + (3*std)

fig = ff.create_distplot([mean_list], ["reading_ time"], show_hist=False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0,1.20], mode = "lines", name = "mean of sampling data"))
fig.add_trace(go.Scatter(x = [first_standarddeviation_start, first_standarddeviation_start], y = [0,1.20],mode = "lines", name = "Standard Deviation 1"))
fig.add_trace(go.Scatter(x = [first_standarddeviation_end, first_standarddeviation_end], y = [0,1.20],mode = "lines", name = "Standard Deviation 1"))
fig.add_trace(go.Scatter(x = [second_standarddeviation_start, second_standarddeviation_start], y= [0,1.20],mode = "lines", name = "Standard Deviation 2"))
fig.add_trace(go.Scatter(x = [second_standarddeviation_end, second_standarddeviation_end], y = [0,1.20],mode = "lines", name = "Standard Deviation 2"))
fig.add_trace(go.Scatter(x = [third_standarddeviation_start, third_standarddeviation_start], y = [0,1.20],mode = "lines", name = "Standard Deviation 3"))
fig.add_trace(go.Scatter(x = [third_standarddeviation_end, third_standarddeviation_end], y = [0,1.20],mode = "lines", name = "Standard Deviation 3"))
fig.show()

a = pd.read_csv("data1.csv")
data = a["reading_time"].tolist()
mean_of_sample1 = statistics.mean(data)
print("Mean of sample 1:", mean_of_sample1)
fig = ff.create_distplot([mean_list], ["reading time"], show_hist= False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0,1.20], mode = "lines", name = "mean of sampling data"))
fig.add_trace(go.Scatter(x = [mean_of_sample1, mean_of_sample1], y = [0,1.20], mode = "lines", name = "mean of sample 1"))
fig.add_trace(go.Scatter(x = [first_standarddeviation_end, first_standarddeviation_end], y = [0,1.20],mode = "lines", name = "Standard Deviation 1"))
fig.show()

z_score = (mean - mean_of_sample1)/std0
print(z_score)
