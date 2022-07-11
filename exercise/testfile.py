#
#
# # Question:
# # A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# #
# # Following are the criteria for checking the password:
# #
# # At least 1 letter between [a-z]
# # At least 1 number between [0-9]
# # At least 1 letter between [A-Z]
# # At least 1 character from [$#@]
# # Minimum length of transaction password: 6
# # Maximum length of transaction password: 12
# # Your program should accept a sequence of comma separated passwords and
# # will check them according to the above criteria. Passwords that match the criteria
# # are to be printed, each separated by a comma.
# #
# # Example
# #
# # If the following passwords are given as input to the program:
# #
# # ABd1234@1,a F1#,2w3E*,2We3345, Jk3@hj
# # Then, the output of the program should be:
# #
# # ABd1234@1
#
# import re
#
# input_data = input("Enter various types of passwords: ")
# input_list = input_data.split(",")
# print(input_list)
#
# def checkpwd(passwrd):
#     cnt = 0
#     #check for length
#     cnt += (len(passwrd) >=6 and len(passwrd) <=12)
#     #check for alphabets
#     cnt += bool(re.search("[a-z]",passwrd))
#     cnt += bool(re.search("[A-Z]", passwrd))
#     #check for numbers
#     cnt += bool(re.search("[0-9]", passwrd))
#     #check for spl char
#     cnt += bool(re.search("[$#@]", passwrd))
#     return cnt
#
#
# output_list = []
#
# for pwd in input_list:
#     #check password
#     #append if it meets all req
#     if checkpwd(pwd) == 5:
#         output_list.append(pwd)
#
# print(",".join(output_list))



# # Question:
# # You are required to write a program to sort the (name, age, score) tuples by
# # ascending order where name is string, age and score are numbers.
# # The tuples are input by console. The sort criteria is:
# #
# # 1: Sort based on name
# # 2: Then sort based on age
# # 3: Then sort by score
# # The priority is that name > age > score.
# #
# # If the following tuples are given as input to the program:
# #
# # Tom,19,80
# # John,20,90
# # Jony,17,91
# # Jony,17,93
# # Json,21,85
#
# # Then, the output of the program should be:
# #
# # [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
#
# lst = []
# while True:
#     s = input().split(',')
#     if not s[0]:                          # breaks for blank input
#         break
#     lst.append(tuple(s))
#
# print(lst)
#
# lst.sort(key=lambda x:(x[0],int(x[1]),int(x[2])))  # here key is defined by lambda and the data is sorted by element priority 0>1>2 in accending order
# print(lst)
# # lst.sort(key=lambda x:(x[0],int(x[1]),int(x[2])))
# # print(lst)


# # Question:
# # Define a class with a generator which can iterate the numbers,
# # which are divisible by 7, between a given range 0 and n.
# #
# # Suppose the following input is supplied to the program:
# #
# # 7
# # Then, the output should be:
# #
# # 0
# # 7
# # 14
#
# class divby7:
#     def by_seven(self,n):
#         #get the number and find the range
#         num = int(n/7) + 1
#         for i in range(0 , num):
#             yield i*7
#
#
# objdiv = divby7()
# n = int(input("Enter a number : "))
#
# for j in objdiv.by_seven(n):
#     print(j)
#


# # Question:
# # A robot moves in a plane starting from the original point (0,0). The robot can move toward UP,
# # DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
# #
# # UP 5
# # DOWN 3
# # LEFT 3
# # RIGHT 2
# # The numbers after the direction are steps. Please write a program to compute the distance from
# # current position after a sequence of movement and original point. If the distance is a float,
# # then just print the nearest integer. Example: If the following tuples are given as input to the program:
# #
# # UP 5
# # DOWN 3
# # LEFT 3
# # RIGHT 2
# # Then, the output of the program should be:
# #
# # 2
#
#
# import math
#
# x = 0
# y = 0
# #get the input and move the turtle
# while True:
#     #get the input
#     input_data = input("Enter the movement : ").strip()
#     if input_data == "" :
#         break
#     input_list = input_data.split(" ")
#     #get the x and y coor
#     if input_list[0].upper() == "UP" :
#         x += int(input_list[1])
#     if input_list[0].upper() == "DOWN" :
#         x -= int(input_list[1])
#     if input_list[0].upper() == "LEFT" :
#         y -= int(input_list[1])
#     if input_list[0].upper() == "RIGHT" :
#         y += int(input_list[1])
#
# tmp = (x**2) + (y**2)
# area = round(math.sqrt(tmp))
#
# print(area)
#


