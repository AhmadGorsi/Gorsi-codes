import requests

#  1. Data Types & Variables:
#    - Create variables for: name (string), age (int), is_student (bool), marks (list of 5 integers).
#    - Print their types using type().
#  2. Conditional Logic:
#    - Ask user for a number. If even and divisible by 4: print 'Special Even Number'. If even: print 'Even'. Else: print 'Odd'.
#  3. Loops & Strings:
#    - Print all vowels from a given string input. Reverse string without slicing.
#  4. Functions:
#    - Write calculate_grade(marks: list) that returns A/B/C/Fail based on average.
#  5. Dictionary Processing:
#    - Given {"Ali":[85,90,92],"Sara":[70,75,80],"Zain":[95,88,91]}, print student with highest avg.
#  6. JSON Task:
#    - Save dictionary as JSON file and reload to print students with avg > 80.
#  7. API Call:
#    - Call any public API (e.g., randomuser.me) using requests and store specific fields in JSON file.
#  8. NumPy Array Operations:
#    - Create array of 10 random integers (1-100). Compute mean, std, reshape to (2,5), multiply by 2.
#  9. Mini Project – Student Report System:
#    - Input N students (name + 3 marks). Save to JSON. Use NumPy to find class averages and topper



# name = 'Ahmad'
# age = int('7')
# is_student = ''
# list = [ '77','56','88','34','23']
   

# print(type(name))
# print(type(age))
# print(type(list))
# print(type(is_student))


# Second Task 


# user = int(input('Enter Your Number:'))

# if user % 4 == 0:
#     print('Sep Even Number')
# elif user % 2 == 0:
#     print('yes it is even')
# else:
#     print('odd')
# print(user)


# 3rd Task 

# vowels = str(input('Enter Your Alphabets'))
# if vowels == 'a,b,c,d,e,f,g':
#     print('yes right')
# elif vowels == 'a,e,i,o,u':
#     print('hdi')
# else:
#     print('wrong')


# 4th tasks 

# grade = int(input('enter your number kindly'))

# if grade >= 90:
#     print('You got A')
# elif grade >= 80:
#     print('You got B')
# elif grade >= 60:
#     print('You got C')
# else:
#      print('fail')

# # 5th Tasks

# {"Ali":[85,90,92],"Sara":[70,75,80],"Zain":[95,88,91]},  




# 6th task



dictionary = {"Ali":[85,90,92],"Sara":[70,75,80],"Zain":[95,88,91]},  

response = requests.get(dictionary)

data = response.json()

print("data",data)




# 7th tasks 

# import requests

# url = "https://superheroapi.com/api/access-token/"

# response = requests.get(url)

# data = response.json()

# print("data",data)

# 8th tasks 



# random = [

# ]












