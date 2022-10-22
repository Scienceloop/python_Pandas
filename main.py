import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_sqirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_sqirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_sqirrel_count = len(data[data["Primary Fur Color"] == "Black"])


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_sqirrel_count, red_sqirrel_count, black_sqirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_count.csv")