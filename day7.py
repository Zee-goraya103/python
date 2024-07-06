# print("Hello world")

cars={
    "model":"v8",
    "color":"black",
    "tyre":"four",
    "seats":"8",
    "seatss":"8",
}
print(cars)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}

carKeys = thisdict.keys()
print(carKeys)
print([thisdict["model"]])

thisdict["model"]="Ford"

print([thisdict["model"]])

carModel = cars.get("model")
print(f"My car model is {carModel}")