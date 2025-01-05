#  print all the elements/characters in the string
channel_name = "ETL QA Labs"
# length of the string ( total number of characters in the string )
n = len(channel_name)
#print(n)
startIndex = 0
endIndex = n -1

# way 1
for idx in range(startIndex,endIndex+1,1):
    #print(channel_name[idx], end = ",")
    pass

print()
# way 2
for ele in channel_name:
    #print(ele, end = " | ")
    pass


# extract the substring from 1st charcter to 6th charcter
#channel_name = "ETL QA Labs"

# way 1
for idx in range(0,6,1):
    #print(channel_name[idx])
    pass

# way 2
for idx in range(0,6,1):
    #print(channel_name[idx])
    pass

# way 3
#print(channel_name[0:6:1])


# specific step = 3
for idx in range(0,11,3):
    #print(channel_name[idx],end=" ")
    pass

# String Slicing
#channel_name = "ETL QA Labs"
#print(type(channel_name))
first_word = channel_name[0:3:1]
#print(first_word," type is :",type(first_word))

full_string  = channel_name[0:n:1]
#print("Forward dierction :",full_string)


# form  a string with Alternate characters from the channel_name string
alternate_char = channel_name[0:n:2]
#print(alternate_char)


# print the wole string in forward dierction
full_string  = channel_name[::1]
#print("Forward dierction :",full_string)

# Print the string in reverse order
reverse = channel_name[::-1]
#print("reverse dierction :",reverse)

rev = channel_name[n::-1]
#print(rev)

"""
# While loop usage
# Print from 10 to 20
startNum =  10
endNum = 20
print(" printing using while loop")
while startNum <= endNum:
    print(startNum,end = " | ")
    startNum = startNum + 1

startNum =  10
endNum = 20
print(" startnum:",startNum," and endNum :",endNum)
print(" printing using for loop")
for num in range(startNum,endNum+1,1):
    print(num,end = " , ")
"""

# Split function ( by default split will accept as space,tabs or newline
name = "ETL QA Labs"
#print(type(name)) # string
words = name.split()
#print(words)

emailId = "etlqalabs@gmail.com@hotmail.com"
emaillist  = emailId.split("@")
#print(emaillist)
#print("first part of email: "+emaillist[0])
#print("second part of email: "+emaillist[1])
#print("Third part of email: "+emaillist[2])

for part in emaillist:
    #print(part)
    pass


# continue
# print all the even numbers from 1 to 20
# way 1
for i in range(0,21,1):
    if (i % 2 != 0):
        continue
    #print(i, end = " ")
# way 2
for i in range(0,21,1):
    if (i % 2 == 0):
        #print(i, end = " ")
        pass


# break
l = [1,2,3,4,5,6,10,20,40,50]
for ele  in l:
    if ( ele == 10 ):
        break
    #print(ele, end =  " ")

"""
# if .. else ...elif

marks = 80

if ( marks < 34 ):
    print("exam failed " )
elif (marks >=34 and marks <=45):
    print(" Thrird division" )
elif (marks >45 and marks <60):
    print(" second division" )
else:
    print(" first division")
"""

# Function definition
def print_name():
    print("Hello , I am a function  line 1")
    print("Hello , I am a function Line 2 ")
    print("Hello , I am a function line 3")
    print("Hello , I am a function line 4")

#print_name()

# Write a function to check if given number is even or odd

def check_even_or_odd(num):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

check_even_or_odd(2)
check_even_or_odd(3)



