# what is a Tuple
# same as lists but IMMUTABLE
# WHY Tuples - to store the data that would not need changing i.e Date of birth, passport number etc.

# Syntax of Tuple: we use () to create a Tuple

#user_details_tuple = ("name", "dob", "passport number")
# print(dob)

# print(len(dob))
# print(dob[1])


user_details_tuple = ("name", "dob", "passport number")

# Convert the tuple into an string
user_detail_list = list(user_details_tuple)
print(user_detail_list)
print(type(user_detail_list))

# # add your name into the string at 0 index
user_detail_list[0] = "james"
# display the list
print(user_detail_list)



