# print("my name is odetoyinbo gbenga")
# print("my gender is male")

# myname = "odetoyinbo gbenga"
# mygender = "male"

# print(f"my name is {myname}")
# print(f"my gender is {mygender}")

# print("my name is {}".format(myname))
# print("my gender is {}".format(mygender))


# #this is a single line comment

# """
# this is a multiline comment
# this is a multiline comment
# this is a multiline comment
# this is a multiline comment
# this is a multiline comment
# """

# age = 25
# my_indian_name = "viral soteriya"
# is_a_graduate = True

# print(age)
# print(my_indian_name)
# print(is_a_graduate)


# print(f"my name  is {my_indian_name}, and i am {age} years old, i am also a {is_a_graduate} graduate")

# print(f"my age is {age}")
# print("my age is {}".format(age))

# house = "myhouse"
# house_age = 50
# house_is_new = False


# age = "20 years old"
# i_am_home = True
# losses_in_life = 20
# egusi_price = 49.99


# print(age)
# print(i_am_home)

# print(type(age))

# name = "10"
# age = int(name)
# print(type(age))

# 1.
# 2.True
# 3.True
# 4.print(type(var))
# 5.my-var = 20
# 6. car_name = "volvo"


y = 2
z = 5
addition = z + y
print(addition)

subtraction = 2 -2 
print(subtraction)

division = 2 / 2
print(division)

multiplication = 2 * 2
print (multiplication)


quotient = 2//2
print(quotient)

remainder = 2 % 2
print(remainder)

# To create a list without square bracket list()

# my_list = [1, 2, 3, 4, 5]

# my_list = [1.3, 3.5, 7.8]

# string_list = [ "apple", "orange", "pawpaw"]

# mised_list = [10, "rice", 3.142, true]

# empty_list =[]


# my_info = ["bulls eye", ["fish"], list(3.142)]


# fruits = [ "apple", "banana", "cherry"]
# print(fruits[0])

# string_list = [ "apple", "orange", "pawpaw"]
# print(string_list[0])
# print(string_list[-2])

# my_list = [1.3, 3.5, 7.8]
# print(my_list[0])
# print(my_list[1])
# print(my_list[-2])
# print(my_list[-1])

# numbers = [0, 1,2,3,4, 5, 6, 7, 8]
# print(numbers[2:5])
# print(numbers[:5])
# print(numbers[::2]) (every secibd element)


# numbers = [1,2,3]
# numbers.append(4)
# numbers.extend({6,7,8,9,10})
# print(numbers)


# original_list = [1,2,3]
# # copy_list = original_list.copy()
# copy_list = original_list = original_list[:]
# copy_list = list(original_list)
# print(copy_list)

# list1 = ["a","b", "3"]
# list2 =[1,2,3]
# list3 = list1 + list2
# print(list3)

# list =[1,2,3,4,5]
# print(len(list))

# list =[1,2,3,4,5]
# print(max(list))

# list =[1,2,3,4,5]
# print(min(list))

# list =[1,2,3,4,5]
# print(sum(list))

# list =[1,4,2,3,5]
# print(sorted(list))

# list =[1,3,4,2,5]
# list.sort()
# print(list)

# list =[1,4,2,3,5]
# list.reverse()
# print(list)

# list =[1,4,2,3,5]
# print(list.index(2))


# matrix = [[1,2,3], [4,5,6], [7,8,9]]
# print(matrix[0][2])
# print(matrix[1][1])
# print(matrix[2][0])


# scores = [90, 89, 74, 34, 59, 87, 95, 80, 55, 78, 35, 90, 66, 24, 45, 67, 81, 60]

# number_of_students = scores
# print("the number of students is", len(number_of_students))
# print("the highest score is",max(scores) )
# print("the lowest score is ", min(scores) )
# print(sorted(scores))
# print(scores[:5])
# average = sum(scores)/len(scores)
# print(average)


# thisdict = {
#   "brand":"ford",
#   "model":"Mustang",
#   "year":"1967"
# }
# print(thisdict["year"])


thisdict = {
  "brand":"ford",
  "model":"Mustang",
  "year":"1967",
  "year":"1467"
}

print(thisdict)

thisdict = {
  "brand":"ford",
  "model":"Mustang",
  "year":"1967",
}

y = thisdict["year"]
print(y)

# using get method

y = thisdict.get("year")
print(y)


thisdict = {
  "brand":"ford",
  "model":"Mustang",
  "year":"1967",
}

x=thisdict.keys()
print(x)

thisdict = {
  "brand":"ford",
  "model":"Mustang",
  "year":"1967",
}
thisdict["month"] =2018
print(thisdict)


thisdict = {
  "brand":"ford",
  "model":"Mustang",
  "year":"1967",
}
thisdict.update({"year":2020})
print(thisdict)


thisdict = {
  "brand":"ford",
  "model":"Mustang",
  "year":"1967",
}
thisdict.pop("model")
print(thisdict)


thisdict = {
  "brand":"ford",
  "model":"Mustang",
  "year":"1967",
}
thisdict.popitem()
print(thisdict)

#deleting an item 
thisdict = {
  "brand":"ford",
  "model":"Mustang",
  "year":"1967",
}

del thisdict["model"]
print(thisdict)

#deleting the whole dictionary
thisdict = {
  "brand":"ford",
  "model":"Mustang",
  "year":"1967",
}

del thisdict#
print(thisdict)