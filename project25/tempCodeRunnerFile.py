# with open ("C:/Users/AJAY/Documents/sau_code/angela yu/100_Projects/project25/weather_data.csv") as new_data:
#     data = new_data.readlines()
#     print(data)

import csv

with open("C:/Users/AJAY/Documents/sau_code/angela yu/100_Projects/project25/weather_data.csv") as data_files:
    data = csv.reader(data_files)
    temperature = []
    # temperature = csv.DictReader(data_files, delimiter = ',')
    # columns = list(temperature)
    # for column in columns:
    #     print(column['temp'])
    for row in data:
        if row[1] != 'temp':
            temperature.append(int(row[1]))
    print(temperature)
