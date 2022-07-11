# # with open("weather_data.csv") as weather_file:
# #     contents = weather_file.readlines()
# #     print(contents)
# #
# # import csv
# #
# # with open("weather_data.csv") as weather_file:
# #     content_object = csv.reader(weather_file)
# #     temperature = []
# #     for data in content_object:
# #         if data[1] != "temp":
# #             temperature.append(int(data[1]))
# #
# # print(temperature)
#
# import pandas
#
# content = pandas.read_csv("weather_data.csv")
#
# # print (content)
# # print(content["day"])
# # print(content["temp"])
#
# # content_dict = content.to_dict()
# # temp_list = content["temp"].to_list()
# # print (type(temp_list))
# # print(type(content))
# # print(type(content["temp"]))
# # avg_temp = 0
# # for i in temp_list:
# #     avg_temp += i
# # avg_temp = avg_temp / len(temp_list)
# # print (avg_temp)
#
# #max
# #print(content["temp"].max())
#
# #print(content[content.day == "Monday"])
#
# #print (content[content.temp == content["temp"].max()])
#
# monday = content[content.day == "Monday"]
# mtemp_in_c = monday.temp
# mtemp_in_f = (mtemp_in_c * 9/5) + 32
# print (mtemp_in_f)





import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

data_fur = data["Primary Fur Color"]

gray = len(data[data["Primary Fur Color"]=="Gray"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black]
}
data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("squirel color count")
