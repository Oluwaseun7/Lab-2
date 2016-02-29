###Akinnusotu Lab Assignment #2
##x=int(input('Enter first number: '))#User asks what the number is
##y=input('Enter the function you want to use ( /,+,-,* ): ')#ask what the sign is
##z=int(input("Enter second number: "))#asks what the second number is
##
##
##if y is '/' :#says if y is /
##    d=x/z#divide the two numbers
##    print ('Your answer is', d)#prints the answer
##
##elif y is '+' :#if y is +
##    c=x+z#adds the two numbers 
##    print ('Your answer is', c)#prints the answer
##
##elif y is '-' :#says if y is -
##    a=x-z#subtracts the two numbers
##    print ('Your answer is', a)#prints the answer
##
##elif y is '*' :#says if y is *
##    b=x*z#multplies the two numbers
##    print ('Your answer is', b)#prints the answer

#2.3
expr = "12+27"#I put the real equatuion that I am trying to find
plus_sign=expr.find("+")#I told the user to find the + in the problem
num1=int(expr[0:plus_sign])#I made a variable for the first two numbers and + 
num2=int(expr[plus_sign:])#I made a variable for the last two numbers
print("12+27=",num1+ num2)#I put the original problem equal to both my variables
