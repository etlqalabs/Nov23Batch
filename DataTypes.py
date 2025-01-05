
# type casting ( converting data type from one to another  e.g. convert float to int )
weigth_float = 75.8


#print("The value of weight variable is: ",weigth_float, " and Data types of weight vatiable is",type(weigth_float))

weigth_int = int(weigth_float)
#print("The value of weight variable is: ",weigth_int, " and Data types of weight vatiable is",type(weigth_int))

age = 10
age_flt = float(age)
#print(age_flt,"and type is ",type(age_flt))

num1 = "123455"
num2 = "123123"
print(type(num1) ,"and ",type(num2), " and addition of 2 numbers is ",num1+num2)

num3 = int(num1)
num4 = int(num2)
print(type(num3) ,"and ",type(num4), " and addition of 2 numbers is ",num3+num4)

# Variables naming convention

# Camel Case:
myFirstName = "Ajay"

# Pascal



This is the change in the file

MyFirstName = "Ajay"

# Snake case
my_first_name = "Ajay"

# Data Types in Python
 # str ,int,float,boolean - primitive/basic datatype
 # Sequence types ( List , Tuple, Set )
 # Mapping Type ( dict )


#   EXAMPLE OF LIST
# to store a single value we can use primitive data types
# e.g age, name of a person
age = 20
name = "Ajay"
print("My name is ",name," and age is ",age)

# if we want to store multiple similar values in a single variable then type should be non primitive

name_lst = ["Ajay","Akshay","Ankita","Bhupender","Karthick","Ajay"]
name_lst.append("Azhar")
#print("List of students ",name_lst," and type is :",type(name_lst))
# o/p : "Hello Ajay ! Welcome to Python class"

for item in name_lst:
        print(f"Hello {item} ! Welcome to Python class")


#   EXAMPLE OF TUPLE
# if we want to store multiple similar values in a single variable name then type should be non primitive

name_tuple = ("Ajay","Akshay","Ankita","Bhupender","Karthick","Ajay")


#print("List of students ",name_lst," and type is :",type(name_lst))
# o/p : "Hello Ajay ! Welcome to Python class"
print(" Type of name_tuple ",type(name_tuple))
for item in name_tuple:
    print(f"Hello {item} ! Welcome to Python class")


#   EXAMPLE OF SET
# if we want to store multiple similar values in a single variable name then type should be non primitive

name_set = {"Ajay","Akshay","Ankita","Bhupender","Karthick","Ajay"}

#print("List of students ",name_lst," and type is :",type(name_lst))
# o/p : "Hello Ajay ! Welcome to Python class"
print(" Type of name_tuple ",type(name_set))
for item in name_set:
    print(f"Hello {item} ! Welcome to Python class")






















