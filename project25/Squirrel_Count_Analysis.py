import pandas

data = pandas.read_csv("C:/Users/AJAY/Documents/sau_code/angela yu/100_Projects/project25/Squirrel_data.csv")

grey = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])


print(grey)
print(cinnamon)
print(black)

data_dict = {
    "fur_color" : ["Grey", "Black", "Cinnamon"],
    "count":[grey,cinnamon,black],
}
data = pandas.DataFrame(data_dict)
data.to_csv("Squirrel_Count.csv")
print(data)