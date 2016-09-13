price = 1
total_price = 0
print "Type the price of your purchase and press Enter to see the current total. When you finish, enter 0 to complete the purchase."

while price != 0:
    strPrice = raw_input("Enter the price of your item: ")
    price = float(strPrice)
    total_price += price

    print "Here is your current total: $" + str(total_price)

tax = total_price * .06

output_tax = round(tax, 2)

print "Tax at 6%: $" + str(output_tax)

total = total_price + tax

output = round(total,2)

print "Your total with tax comes to, $" + str(output)
