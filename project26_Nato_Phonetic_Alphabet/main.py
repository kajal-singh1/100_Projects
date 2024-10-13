import pandas as pd

data = pd.read_csv("100_Projects/project26/nato_phonetic_alphabet.csv")
new_value = {row.letter:row.code for (index,row) in data.iterrows()}


word = input("Enter a word: ").upper()
output_list = [new_value[letter] for letter in word]
print(output_list)