total = 0
cart={}
groceries = {
    "apples": 5,
    "banana": 3,
    "chocolate": 7,
    "milk":4,
    "milkshake":4,
    "water":2

}


while True:
    cin = input("What do you want to buy? ").lower().strip()

    if cin == "done":
        break


    spliting = cin.split()
    item, quantity = spliting[0], int(spliting[1])

    if item in groceries:
        if item in cart:
           cart[item] = cart[item] + quantity

        else:
            cart[item] = quantity

    else:
        print("Sorry, we don’t have that item")

for item, quantity in cart.items():
    price = groceries[item]
    if item == "milk" and quantity > 2:
        price = price -1  
    total += price * quantity



print("you bought: ", cart )
print("total = $ ", total)

if total > 10:
    print("You spent a lot!")
else:
    print("You spent a little!")
