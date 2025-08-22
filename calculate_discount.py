def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Args:
        price (float): The original price of the item
        discount_percent (float): The discount percentage
    
    Returns:
        float: The final price after discount or original price if no discount applied
    """
    # Check if discount is 20% or higher
    if discount_percent >= 20:
        # Apply the discount
        final_price = price * (1 - discount_percent / 100)
        return final_price
    else:
        # Return original price if discount is less than 20%
        return price

# Prompt user for input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(original_price, discount_percentage)

# Print the result
if discount_percentage >= 20:
    print(f"Final price after {discount_percentage}% discount: ${final_price:.2f}")
else:
    print(f"No discount applied. Original price: ${original_price:.2f}")
