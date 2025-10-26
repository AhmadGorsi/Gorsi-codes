# basic tasks 
# 1:Even or Odd 
# num = int(input('Enter Your Number'))
# if num % 2 ==0:
#     print('Even Number')
# else:
#     print('Odd Number')  

# 2: Positive, Ngative, or Zero 

# num = int(input('Enter Your Number'))
# if num > 0:
#     print('Positive Number')
# elif num < 0:
#     print('Ngative Number')
# else:
#     print('Zero')

# 3:Simple login check 

# password = 'python123'

# user = input('ENter Your Password:')
# if password == user:
#     print('Access Granted')
# else:
#     print('Access Denied')

# MEDIUM LEVEL TASKS

# 4:Basic Calculator with conditons 

# num1 = int(input('Enter Your First Number:'))
# numm2 = int(input('Enter Your Secnod Number:'))
# opreter = (input('Enter Your Opreter:'))

# if opreter == '+':
#     print("Result:", num1 + numm2)
# elif opreter =='-':
#     print("Result:", num1 - numm2)
# elif opreter == '*':
#     print('Result:', num1 * numm2)   
# elif opreter == '/':
#     if numm2 != 0:
#         print("Result:", num1 / numm2)
#     else:
#         print(" Division Error")
# else:
#     print('Math Error')         

# 5: Age Category Finder 

# userage = int(input('Enter Your Age:'))
# if userage < 13:
#     print('Child')
# elif  13 <= userage <= 19:
#     print('Teenager')
# elif 20 <= userage <= 59:
#     print('Adult')
# else:
#     print('Senior')

# 6: Number Guessing Game

# secretnum = 7
# usernum = int(input('Enter Your Secret NUmber:'))
# while usernum != secretnum:
#     print("Wrong guess, try again!")
#     usernum = int(input('Enter Your Secret NUmber Again:'))
# print('Correct')

# TOUGH TASKS 

# c_username = 'gorsi'
# c_password = 'gorsi123'
# attempts = 3

# while attempts > 0:
#     username = input("Enter username: ")
#     password = input("Enter password: ")
#     if c_username == username and c_password == password:
#         print("Welcome")
#         break
#     else:
#         attempts -= 1
#         print("Incorrect Attempts left:", attempts)
# if attempts == 0:
#     print("Account Locked")

# 8: Menu Driven Atm

# c_id = "gorsi"
# c_password = "125"
# attempts = 3
# while attempts > 0:
#     username = input("Enter Id: ")
#     password = input("Enter password: ")

#     if username == c_id and password == c_password:
#         print("Welcome!")
#         break
#     else:
#         attempts -= 1
#         print("Incorrect, Attempts left:", attempts)
# if attempts == 0:
#     print("Account Locked")

# 9: Password Strength Checker
















# 10: Password Strength Checker
password = input("Enter your pasSword: ")
number = False
upper = False
for char in password:
    if char.isdigit():
        number = True
    if char.isupper():
        upper = True
if len(password) >= 8 and number and upper:
    print("Strong Password")
else:
    print("Weak Password")
