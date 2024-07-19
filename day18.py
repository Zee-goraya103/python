# class MYclass :
#   x = 5
#   y = 3
#   z = 5

# fruits = MYclass()
# print(fruits.x,fruits.y,fruits.z)
# class Person :
#  def __init__(self,name,age):
#   self.name = name
#   self.age = age  

#   def myfunc(self):
#    print("hello my name is" + self.name)

# p1 = Person("john",35)
# p1.myfunc()
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.age = 40
p1.myfunc()