#Project Caesar Cipher
import art_caesar_cipher
print(art_caesar_cipher.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text , shift , direction):
    end_text = ""
    if direction == "decode":
            shift *= -1
    for char in text:
        if char in  alphabet:
            position = alphabet.index(char)
            new_position = position +  shift
            end_text += alphabet[new_position]
        else:
             end_text += char
    print(f"The {direction}d text is {end_text}")

should_continue = True
while should_continue:  
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    caesar(text , shift , direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    if restart == "no":
         should_continue = False
         print("Good Bye")



         
#Interactive Coding
#Q1 Area Calculation
# import math
# def paint_cal(height , width , cover):
#     no_of_cans = math.ceil((height * width) / coverage)
#     print(f"you will need {no_of_cans} cans")

# test_h = int(input("Height of wall: "))
# test_w = int(input("width of wall: "))
# coverage = 5
      
# paint_cal(height = test_h , width = test_w , cover = coverage)

#Q2 Prime Number Checker
# def prime_checker(number):
#     is_prime = True
#     for i in range (2 , number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("it is a prime")
#     else:
#         print("it is not a prime")

# n = int(input("Check this number: "))
# prime_checker(number = n)