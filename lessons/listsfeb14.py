"""Demonstrate Basic List Syntax"""

# Create an empty list
grocery_list: list[str] = list() # <-constructor
grocery_list: list[str] = [] # <-- literal
print("Empty list: ")
print(grocery_list)

# Add to a list
grocery_list.append("frosted flakes")
grocery_list.append("milk")
grocery_list.append("pizza")
print("After adding things:")
print(grocery_list)

# Create a list with objects in it
grocery_list2: list[str] = ["frosted flakes", "milk", "pizza"]
print("Already populated list: ")
print(grocery_list2)
print("Add another thing: ")
grocery_list2.append("whipped cream")
print(grocery_list2)

# Indexing
print("Printing one item:")
print(grocery_list[2])

# Modifying by Index
x: list[str] = ["c", "a", "r", "s"]
x[2] = "t"
print(x)

grocery_list[0] = "cinnamon toast crunch"
print("Modifying:")
print(grocery_list)

# Length of a list
print("Length:")
print(len(grocery_list))

#Removing an item
grocery_list.pop(1)
print("Remove an item:")
print(grocery_list)

def display(t: list[str]) -> None:
    print(t)

display(["hi", "hello"])

def create(x: str, y: str) -> list[str]:
    new_list: list[str] = [x, y]
    return new_list

print(create("hi", "waz good"))


