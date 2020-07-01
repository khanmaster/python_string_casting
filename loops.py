# # what are loops
# # for loops are used to iterate through Lists, strings, Dictionaries and Tuples
# # syntax:- for variable in name of the data_collection(list,string,dictionary or Tuple)
#
#
# list_data = [1, 2, 3, 4, 5]
# for data in list_data:
#
# # if condition will come inside for loop
#  if data > 4:
#     print(data)
#     # break condition will come inside if block
#     #print(data)
#     # print data block should be within if block

# create a string and loop through the string
# city = "London"
# for letter in city:
#     print(letter)

# print the string in one line

# looping through a dictionary
student_record = { "name": "shahrukh",
                   "stream": "DevOps",
                   "completed_lesson": 5,
                   "completed_lessons_names": ["strings", "Tuples", "variables"]
}
for record in student_record.keys():
    if record == "name":
        print(record)
    elif record == 5:
        print(record)

# exercise

# dictionary with employee records minimum 5 key value pairs

# using loop iterate through the dictionary

# display the values of and keys of the dictionary

#










# print(list_data[0])
# print(list_data[1])
# print(list_data[2])
