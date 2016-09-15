price = 1
total_price = 0

def calculate_tax(amount):
        tax_amount = amount * .06
        tax_output = round(tax_amount, 2)
        return tax_output

print "Type the price of your purchase and press Enter to see the current total. When you finish, enter 0 to complete the purchase."

while price != 0:
    strPrice = raw_input("Enter the price of your item: ")
    price = float(strPrice)
    total_price += price

print "Here is your current total: $" + str(total_price)

output_tax = calculate_tax(total_price)

print "Tax at 6%: $" + str(output_tax)

amount = total_price + output_tax

calculate_tax(amount)

print "Your total with tax comes to, $" + str(round(amount, 2))