# # Question:
# # Write a program to compute the frequency of the words from the input.
# # The output should output after sorting the key alphanumerically.
# #
# # Suppose the following input is supplied to the program:
# #
# # New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# # Then, the output should be:
# #
# # 2:2
# # 3.:1
# # 3?:1
# # New:1
# # Python:5
# # Read:1
# # and:1
# # between:1
# # choosing:1
# # or:2
# # to:1
#
# input_data = input("Enter a string: ").split()
# input_set = sorted(set(input_data))
# for wrd in input_set:
#     n = input_data.count(wrd)
#     print(f"{wrd} : {n}")
#
# # ss = input().split()
# # word = sorted(set(ss))     # split words are stored and sorted as a set
# #
# # for i in word:
# #     print("{0}:{1}".format(i,ss.count(i)))


# # Question 24
# # Question:
# # Python has many built-in functions, and if you do not know how to use it, you can read document
# # online or find some books. But Python has a built-in document function for every built-in functions.
# #
# # Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
# #
# # And add document for your own function
# #
# # Hints:
# # The built-in document method is __doc__
#
# # print(abs.__doc__)
# # print(int.__doc__)
#
# def square(n):
#     '''
#     This is a function for getting a square of a integer number
#     It returns the square of the given number
#     '''
#     return n**2
#
# print(square(5))
# print(square.__doc__)

# # Define a class, which have a class parameter and have a same instance parameter.
#
# class NewClass():
#     name = "My class"
#
#     def __init__(self, nam):
#         self.name = nam
#         print(f"Hello ! {self.name}")
#
#     def say_hello(self):
#         print("This is a hello from my class")
#
#
#
# myclass = NewClass("Saku")
# myclass.say_hello()

# # Define a function that can accept two strings as input and print the string with maximum length in console.
# # If two strings have the same length, then the function should print all strings line by line.
#
# def str_max_length(str1,str2):
#     if len(str1) > len(str2) :
#         print(f"Longest string is {str1} and length is {len(str1)}")
#     elif len(str1) < len(str2) :
#         print(f"Longest string is {str2} and length is {len(str2)}")
#     else:
#         print(f"strings are equal in length and length is {len(str1)}")
#         print(f"{str1}")
#         print(f"{str2}")
#
# str_max_length("This is trial", "This is example")
# str_max_length("This is Sample of data", "This is example")
# str_max_length("This is nice", "This is good")


# # Define a function which can print a dictionary where the keys are numbers between 1 and 20
# # (both included) and the values are square of keys.
#
# def dict_square():
#     dict = {i:i**2 for i in range(1,21)}
#     print(dict)
#
# dict_square()
#


# # Define a function which can generate a dictionary where the keys are numbers between 1 and 20
# # (both included) and the values are square of keys. The function should just print the keys only.
# def dict_square():
#     dict = {i:i**2 for i in range(1,21)}
#     return dict
#
# # def print_key():
# #     pdict = dict_square()
# #     for i in pdict:
# #         print(i)
#
# # print_key()

# d = dict_square()
# print(d.keys())

# # Define a function which can generate and print a list where the values are square
# # of numbers between 1 and 20 (both included).
# def square_list():
#     list_values = [i**2 for i in range(0,21)]
#     print(list_values)
#
# square_list()

# # Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
# # Then the function needs to print the first 5 elements in the list.
#
# def square_list():
#     list_values = [i**2 for i in range(0,21)]
#     return list_values
#
# def print_list(n):
#     li = square_list()
#     # if len(li) < n:
#     #     n = len(li)
#     # for i in range(0,n):
#     #     print(li[i])
#     print(li[:5])
# print_list(25)


# # Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
# # Then the function needs to print the last 5 elements in the list.
#
# def square_list():
#     list_values = [i**2 for i in range(0,21)]
#     # print(list_values[16:21:1])
#     print(list_values[-5:])
#
# square_list()


# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
# Then the function needs to print all values except the first 5 elements in the list.
# def square_list():
#     list_values = [i**2 for i in range(0,21)]
#     # print(list_values[16:21:1])
#     print(list_values[5:])
#
# square_list()
#


# Define a function which can generate and print a tuple where the value are square of numbers between 1
# and 20 (both included).



def square_list():
    list_values = [i**2 for i in range(0,21)]
    # print(list_values[16:21:1])
    print(tuple(list_values))

square_list()