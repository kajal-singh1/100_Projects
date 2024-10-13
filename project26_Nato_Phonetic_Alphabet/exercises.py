#LIST COMPREHENSION
# Exercise1(Printing Squared numbers)
numbers = [1,1,2,3,5,8,13,21,34,55]

squared_numbers = [n*n for n in numbers]

print(squared_numbers)


# Exercise2(Printing only even numbers)
numbers = [1,1,2,3,5,8,13,21,34,55]

result = [n for n in numbers if n%2==0]

print(result)


# Exercise3(Printing common values from two text files)
import pandas as pd
file1 = pd.read_csv("100_Projects/project26/file1.txt")
file2 = pd.read_csv("100_Projects/project26/file2.txt")
a = file1.iloc[:, 0].to_list()
b = file2.iloc[:, 0].to_list()
print(a)
print(b)
result = [num for num in a if num in b]
print(result)


#DICTIONARY COMPREHENSION
#1 Finding the length of each words in a sentence
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {wrds:len(wrds) for wrds in  sentence.split()}
print(result)

#2 converting from celsius to farenheit
weather_c = {
    "Monday":12,
    "Tuesday":14,
    "Wednesday":15,
    "Thursday":14,
    "Friday":21,
    "Saturday":22,
    "Sunday":24,
}

weather_f = {day:(value*9/5)+32 for (day,value) in weather_c.items()}
print(weather_f)