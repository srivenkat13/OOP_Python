#  there is also a way to handle multiple exceptions in one except block 

try:
    a=b
    print( "breaked here")
    z=10/0

except (NameError,ZeroDivisionError):
    print('Some error has occured ')
#  just like in the single exception handling case it wont move to next line when and exception is encountered.
