# def calculate_age(day,month,year):
#     today = date.today()
#     birthdate = date(year,month,day)
#     age = today.year - birthdate.year - ((today.month,today.day)<(birthdate.month,birthdate.day))
#     return age
# print("enter your birth date")
# birth_date = int(input())
# print("enter your birth month")
# birth_month = int(input())
# print("enter your birth yeay")
# birth_year = int(input())
# def calculate_age(day,month,year):
#     today = date.today()
#     birthdate = date(year,month,day)
#     age = today.year - birthdate.year - ((today.month,today.day)<(birthdate.month,birthdate.day))
# calculate_age(day,month,year)
# print(f"you are {age}years old")
from datetime import date

def calculate_age(day, month, year):
    today = date.today()
    birthdate = date(year, month, day)
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

print("Enter your birth date:")
birth_date = int(input())
print("Enter your birth month:")
birth_month = int(input())
print("Enter your birth year:")
birth_year = int(input())

age = calculate_age(birth_date, birth_month, birth_year)
print(f"You are {age} years old.")
