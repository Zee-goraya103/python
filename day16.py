# print("enter the quantity")
# quantity = int(input())
# print("enter the price")
# price = int(input())
# print("enter require numbers")
# numbers = int(input())

# def engine_oil(name):
#     print(f"oil name is {name}")

# engine_oil("toyota")
print("enter first number")
first_number = input()
print("enter second number")
second_number = input()
print("perform any arithmatic operation")
arithmetic_operatio = input()
inputlength1 = len(first_number) 
inputlength2 = len(second_number)
addition = lambda x,y:x+y
subtraction = lambda x,y:x-y
multiplication = lambda x,y:x*y
dvision = lambda first_number,second_number:first_number/second_number

first_number = int(first_number)
second_number = int(second_number)
if inputlength1==0 or inputlength2==0: 
    print("please enter a valid number") 
elif arithmetic_operatio=="+":
  print(addition(first_number,second_number))
elif arithmetic_operatio=="-":
  print(subtraction(first_number,second_number))
elif arithmetic_operatio=="*":
  print(multiplication(first_number,second_number))
elif arithmetic_operatio=="/":
  print(dvision(first_number,second_number))
else:
  print("Enter valid symbol for calculation")

