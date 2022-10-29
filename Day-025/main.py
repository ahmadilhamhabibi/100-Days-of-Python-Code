# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
""" print type table and column """
# print(type(data))
# print(type(data["temp"]))

"""Convert data to dictionary and list"""
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)

"""Get Mean and MAX"""
# print(data["temp"].mean())
# print(data["temp"].max())

"""Get data in columns"""
# print(data["condition"])
# print(data.condition)

"""Get data in row"""
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9 / 5 + 32
# print(monday_temp_F)

"""Create a dataframe from stratch"""
data_dict = {
    "student": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")