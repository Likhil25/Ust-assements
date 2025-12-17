items = []
category_totals = {}

n = int(input("Enter number of items: "))

i = 0
while i < n:
    print("\nItem", i + 1)

    name = input("Item name: ")
    category = input("Categories (electronics/clothing/grocery): ").lower()
    price = float(input("Price: "))

    if price <= 0:
        print("Invalid price")
        i += 1
        continue

    if category == "electronics":
        if price >= 50000:
            final_price = price * 0.90
        else:
            final_price = price * 0.95

    elif category == "clothing":
        final_price = price * 0.80

    elif category == "grocery":
        final_price = price

    else:
        final_price = price
        pass

    items.append([name, category, final_price])

    if category not in category_totals:
        category_totals[category] = 0

    category_totals[category] += final_price
    i += 1


print("\nItem Summary")
for item in items:
    print(item[0], item[1], item[2])

print("\nCategory Totals")
for cat in category_totals:
    print(cat, category_totals[cat])
