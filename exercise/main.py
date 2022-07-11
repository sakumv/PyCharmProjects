# # Write a program which will find all such numbers which
# # are divisible by 7 but are not a multiple of 5, between 2000
# # and 3200 (both included).The numbers obtained should be printed
# # in a comma-separated sequence on a single line.
#
# #Answer
# #------
# result = ""
# for i in range(2000,3201):
#     if i % 7 == 0 and i % 5 != 0:
#         result += str(i) + ", "
#
# print (result)
#
# result =[str(i) for i in range(2000,3201) if (i % 7 == 0 and i % 5 != 0)]
# print(", ".join(result))

# Write a program which can compute the factorial of a given numbers.The results should be printed
# in a comma-separated sequence on a single line.Suppose the following input is
# supplied to the program: 8 Then, the output should be:40320

# import math
#
# fact = input("Enter a number :")
# fact = int(fact)
#
# factorial = math.factorial(fact)
# print (factorial)
#
#
# input_data = input("Enter the numbers for finding factorial separated by ,: ")
# input_data = input_data.strip()
# input_list = input_data.split(",")
#
# output_list = [str(math.factorial(int(i))) for i in input_list]
#
# print(",".join(output_list))
#


# With a given integral number n, write a program to generate a dictionary
# that contains (i, i x i) such that is an integral number between 1 and n (both included).
# and then the program should print the dictionary.Suppose the following input is supplied
# to the program: 8

# Then, the output should be:

# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

# def add_dic(dic,key,value):
#     dic[key] = value
#
# input_value = int(input("Enter the number : "))
#
# # output_dic = {}
# # i=1
# # while i <= input_value:
# #     add_dic(output_dic,i,i*i)
# #     i += 1
# #
# # print (output_dic)
#
# output_dic={key:key*key for key in range(1,input_value+1)}
# print (output_dic)
#
# # Question:
# # Write a program which accepts a sequence of comma-separated numbers from console
# # and generate a list and a tuple which contains every number.Suppose the
# # following input is supplied to the program:
# #
# # 34,67,55,33,12,98
# # Then, the output should be:
# #
# # ['34', '67', '55', '33', '12', '98']
# # ('34', '67', '55', '33', '12', '98')
#
# input_string = input("Enter numbers with , separated:- ")
# #remove apaces if it is there
# input_string = input_string.strip()
# input_list = input_string.split(",")
# print (input_list)
# #test_str.split(', ')
# #(int, )
# #output_list = tuple(map(int,input_string.split(","))) # to show  numbers in tuple
# output_list = tuple(input_string.split(","))
# #output_list = eval(input_string)
# print(output_list)


# Question:
# Define a class which has at least two methods:
#
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
#
# Hints:
# Use init method to construct some parameters
#

# class test:
#     def __init__(self):
#         self.input_string = ""
#
#     def getString(self):
#         self.input_string = input("Enter a Srting: ")
#
#     def printString(self):
#         print(self.input_string.upper())
#
#
# #create the object
# obj = test()
# obj.getString()
# obj.printString()


# # Question:
# # Write a program that calculates and prints the value according to the given formula:
# #
# # Q = Square root of [(2 _ C _ D)/H]
# #
# # Following are the fixed values of C and H:
# #
# # C is 50. H is 30.
# #
# # D is the variable whose values should be input to your program in a comma-separated
# # sequence.For example Let us assume the following comma separated input sequence is
# # given to the program:
# #
# # 100,150,180
# # The output of the program should be:
# #
# # 18,22,24
# import math
#
# C = 50
# H = 30
#
# input_value = input("Enter values , separated : ").strip()
# input_list = list(eval(input_value))
# #input_value.split(",")
# print (input_list)
# #output_list = [math.sqrt((2*C*i)/H)  for i in input_list]
# output_list = [str(int(math.sqrt((2*C*i)/H)))  for i in input_list]
# #print(output_list)
# print(",".join(output_list))


# # _Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# # The element value in the i-th row and j-th column of the array should be i _ j.*
# #
# # Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5
# #
# # Then, the output of the program should be:
# #
# # [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
#
# #get the inputs
# x = int(input("Enter x: "))
# y = int(input("Enter y: "))
#
# out_list = []
# tmp_list = []
# for i in range(x):
#     tmp_list.clear()
#     for j in range(y):
#         tmp_list.append(i*j)
#     out_list.extend(tmp_list)
# print(out_list)
#
# # output = [[j*i for j in range(y)] for i in range(x)]
# # print(output)


# # Question:
# # Write a program that accepts a comma separated sequence of words as input and prints
# # the words in a comma-separated sequence after sorting them alphabetically.
# #
# # Suppose the following input is supplied to the program:
# #
# # without,hello,bag,world
# # Then, the output should be:
# #
# # bag,hello,without,world
#
# input_string = input("Enter a string with , separated words :").strip()
# input_list = input_string.split(",")
# output = sorted(input_list)
# output = ",".join(output)
# print(output)
#
#


