#  there is also a way to handle multiple exceptions in one except block 
print("hello")
try:
    # a=b
    print( "breaked here")
    # z=10/0
    f=open('sample.txt')

except (NameError,ZeroDivisionError):
    print('Some error has occured ')
#  just like in the single exception handling case it wont move to next line when and exception is encountered.
#  if the exception is not caught in the above cases then it moves to another except block if provided.
except:
    print('Error')
