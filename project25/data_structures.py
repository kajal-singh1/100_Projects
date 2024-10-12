# code for converting a csv file into a list
with open ("C:/Users/AJAY/Documents/sau_code/angela yu/100_Projects/project25/weather_data.csv") as new_data:
    data = new_data.readlines()
    print(data)


#code for accessing the column from the csv file by importing csv
import csv
with open("C:/Users/AJAY/Documents/sau_code/angela yu/100_Projects/project25/weather_data.csv") as data_files:
    data = csv.reader(data_files)
    temperature = []
    for row in data:
        if row[1] != 'temp':
            temperature.append(int(row[1]))
    print(temperature)



import pandas

data = pandas.read_csv("C:/Users/AJAY/Documents/sau_code/angela yu/100_Projects/project25/weather_data.csv")
temp_list = data["temp"].to_list()

#calculating average using usual method
avg = sum(temp_list)/len(temp_list)
print(round(avg))

#calculating average using series method
print(data["temp"].mean())

#converting from celsius to farenheit
monday = data[data.day == "Monday"]
print((monday.temp*1.8)+32)
    
#creating a dataframe from scratch
data_dict = {
    "students" : ["Anni", "Sufiya", "Riya"],
    "scores":[45,56,72],
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
print(data)