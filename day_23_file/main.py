# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()


# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

with open("/Users/sakuj/Desktop/my_file.txt","a") as file:
    file.write("\nThis is from python code appending the file with a relative path")


