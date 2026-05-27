total_amount = int(input("Enter original bill amount: "))

if total_amount >= 500000:
    discount = total_amount * 10 / 100
else:
    discount = 0

final_amount = total_amount - discount

print("\n--- RIKKEI STORE PAYMENT INVOICE ---")
print(f"Discount amount: {discount:.0f} VND")
print(f"Final amount to pay: {final_amount:.0f} VND")
