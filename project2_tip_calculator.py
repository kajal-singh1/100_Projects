print("Welcome to the tip calculator")
Bill = int(input("What was the total bill?"))
Number_of_ppl = int(input("How many people to split? "))
percentage = int(input("What percentage tip would like to give? 10 , 12, , or 15"))
total_bill = (Bill * (percentage/100)) + Bill
bill_per_person = total_bill/Number_of_ppl
print("Each person should pay:" , bill_per_person)






#Intiractive Coding
# user_input = (input("Enter the number ="))
# digit_1st = user_input[0] 
# digit_2nd = user_input[1]
# add = int(digit_1st) + int(digit_2nd)
# print(f"Final Result = {add}" )

# #BMI Calculator Exercise
# weight = float(input("Enter the weight = "))
# height = float(input("Enter the height = "))
# BMI = weight / height **2
# BMI_int = int(BMI)
# print("BMI = " , BMI_int)

# #Life in weeks exercise
# age = int(input("Enter your age = "))
# leftyears = (90 - age )  
# months = leftyears * 12
# weeks = leftyears * 52
# days = leftyears *  365

# print(f"you have {days} days ,{weeks} weeks, {months} months left ")

