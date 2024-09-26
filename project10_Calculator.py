#Calculator

from art_calculator import logo
def add(n1 , n2):
    return n1 + n2

def sub(n1 , n2):
    return n1 - n2

def mul(n1 , n2):
    return n1 * n2

def div(n1 , n2):
    return n1 / n2

operations = {'+' : add,
             '-' : sub,
             '*' : mul,
             '/' : div}

def calculator():
    print(logo)
    num1 = float(input("what's the first number?: "))
    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("what's the next number?: "))
        calculation_fn = operations[operation_symbol]
        answer = calculation_fn(num1 , num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if  input(f"Type 'y' to continue calculating with {answer} , or type 'n' for new calculation. ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()

# def format_name(f_name , l_name):
#     print(f_name.title())
#     print(l_name.title())
# format_name("kgu" , "singh")

#interactive coding
#Q1days in the month

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return  True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# def days_in_month(year , month):
#     '''This will function will provide the year and month '''
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if month == 2 and  is_leap(year) :
#         return 29
#     return month_days[month - 1]
# year = int(input("Enter a year: "))
# month = int(input("Enter the month: "))
# days = days_in_month(year , month)
# print(days)