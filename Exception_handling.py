#  the first statement which might rasie and exception should be given in try block
# the code that needs to be excuted in case of the try block fails is given in except block

try:
    f=open('sample.txt')
except:
    print('The file your trying to access is not found !')
#  there instead of giving a run time error , once the try block failed the except block is executed which alerts the user about the error that happened above ( this is just an example , not everytime the  except block needs to have this).
else:
    print('file opened successfully ')
    #  else statement is executed when the exception doesn't occur at all