# menu = {
#     "cofee":"80",
#     "pasta":"100",
#     "salad":"40",
#     "mineral water":"20",
# }
# menuItem = []
# print("Herwe is our menu")
# for items in menu.keys():
#     print(f"we have {items}")
#     menuItem.append(items)

# print("select your order")
# resturant = input()
# if resturant not in menuItem:
#     print("we dont serve that item")
# else:
    
    
#     price = menu[resturant]
# print(f"the price of {resturant} is {price}")
class pion:
   name = "pola"
   school = "dhariwal public school"
   salary = 30000
class teacher:
   name = "zulqarnain"
guru = pion()
school=guru.school
total_payment = guru.salary

class professor :
   name = "waseem"
   guru = pion()
   school=guru.school
   total_payment = guru.salary

pro=professor()
print(pro.total_payment)
  
     