# 1. Accept the order amount and membership status ("yes" or "no") from the user.
order_amount_input = input("Enter order amount (₹): ")
membership_input = input("Are you a member? (yes/no): ")

# 2. Use string operations to handle membership input without case sensitivity.
membership_status = membership_input.strip().lower()
order_amount = float(order_amount_input)

# 3. Use comparison operators and Boolean expressions to validate the order amount.
is_valid_amount = (order_amount >= 0) and (order_amount < 100000)

# 4. Use conditional statements to determine the applicable discount percentage.
if not is_valid_amount:
    eligibility_status = "Invalid Order Amount"
    discount_percentage = 0
    discount_amount = 0
    final_payable = order_amount
else:
    eligibility_status = "Valid"
    # Business rules evaluation
    if order_amount >= 5000:
        discount_percentage = 15
    elif order_amount >= 2000 and membership_status == "yes":
        discount_percentage = 10
    else:
        discount_percentage = 0
    
    discount_amount = (order_amount * discount_percentage) / 100
    final_payable = order_amount - discount_amount

# 5. Display the original amount, discount amount, final payable amount, and eligibility status.
print("\n--- Shopping Summary ---")
print("Eligibility Status:", eligibility_status)
print(f"Original Amount: ₹{order_amount}")
print(f"Discount Percentage: {discount_percentage}%")
print(f"Discount Amount: ₹{discount_amount}")
print(f"Final Payable Amount: ₹{final_payable}")
