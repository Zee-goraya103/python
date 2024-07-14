# def my_function(name):
#     print(f"your name is {name}")

# my_function("zulqarnain")
# print("enter your name")
# name = input()
# print("enter your age")
# age = int(input())
# def  intro(x,y):
#     print(f"your name is {x}your ages is {y}")

# intro(name,age)
print("enter first number")
first_number = input()
print("enter second number")
second_number = input()
print("enter the expression")
arithmetic_operation = input()

def adding(a, b):
    print(a + b)

def minus(a, b):
    print(a - b)

def multiplication(a, b):
    print(a * b)

def division(a, b):
    print(a / b)

def answer(a, b, c):
    if c == "+":
        adding(a, b)
    elif c == "-":
        minus(a, b)
    elif c == "*":
        multiplication(a, b)
    elif c == "/":
        division(a, b)
    else:
        print("Invalid arithmetic operation")

def calculation(x, y, z):
    if not x or not y or not z:
        print("Please input valid values")
    else:
        first_number = int(x)
        second_number = int(y)
        arithmetic_operation = z
        answer(first_number, second_number, arithmetic_operation)

calculation(first_number, second_number, arithmetic_operation)

    
