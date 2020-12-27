# there is a class named Exception in python which has all the expection specified in it. When we have to handle multiple exceptions this comes handy
try:
    f=open('sample.txt') # this  is a file not found error
    a=b # this is name error
    z=10/0 # this is zero divison error 

# now we need to handle all these 3 exceptions 
except FileNotFoundError: # this means when the File not found error is detected come to this block
    print('File not found')

except NameError as e: # here the name error exception is handled 
    # as e is given to print the internal message of NameError
    print(e)

except: # rest of the exceptions are handled here
    print(" Some error has occured")