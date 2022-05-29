
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# a=dec.items()
# a=dec.keys()
print("opetion are:",car.keys())
a=input("Enter you word  ")
print("key menaing is : ",car.get(a))

# car.update({"color": "White"})
car1=car.get("year")

print(car1)