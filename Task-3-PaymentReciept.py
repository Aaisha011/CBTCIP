# import datetime
# shop_name=input("Enter your shop name:\n")
# payer_name = input("Enter payer's name: ")
# payment_method = input("Enter payment method (e.g., Credit Card, Cash, etc.): ")  
    
# sum = 0
# while True:
#     item_name = input("Enter the name of the item or type 'done' to finish:\n")
    
#     # Check if the user wants to finish shopping
#     if item_name.lower() == "done":
#         print(f"Your total bill is Rs.{sum} and thanks {payer_name} for shopping with us, visit again...")
#         break
    
#     # If not "done", then proceed to ask for the price
#     item_price = int(input("Enter the price of the item:\n"))
#     sum += item_price
#     print(f"Your bill is Rs.{sum}")
    

# payment_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# print(payment_date)
# print(shop_name)


import datetime

shop_name = input("Enter your shop name:\n")
payer_name = input("Enter payer's name: ")
payment_method = input("Enter payment method (e.g., Credit Card, Cash, etc.): ")  

sum = 0
items = []

while True:
    item_name = input("Enter the name of the item or type 'done' to finish, or 'remove' to remove the last item:\n")
    
    if item_name.lower() == "done":
        payment_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("\n----- Receipt -----")
        print(f"Shop Name: {shop_name}")
        print(f"Payer Name: {payer_name}")
        print(f"Payment Method: {payment_method}")
        print(f"Date: {payment_date}\n")
        print("Summary of your purchase:")
        for item in items:
            print(f"{item['name']} (x{item['quantity']}): Rs.{item['total_price']}")
        print(f"\nYour total bill is Rs.{sum}. Thanks {payer_name} for shopping with us, visit again!")
        break
    
    if item_name.lower() == "remove":
        if items:
            last_item = items.pop()
            sum -= last_item['total_price']
            print(f"Removed {last_item['name']} (x{last_item['quantity']}) from your bill. New total: Rs.{sum}")
        else:
            print("No items to remove.")
        continue
    
    try:
        item_price = int(input("Enter the price of the item:\n"))
        item_quantity = int(input("Enter the quantity of the item:\n"))
    except ValueError:
        print("Invalid input! Please enter numerical values for price and quantity.")
        continue
    
    item_total_price = item_price * item_quantity
    sum += item_total_price
    items.append({"name": item_name, "price": item_price, "quantity": item_quantity, "total_price": item_total_price})
    
    print(f"Added {item_name} (x{item_quantity}) to your bill. Your current total is Rs.{sum}")

print(shop_name)
