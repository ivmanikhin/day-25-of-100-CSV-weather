import pandas
# import csv
#
# with open('weather-data.csv') as file:
#     data = csv.reader(file)
#     next(data)
#     temperatures = []
#     for row in data:
#         temperatures.append(int(row[1]))
#     print(temperatures)

data = pandas.read_csv('weather-data.csv')
# temperatures = data.temp.to_list()
# average_temp = data.temp.mean()
# max_temp = data.temp.max()
# print("%.2f" % average_temp)
# print(max_temp)
monday = data[data.day == 'Monday']
monday_temp_F = int(monday.temp) * 1.8 + 32
print(monday_temp_F)
