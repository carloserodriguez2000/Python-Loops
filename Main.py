############################################################
##-Create a program that counts from 0-100
##-If the number is divisible by 3 print Fizz instead
##-If the number is divisible by 5 print Buzz instead
##-If the number is divisible by 3 and 5 print FizzBuzz

################################################################################
def printStartingAt( initialValue):
        print (" The initial value is %s." %(initialValue))
        if (((initialValue % 3) == 0) and ((initialValue % 5) == 0)):
            print ('FizzBuzzBangBongle for %s' %(initialValue))
        elif ( (initialValue % 5) == 0) :
            print ('Buzz for %s' %(initialValue))
        elif ((initialValue % 3) == 0 ):
            print('Fizz for %s' %(initialValue))

        

    

############################################################
def main ():
    number=1
    while number < 100:
        printStartingAt( number )
        number+=1

############################################################
main()

