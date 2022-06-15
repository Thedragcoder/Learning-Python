# the variale message is a global variable and can be accessed anywhere on the program for this reason
# global variable stays for longer period of time until they are garbage collected
# you should not use global variable that often they are evil
# SO AS A BEST PRACTICE CREATE FUNCTIONS WITH LOCAL VARIABLES AND USE THEM
message = "This is a global variable"


def what_scope():
    # the scope of this me_ssage variable is what_scope function
    me_ssage = 'This is a local varaible'
# this variable cant be accessed outside of the function


def mess(name):
    message_one = "hello"


def messa(name):
    message_one = "hello world"
# the parameter name and the local variable message_one are completly different from one another


# THE LOCAL VARIABLES HAVE SHORT LIFETIME SO WHEN WE CALL MESS FUNCTION AND PASS THE ARGUMENT TO IT THE PYTHON
# INTERPRETER WILL ALLOCATE SOME MEMORY AND HAVE THE NAME AND MESS VARIABLE REFERENCE THOSE MEMORY LOCATIONS
# WHEN YOU FINISH EXECUTING THE MESS FUNCTION THESE VARIABLES ARE NOT REFERENCED OR USED ANYWHERE ELSE
# AND EVENTUALLY THEY GET GARBAGE COLLECTED WHICH MEANS PYTHON INTERPRETER WILL RELEASE THE MEMORY ALLOCATED FOR THESE VARIABLES
mess('local')
