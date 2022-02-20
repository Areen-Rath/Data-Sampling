import random
import statistics
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv('medium_data.csv')
time = df["reading_time"].tolist()

population_mean = statistics.mean(time)
print(population_mean)

def find_sample_mean():
    dataset = []
    for i in range(0, 30):
        index = random.randint(0, len(time))
        value = time[index]
        dataset.append(value)

    sample_mean = statistics.mean(dataset)
    return sample_mean

def setup():
    global sample_mean_array
    sample_mean_array = []
    for i in range(0, 100):
        mean_array = find_sample_mean()
        sample_mean_array.append(mean_array)

    sample_mean_array_mean = statistics.mean(sample_mean_array)
    print(sample_mean_array_mean)

def plot_graph():
    data = sample_mean_array
    fig = ff.create_distplot([data], ["Reading Time"], show_hist = False)
    fig.show()

setup()
plot_graph()