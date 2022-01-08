price_list={'Juice':30, 'Fried Rice':150, 'Burger':50, 'Pizza':110, 'Fried Chicken':90, 'Noodles':70}
def take_order():
    items = []
    total_cost = 0
    print("Please enter the name of the items:")
    while True:
        input_item = input()
        if input_item=='X':
            break
        else:
            items.append(input_item)
    for i in items:
        total_cost += int(price_list[i])

    print(f"Total cost: {total_cost}")
take_order()