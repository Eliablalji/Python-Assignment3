def calculate_discount(price, discount_percent):
  """
  Calculates the final price after applying a discount.

  Args:
    price: The original price of the item.
    discount_percent: The discount percentage.

  Returns:
    The final price after discount, or the original price if no discount is applied.
  """

  if discount_percent >= 20:
    discount_amount = (discount_percent / 100) * price
    final_price = price - discount_amount
    return final_price
  else:
    return price


# Get input from the user
original_price = float(input("Enter the original price: "))
discount = float(input("Enter the discount percentage: "))

# Calculate and print the final price
final_price = calculate_discount(original_price, discount)

if discount >= 20:
  print("Final price after discount:", final_price)
else:
  print("Original price:", final_price)