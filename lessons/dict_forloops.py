"""Practice with Dictionaries and for Loops"""

in_stock: dict[str, bool] = {"carrots": True, "beets": False, "apples": True}

for key in in_stock:
    #key is "carrots" "beets" "apples"
    #in_stock[key] is values: True False True
    if in_stock[key] is True: #in_stock[key] is True (conditional already checks booleans)
        #could also use if in_stock[key] is True
        print(key)
 