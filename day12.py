print("enter first number")
first_number = input()
print("enter second number")
second_number = input()
print("perform any arithmatic operation")
arithmetic_operatio = input()
inputlength1 = len(first_number)
inputlength2 = len(second_number)
inputlength3 = len(arithmetic_operatio)
if inputlength1==0 or inputlength2==0:
    print("please enter a valid number")
elif inputlength3==0:
    print("please enter a operation")
elif arithmetic_operatio=="+":
   inputlength1 = input(first_number)
   inputlength2 = input(second_number)
   print(first_number+second_number)
elif arithmetic_operatio=="-":
    inputlength1 = input(first_number)
    inputlength2 = input(second_number)
    print(first_number-second_number)
elif arithmetic_operatio=="*":
    inputlength1 = input(first_number)
    inputlength2 = input(second_number)
    print(first_number*second_number)
elif arithmetic_operatio=="/":
    inputlength1 = input(first_number)
    inputlength2 = input(second_number)
    print(first_number/second_number)
else:
 print("please enter a valid operation from this +,-,/,*")