"""import csv
import pandas
import statistics
# import numpy as np

#with open("weather_data.csv", "r") as data_file:
#    data = data_file.readlines()
#    print(data)

with open("weather_data.csv", "r") as data_file:
    data = csv.reader(data_file)
    print(data)
    temperatures = []
    for row in data:
        if row[1] != "temp": #  this excludes the heder of the file and appends the remaining data to be able to convert it into a int
            temperatures.append(int(row[1])) 
    print(temperatures)

# How to read a file in pandas
data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()
#print(data["temp"])
#print(data_dict)

temp_list = data["temp"].to_list()
#  average_temp = np.mean(temp_list) Numpy solution
average_temp = data["temp"].mean() # Pandas solution
max_value = data["temp"].max()
print(temp_list)
print(average_temp)
print(max_value)
#GET DATA IN COLUMNS
#You can print data in python either way, by accesing it as an attribute or as a list
#print(data.condition)
#print(data["condition"])
# GET DATA IN ROW
#print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)
monday_temp = monday.temp[0]
farenheit_temp_monday = monday_temp * (9/5) + 32
print(farenheit_temp_monday)

# CREATE A DATAFRAME FROM SCRATCH

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv") """
import pandas

# CHALLENGE -> Fur, Color, Count generate a csv with the fur, color and the sum of count grouped by color

"""My solution
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250214.csv")
#GROUP THE COLUMNS BY THE PRIMARY FUR COLOR
fur_grouped = data.groupby('Primary Fur Color')
#COUNT THE GROUPED COLUMNS BY THE UNIQUE SQUIRREL ID
fur_count = fur_grouped.count().reset_index()[["Primary Fur Color", "Unique Squirrel ID"]]
# RENAME THE COLUMNS THAT DON'T HAVE THE PROPER NAME
fur_count = fur_count.rename(columns={"Unique Squirrel ID": "Count"})
fur_count = fur_count.rename(columns={"Primary Fur Color": "Fur Color"})
# SAVE TO A CSV FILE
fur_count.to_csv("fur_count.csv")"""

"""Angela's solution
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")


"""






