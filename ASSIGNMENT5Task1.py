#Task 1: Create a Dictionary of Student Marks
dict={'alice': 84,'ram':65, 'diya': 98,'tiya':55,'jiya':69}
#print(dict)
name=input("Enter student 's name: ")
m=dict.get(name)


if m != None:
    print("{}'s marks:{}".format(name, m))
else:
    print('Student not found')





