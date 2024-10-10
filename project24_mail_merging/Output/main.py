PLACEHOLDER = "[name]"

with open("C:/Users/AJAY/Documents/sau_code/angela yu/100_Projects/project24_mail_merging/Input/Names/Invited_names.txt") as names_files:
    names = names_files.readlines()
    print(names)

with open("C:/Users/AJAY/Documents/sau_code/angela yu/100_Projects/project24_mail_merging/Input/Letter/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        # print(new_letter)
        with open(f"C:/Users/AJAY/Documents/sau_code/angela yu/100_Projects/project24_mail_merging/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

