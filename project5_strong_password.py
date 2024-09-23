#Creation of a strong password generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
n_letters = int(input("How many letters would you like in ypur password \n"))
n_symbols = int(input("How many symbols would you like? \n"))
n_numbers = int(input("How many numbers would you like? \n"))

passwrd = " "
for letter in range( 1 , n_letters+1):
    l = random.choice(letters)
    passwrd += l
for number in range( 1 , n_numbers+1):
    n = random.choice(numbers)
    passwrd += n
for symbol in range( 1 ,n_symbols+1):
    s = random.choice(symbols)
    passwrd += s
print('password = ',passwrd)



#Interactive Coding
#Q1 Average Height of the Student
# student_heights = input("Input a list of student heights\n").split()
# for n in range(0 , len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)
# sum = 0
# avg = 1
# for i in student_heights:
#     sum += i
# print(sum)
# for i in student_heights:
#     avg += 1
# print(avg-1)
# avg_height = sum / avg -1
# print(avg_height)

#Q2 Highest score
# student_scores = input("Input a list of student marks in a class\n ").split()
# for n in range(0 , len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)

# max = student_scores[0]
# for marks in student_scores:
#     if marks > max:
#         max = marks
# print(f"The highest score in the class is : {max}")

#addition of 1st 100 numbers
# sum = 0
# for number in range(1 , 101):
#     sum += number
# print("100 numbers addition = " , sum)

#adding evens exercise
# sum = 0
# for number in range(2 , 101 , 2):
#     sum += number
# print("100 numbers addition = " , sum)

#Fizz Buzz Exercise
# for number in range(1 , 101 ):
#     if number % 5 == 0 & number % 3 == 0:
#         print("fizzbuzz")
#     elif number % 5 == 0:
#         print("Buzz")
#     elif number % 3 == 0:
#         print("fizz")
#     else:
#         print(number)
    
