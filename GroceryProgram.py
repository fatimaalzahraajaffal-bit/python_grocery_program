total = 0
cart=[]
groceries = {
    "apples": 5,
    "banana": 3,
    "chocolate": 7,
    "milk":4,
    "milkshake":4,
    "water":2

}


while True:
    item = input("What do you want to buy? ")

    if item == "done":
        break
    if item in groceries:
        cart.append(item)

    else:
        print("Item not available.")
