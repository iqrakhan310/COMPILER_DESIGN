def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

number = int(input("Enter a number to find its factorial: "))
result = factorial(number)
print("Factorial of", number, "is", result)


#CALCULATING DISCOUNT
def calculate_discount(price, discount_percentage):
    discount_amount = price * (discount_percentage / 100)
    discounted_price = price - discount_amount
    return discount_amount, discounted_price

# Example usage
price = float(input("Enter the original price: "))
discount_percentage = float(input("Enter the discount percentage: "))

discount_amount, discounted_price = calculate_discount(price, discount_percentage)
print("Discount amount: $", discount_amount)
print("Discounted price: $", discounted_price)


#CHECKING CASE OF CHARACTER

def check_case(char):
    if char.isupper():
        print(f"The character '{char}' is in uppercase.")
    elif char.islower():
        print(f"The character '{char}' is in lowercase.")
    else:
        print(f"The character '{char}' is neither uppercase nor lowercase.")

# Example usage
char = input("Enter a character: ")
if len(char) == 1:
    check_case(char)
else:
    print("Please enter only one character.")


