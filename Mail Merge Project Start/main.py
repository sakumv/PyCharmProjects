

#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
PLACE_HOLDER = "[name]"

invite_names =[]
with open("./Input/Names/invited_names.txt") as invite_list:
    invite_names = invite_list.readlines()




#     #Replace the [name] placeholder with the actual name.
with open("./Input/Letters/starting_letter.txt") as inv_letter:
    contents = inv_letter.read()
    for name in invite_names:
        striped_name = name.strip()
        new_letter = contents.replace(PLACE_HOLDER, striped_name)
        path = "./Output/ReadyToSend/" + striped_name + ".txt"
        with open(path,mode="w") as invitation:
            invitation.write(contents)

#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

