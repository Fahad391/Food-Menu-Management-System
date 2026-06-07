# created a function to add dishes in the Menu
def add_dish(dish_name, dish_price):
    if not dish_name:
        raise ValueError("Dish Name can't be empty")
    
    # using exception handling to tackle errors
    try:
        price = float(dish_price)
    except ValueError:
        raise ValueError("price must be either integer or a decimal number")
    
    # used 'a' to append and avoid overwrite
    with open("Menu.txt", 'a') as menu:
        insert_item = f"Dish: {dish_name}  Price: {price} BDT\n"
        menu.write(insert_item)

# created another function to display Menu items
def view_menu():
    try:
        with open("Menu.txt", 'r') as menu:
            items = menu.read()
            return items if items.strip() else "Menu is empty"
    except FileNotFoundError:
        return "File not found."