# # Write a program that accepts sequence of lines as input and prints the lines
# # after making all characters in the sentence capitalized.
# #
# # Suppose the following input is supplied to the program:
# #
# # Hello world
# # Practice makes perfect
# # Then, the output should be:
# #
# # HELLO WORLD
# # PRACTICE MAKES PERFECT
# # input_text = input("Enter sentences :")
# # input_text = input_text.upper()
# # print(input_text)
# lst = []
# while True:
#     s = input()
#     if len(s) > 0:
#         lst.append(s.upper())
#     else:
#         break
#
# for line in lst:
#     print(line)


# # Question
# # Write a program that accepts a sequence of whitespace separated
# # words as input and prints the words after removing all duplicate
# # words and sorting them alphanumerically.
# #
# # Suppose the following input is supplied to the program:
# #
# # hello world and practice makes perfect and hello world again
# # Then, the output should be:
# #
# # again and hello makes perfect practice world
#
#
# tmp = []
# lst = []
# while True:
#     input_string = input().strip()
#     tmp.clear()
#     if len(input_string) > 0:
#         tmp = input_string.split()
#         for word in tmp:
#             if word not in lst:
#                 lst.append(word)
#     else:
#         break
#
# lst = sorted(lst)
#
# print(" ".join(lst))


# # Question 11
# # Question
# # Write a program which accepts a sequence of comma separated 4
# # digit binary numbers as its input and then check whether they are
# # divisible by 5 or not. The numbers that are divisible by 5 are to be printed
# # in a comma separated sequence.
# #
# # Example:
# #
# # 0100,0011,1010,1001
# # Then the output should be:
# #
# # 1010
# # Notes: Assume the data is input by console.
#
# input_data = input("Enter binary numbers : ")
# input_list = input_data.split(",")
# #print (input_list)
# #convert to a base 10 number
# output_list = [value for value in input_list if int(value,2) % 5 == 0]
# print(",".join(output_list))

# # Question:
# # Write a program, which will find all such numbers between 1000 and 3000 (both included)
# # such that each digit of the number is an even number.The numbers obtained should be printed
# # in a comma-separated sequence on a single line.
#
# #get the number and check the digits
# input_string = "1000"
# output_data = []
#
# output_list = []
#
# for numb in range(1000,3001):
#     output_list.clear()
#     input_string = str(numb)
#     digit_list = list(input_string)
#     output_list = [i for i in digit_list if int(i) % 2 ==0]
#     if len(output_list) == 4:
#         print(output_list)
#         output_data.append("".join(output_list))
#
# print(", ".join(output_data))


# # Question:
# # Write a program that accepts a sentence and calculate the number of letters and digits.
# #
# # Suppose the following input is supplied to the program:
# #
# # hello world! 123
# # Then, the output should be:
# #
# # LETTERS 10
# # DIGITS 3
#
#
# num_letters = 0
# num_digits = 0
# input_data = input("Enter a sentence : ")
# for letter in input_data:
#     #check if it is a alphabet
#     if letter.isalpha() == True:
#         num_letters += 1
#     #check if it a number
#     elif letter.isdigit()==True:
#         num_digits += 1
#
# print(f"LETTERS : {num_letters}")
# print(f"DIGITS : {num_digits}")
#


# # Question:
# # Write a program that accepts a sentence and calculate the number of upper case letters
# # and lower case letters.
# #
# # Suppose the following input is supplied to the program:
# #
# # Hello world!
# # Then, the output should be:
# #
# # UPPER CASE 1
# # LOWER CASE 9
#
# upper_case = 0
# lower_case = 0
# input_data = input("Enter a string: ")
# for letter in input_data:
#     if letter.isupper() :
#         upper_case += 1
#     elif letter.islower():
#         lower_case += 1
#
# print(f"UPPER CASE : {upper_case}")
# print(f"LOWER CASE : {lower_case}")


# # Question:
# # Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# #
# # Suppose the following input is supplied to the program:
# #
# # 9
# # Then, the output should be:
# #
# # 11106
#
# a = int(input("Enter a number (1-9): "))
# tmp_list = []
# tmp_var = ""
# x = 0
# for i in range(0,4):
#     tmp_var += str(a)
#     tmp_list.append(tmp_var)
#     x += int(tmp_var)
#
# # for var in tmp_list:
# #     x += int(var)
#
# print(tmp_list)
# print(x)


# # Question:
# # Use a list comprehension to square each odd number in a list.
# # The list is input by a sequence of comma-separated numbers. >
# # Suppose the following input is supplied to the program:
# #
# # 1,2,3,4,5,6,7,8,9
# # Then, the output should be:
# #
# # 1,9,25,49,81
#
# input_list = [1,2,3,4,5,6,7,8,9]
# output_list = [str(val*val) for val in input_list if val %2 != 0]
# print(",".join(output_list))

# Write a program that computes the net amount of a bank account based a transaction
# log from console input. The transaction log format is shown as following:
#
# D 100
# W 200
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
#
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
#
500

total_deposit = 0
total_withdrawal = 0
total = 0

while True:
    input_data = input("Enter the Code(D/W) & Amount: ")
    if len(input_data) > 0:
        tmp_list = input_data.split(" ")
        if (tmp_list[0] == "D"):
            total_deposit += int(tmp_list[1])
        else:
            total_withdrawal += int(tmp_list[1])
    else:
        break

total = total_deposit - total_withdrawal
print(f"Total : {total}")