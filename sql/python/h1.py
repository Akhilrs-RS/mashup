import random

# Prices per kg (using integers)
price_rice = 45
price_sugar = 40
price_oil = 130

# Quantities bought (using floats)
qty_rice = 3.0
qty_sugar = 2.5
qty_oil = 1.8

# Calculate total price for each item
total_rice = price_rice * qty_rice       # float result
total_sugar = price_sugar * qty_sugar    # float result
total_oil = price_oil * qty_oil          # float result

# Final total before delivery
final_total = total_rice + total_sugar + total_oil

# Show totals
print("Total price for rice :", int(total_rice))       # explicit conversion
print("Total price for sugar:", int(total_sugar))
print("Total price for oil  :", int(total_oil))

# Show final total bill as integer and as string
final_total_int = int(final_total)
final_total_str = str(final_total_int)

print("\nFinal total (int):", final_total_int)
print("Final total (string):", final_total_str)

# Add random delivery charge (₹5–₹10)
delivery_charge = random.randint(5, 10)

# Final amount including delivery charge
final_with_delivery = final_total_int + delivery_charge

print("\nDelivery charge added:", delivery_charge)
print("Final bill including delivery:", final_with_delivery)