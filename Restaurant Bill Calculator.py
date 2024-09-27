# Restaurant Bill Calculator

print("Welcome to our Restaurant. Here's is the menu:")
print(" Pizza: Rs:40\n Pasta: Rs:50\n Burger: Rs:60\n Salad: Rs: 70\n Coffee: Rs:80")

menu = {
    "Pizza":40,"Pasta":50,"Burger":60,"Salad":70,"Coffee":80,
}

order_total = 0
item = input("Enter the item: ")
if item in menu:
    order_total += menu[item]
    print(f"Your item {item} has been added to your order.")
else:
    print(f"Order item is not available yet.")

another_item = input("Do you want to add another item? (yes/no) ")
if another_item == "yes":
    item2 = input("Enter the next item: ")
if item2 in menu:
    order_total += menu[item2]
    print(f"Your item {item2} has been added to your order.")
else: 
    print(f"Order item is not available yet.")
    
print(f"Total amount of item is {order_total}")






