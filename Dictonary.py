"""
# recap of list, tuple, set
lst = [1,2,3,4,5]
# first element in the list
print(lst[0])


# last element of the lists
n = len(lst)
print(lst[n-1])
print(lst[-1])

# tuple is same as list

# set is unordered
set = {1,2,3,4,1,2,5,1,2,3}
print(set)

# how to access the elements from the set

# way 1: using for loop
for ele in set:
    #print(ele)
    pass

# way 2: convert in to list/tuple
set_to_list  = list(set)
print(set_to_list[0])


# Dictionary ( dict )is key value pair data structure.aka map in java
# Unordered
# Mutable
student = {"name":"Deepali","stid":10,"city":"Pune"}
# To display all the dictory contents
print(student)

# To access a value based the key
print(student['name'],student['city'])
# to acess using .get()
print(student.get('name'))

# add one more item
student['country']="India"

# update /change the existing value
student['city'] = "Bangalore"

# remove an specified item base don key
print(student)
student.pop("stid")
print(student)

# to remove the last item in the dictinary
student.popitem()
print(student)


student = {"name":"Deepali","stid":10,"city":"Pune"}
# to get all the keys
#print(student.keys())
# to get all the values
#print(student.values())

# Iterate over the dictionary
for ele in student.items():
    print(ele)

# Iterate over the dictionary
for ele in student.items():
    print(ele[0],": ",ele[1])

# Iterate over the dictionary
for key,value in student.items():
    print(key,value)


# From a given list, how to count the number of corruences of each elements
list1  = [ 1,2,3,4,5,1,2,5,5]

"""
1:2
2:2
3:1
4:1
5:3
"""

# list1  = [ 1,2,3,4,5,1,2,5,5]
def count_list_occurence(list):
    count_element = {}
    for ele in list:
        if ele in count_element:
            count_element[ele]=  count_element[ele] + 1
        else:
            count_element[ele] = 1
    return count_element

print(count_list_occurence(list1))

# Assignemnt
# a) Find all the duplicate values in the list and return that as list
# b) Find all the unque values in the list and return that as list
"""

# Pandas

















