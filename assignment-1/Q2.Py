#Taking user details for a shopping scenario:
Customer_name=input("Enter your name:")
Product_price=float(input("Enter the price of the product:"))
Premium_member=bool(input("Are you a premium member? (Yes/No):"))
Coupon_code=input("enter the coupon code (if any):")

#Applying discount based on the criteria:
if Product_price>5000 and Premium_member:
    Discount=0.20
elif Coupon_code=="SAVE10" or Premium_member:
    Discount=0.10
else:
    Discount=0.0

#Calculating the final price after discount:
Final_price=Product_price*(1-Discount)

#Displaying the final price to the customer:
print(f"\n--- Final Price for {Customer_name} ---")
print(f"Original Price : ₹{Product_price}")
print(f"Discount       : {Discount*100}%")
print(f"Final Price    : ₹{Final_price}")
if Premium_member:
    print("Premium benefits applied.")