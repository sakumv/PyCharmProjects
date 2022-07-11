student_dic = {
    "student" : ['Angela','Tarini', 'Kiruba'],
    "score" : [32,56,87]
}
# for (key,value) in student_dic.items():
#     print(key)

import pandas

student_data_frame = pandas.DataFrame(student_dic)
#print (student_data_frame)

# for (key,value) in student_data_frame.items():
#     print(value)

for (index, row) in student_data_frame.iterrows():
    # print (index)
    # print(row)
    print(row.student)
    print(row.score)



#sample list comprehension from file
# #get the contents from file 1
# file1 = open("file1.txt")
# file1_contents = file1.readlines()
# print(file1_contents)
#
# file2 = open("file2.txt")
# file2_contents = file2.readlines()
# print(file2_contents)
#
# # Write your code above 👆
# result = [int(num.strip()) for num in file1_contents if (num in file2_contents)]
# print(result)

# #sample dictionary comprehension
# import random
# names = ["Alex", "Beth", "Christina", "David", "Elisa", "Freddy"]
# student_scores = {student:random.randint(1,100) for student in names}
# print (student_scores)
#
# #get the passed students
# student_passed = {student:score for (student,score) in student_scores.items() if (score >= 50)}
# print (student_passed)


# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
# wordlist = sentence.split()
# print(wordlist)
# # Write your code below:
# result = {word:len(word) for word in wordlist}
#
# print(result)

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆
# #(temp_c * 9/5) + 32 = temp_f
#
# # Write your code 👇 below:
# weather_f = {day:(temp * 9/5) + 32 for (day,temp) in weather_c.items() }
#

# print(weather_f)










#sample list comprehension with if

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above 👆
#
# #Write your 1 line code 👇 below:
# squared_numbers = [numb*numb for numb in numbers]
#
#
# #Write your code 👆 above:
#
# print(squared_numbers)


# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above
#
# #Write your 1 line code 👇 below:
#
#
# result = [num for num in numbers if (num % 2 == 0)]
# #Write your code 👆 above:
#
# print(result)

# new_list = [n+1 for n in numbers]
# new_range = [i for i in range(5,10)]
# new_range = [i*2 for i in range(1,5)]
# name = ["Jay","Saku", "Tarini","Kiruba", "Kalai", "Srikanth", "Bhavani"]
# new_name = [name for name in name if len(name) <=4]
# names = ["Alex","Beth","Carolyn","David","Elenor","Flamingo"]
# new_nme = [name.upper() for name in names if len(name) >= 5]
