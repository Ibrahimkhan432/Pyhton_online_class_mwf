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

obtain = int(input("enter your marks : "))
total = int(input("enter total marks : "))
print("your percentage is ", obtain / total *100)