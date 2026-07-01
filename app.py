# print("hello")
# functions
# code - controlled
# maintain
# reusable
# readable

# naming convention
#  myFunction
# _my_function
# -myfunction
#  4function

# def myFunction():
#  print("hello this is funtion")
# myFunction()  #invoke  

# def myname(fname,lname):  # parameter
#   print("my name is" + " jnew " , fname,lname)
# myname("ibrahim" , "khan")  # argument

# def sum(num1,num2):
#    print(num1 + num2)
# sum(2,3)   
  
# def sum(num1,num2=0): #default parameters
#    print(num1 + num2)
# sum(2)   

# def sum(a,b):
#    return a + b 
   
# newvariable = sum(2,3)
# print(newvariable)

# def yourname(name="monster"):
#      print(name)
# yourname()    
# yourname("danish")    
# yourname("khan")    

# def sum(a,b):
#     print("sum=>",a+b)
# sum(a=2,b=3) 

# def fname(fname,lname,fullname):
#     print("my fname is", fname,fullname + "  " +  " " +  "and my lname is",lname)
# fname("ibrahim","khan" , "ibrahim khan")

# def sum():
#  return ("hello")
# againsum = sum()
# print(againsum)

# a = 2 # assign
# a == 2 # equal to 
# "2" === 2 # equal with type

# -- topic (data and interactivity)
# data - information
# which use for input and output process
   # -data types
# name = "ibrahim" - string
# age = 15 - integer (int)
# height = 5.9 - float
# isActive = true - boolean (bool)

# sum = 2 + "3" # error
# sum = "2" + "3" #concatenation
# sum = 2 + 3.5 # temporary (coercion)
# total = 300
# obtain = "100"
# percent = obtain / total * 100
# print(type(percent))
# print(type(obtain))

# --- interactivity
# input()
# num1 = 3
# num2 = 4
# sum = num1 + num2
# print(sum)

# num1 = +input("enter first num ")
# num2 = +input("enter second num ")
# # sum = int(num1) + int(num2)
# sum = num1 + num2
# print(sum)

# obtain = int(input("enter your marks : "))
# total = int(input("enter total marks : "))
# print("your percentage is ", obtain / total *100)

# asssignment
# .function(fullname)
# .input (user multiplication)


#  --- list
std1 = "ali"
std2 = "bilal"
std3 = "ayan"
std4 = "asad"

# stduntlist = ["ali","bilal","ayan","asad"]
# print(stduntlist)
# # list - rules
#  [ ] , [ , ] - comma seperated
# stduntlist = ["ali",20,76.76,True]
# order         1    2   3    4 (length) -total elements
# order access. 0    1   2    3 (index)start from zero
# print(len(stduntlist)) - length
# print(stduntlist[0])
# print(stduntlist[1])
# print(stduntlist[4]) - out of range error
# print(stduntlist[-1])
# print(stduntlist[-2])
# print(stduntlist[2:])
# index order cannot be changed
# list can be modify (changeable)


# mydata = ["ali",20,"ali@gmail.com"]
# mydata.append(30) - add in last
# mydata.insert(2,"danish") #- 2 is index , "danish" is element
# mydata.remove("ali@gmail.com")
# mydata.remove("khan") - not exist error
# mydata.pop(0)
# del mydata[2] # del is keyword
# mydata.clear()
# print(mydata)

# str, int,list, (reserve) not use in variable name
# list1 = ["a","b","c"]
# list2 = ["d","e","f"]
# list1.extend(list2) # method (formula)
# list1.remove() #formula
# list1.pop()
# print(list1)

# a = "b"
# list2 = [a , "a"]
# print(list2)
# "a" - string , a -variable

# list1 = ["a","b","c"]
# # list1.pop()
# list1.pop(1)
# print(list1)

list1 = ["a","b","c"]
# list1[0] = "khan"
list1[0:2] = ["ibrahim","khan"]
print(list1)

asssignment
create a list in which you can connect 2 lists
create a list and remove second index with 2 new add values
create a list and remove first and last element using method