# age = 22

# while age <= 18:
#     print(age)
#     if age >=5:
#      break
#     age+=1
# else:
#    print("Your number is longer then the number and that wht the condition is false")
# fruits = ["apple","banana","orange"]
# for x in fruits:
#     print(x)
#     if x=="banana":
#         break
print("enter your age")
age = int(input())
while age>=18:
    print(f"Your age is {age} you can drink ")
    break
while age<18:
    print("enter your age")
    age = int(input())

