"""Practice instantiating Pizza class."""

from pizza import Pizza

my_pizza: Pizza = Pizza("large", 1, True)
sals_pizza: Pizza = Pizza("small", 2, False)

# def price(pizza_order: Pizza) -> float:
#     """Calculate and return cost of pizza."""
#     price: float = 0.0
#     if pizza_order.size == "large":
#         cost = 6.0 
#     else: 
#         cost = 5.0
#     # charge 0.75 for topping
#     cost += .75 * pizza_order.toppings
#     # charge $1 for gluten free
#     return cost

print(my_pizza.price())
print(sals_pizza.price())
my_pizza.add_toppings(2)
print(my_pizza.toppings)
print(my_pizza.price)
