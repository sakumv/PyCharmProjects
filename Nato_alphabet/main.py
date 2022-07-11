student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# for(index,row) in data.iterrows():
#     data_dict[row.letter] = row.code

data_dict={row.letter:row.code for (index,row) in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word : ").upper()
# word_list = list(word)
# #print (word_list)
# code_list = []
# for letter in word_list:
#     #get the value from data_dict
#     #print(data_dict[letter])
#     code_list.append(data_dict[letter])
#
# print(code_list)
output_list = [data_dict[letter] for letter in word]
print(output_list)