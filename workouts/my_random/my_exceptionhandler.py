try:
   fh = open("../../data/testfile", "w")
   fh.write("This is my test file for exception handling!!")
except IOError as Argument:
   print ("Error: can\'t find file or read data",Argument)
else:
   print ("Written content in the file successfully")
   fh.close()


def functionName( level ):
   if level < 1:
       raise ("Invalid level!",level)

try:
   functionName(2)
except "Invalid level!":
   print("Invalid")
else:
   print("In else")


try:
   print("Try Block1")
   num1 = 10
   "Strongly typed" + num1
except Exception as i_store_the_errormessage:
   # except block will be called when try block throws error
   print("General Exception Block, error message is -> {} ".format(i_store_the_errormessage))
else:
   print("I will be executing if no exception occurs in the try block - closing connections created in the try block")
finally:
   print("I will be executing at any cost, whether exception occured or not - closing all connections created in this code")

