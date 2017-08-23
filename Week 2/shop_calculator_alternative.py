def main():
    price_total = 0.0
    price_discount = 0.9
    number_of_items = int(input("Number of items:"))
    while number_of_items < 1:
        print("invalid.")
        number_of_items = int(input("Number of items: "))
    for i in range(number_of_items):
        price_total += float(input("Price of item: "))
    if price_total > 100:
        price_total *= price_discount
    print("{:.2f}".format(price_total))
main()
