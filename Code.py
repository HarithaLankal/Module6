class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        #Adds an item to cart_items list
        print("Method not implemented yet")
        pass

    def remove_item(self, item_name):
        #Removes item from cart_items list.
        print("Method not implemented yet")
        pass

    def modify_item(self, item):
        # Modifies an item's description, price, and/or quantity.
        print("Method not implemented yet")
        pass

    def get_num_items_in_cart(self):
        # Returns quantity of all items in cart.
        num_items = 0
        for item in self.cart_items:
            num_items += item.item_quantity
        return num_items

    def get_cost_of_cart(self):
        # Determines and returns the total cost of items in cart.
        total_cost = 0
        for item in self.cart_items:
            total_cost += (item.item_price * item.item_quantity)
        return total_cost

    def print_total(self):
        # Outputs total of objects in cart.
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
            return
        print(self.customer_name + "'s Shopping Cart - " + self.current_date)
        print("Number of Items:", self.get_num_items_in_cart())
        for item in self.cart_items:
            item.print_item_cost()
        print("Total: $" + str(self.get_cost_of_cart()))

    def print_descriptions(self):
        # Outputs each item's description.
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
            return
        print(self.customer_name + "'s Shopping Cart - " + self.current_date)
        print("Item Descriptions")
        for item in self.cart_items:
            print(item.item_name + ": " + item.item_description)


def print_menu(cart):
    menu = (
        "\nMENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Change item quantity\n"
        "i - Output items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit\n"
        "Choose an option: "
    )

    while True:
        choice = input(menu).lower()
        if choice == 'a':
            item_name = input("Enter the item name: ")
            item_description = input("Enter the item description: ")
            item_price = input_price("Enter the item price:\n")
            item_quantity = input_quantity("Enter the item quantity:\n")
            cart.add_item(ItemToPurchase(item_name, item_price, item_quantity, item_description))
        elif choice == 'r':
            item_name = input("Enter name of item to remove: ")
            cart.remove_item(item_name)
        elif choice == 'c':
            item_name = input("Enter the item name: ")
            new_quantity = input_quantity("Enter the new quantity: ")
            cart.modify_item(ItemToPurchase(item_name, 0, new_quantity))
        elif choice == 'i':
            cart.print_descriptions()
        elif choice == 'o':
            cart.print_total()
        elif choice == 'q':
            break
        else:
            print("Invalid option. Please try again.")

# Function to validate numerical input for price
def input_price(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError("Negative value is not allowed.")
            return value
        except ValueError as e:
            print(e)

# Function to validate integer input for quantity
def input_quantity(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError("Negative value is not allowed.")
            return value
        except ValueError as e:
            print(e)
                
def main():
    my_cart = ShoppingCart("John Smith", "April 27, 2024")
    
    print("Item 1\n")    
    item_name = input("Enter the item name:")
    item_description = input("Enter the item description:")
    item_price = input_price("Enter the item price:")
    item_quantity = input_quantity("Enter the item quantity:")
    item1 = ItemToPurchase(item_name, item_price, item_quantity, item_description)
    
    # Get details from user for item 2
    print("\nItem 2\n")    
    item_name = input("Enter the item name:")
    item_description = input("Enter the item description:")
    item_price = input_price("Enter the item price:")
    item_quantity = input_quantity("Enter the item quantity:")	
    item2 = ItemToPurchase(item_name, item_price, item_quantity, item_description)
    my_cart.cart_items = [item1, item2]
    print_menu(my_cart)

if __name__ == "__main__":
    main()
