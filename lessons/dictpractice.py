"""Practice with dictionaries"""

ice_cream: dict[str, int] = dict() #or use {}, 
ice_cream = {"chocolate": 12, "vanilla": 8, "strawberry": 5}

#Adding and removing idems from dictionary
ice_cream["mint"] = 3
print(ice_cream)

ice_cream.pop("mint")
print(ice_cream)

#Access or Modify Dictionary
print(ice_cream["vanilla"])
print(f"Number of chocolate orders: {ice_cream['chocolate']}")

#Updating a value
ice_cream["vanilla"] += 1
print("After adding 1 vanilla")
print(ice_cream)

#Checking if in dictionary
print("mint" in ice_cream)
print("chocolate" in ice_cream)