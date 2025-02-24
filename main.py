class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        if product.stock >= quantity:
            self.items.append({"product": product, "quantity": quantity})
            product.stock -= quantity
            print(f"Added {quantity} {product.name}(s) to the cart.")
        else:
            print(f"Not enough stock for {product.name}.")

    def remove_item(self, product):
        for item in self.items:
            if item["product"] == product:
                product.stock += item["quantity"]
                self.items.remove(item)
                print(f"Removed {product.name} from the cart.")
                return
        print(f"{product.name} not found in the cart.")

    def update_item_quantity(self, product, new_quantity):
        for item in self.items:
            if item["product"] == product:
                if new_quantity <= product.stock + item["quantity"]:
                    product.stock += item["quantity"] - new_quantity
                    item["quantity"] = new_quantity
                    print(f"Updated {product.name} quantity to {new_quantity}.")
                else:
                    print(f"Not enough stock available for {product.name}.")
                return
        print(f"{product.name} not found in the cart.")

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            print("Your cart contains:")
            for index, item in enumerate(self.items):
                print(f"{index + 1}. {item['quantity']} {item['product'].name}(s) - ${item['product'].price * item['quantity']:.2f}")

    def calculate_total(self):
        total = sum(item["product"].price * item["quantity"] for item in self.items)
        return total

def display_menu():
    print("\nWelcome to Keith's PC Parts Store!")
    print("1. View Products")
    print("2. View Cart")
    print("3. Checkout")
    print("4. Exit")

def handle_input(prompt, input_type=str):
    try:
        user_input = input(prompt)
        if input_type == int:
            return int(user_input)
        return user_input
    except ValueError:
        return None

def main():
    invalid_attempts = 0
    # Separate product categories
    cpus = [
        Product("AMD Ryzen 5 5600X", 199.99, 15),
        Product("Intel Core i5-12600K", 289.99, 10),
        Product("Intel Core i9-13900K", 589.99, 8),
        Product("AMD Ryzen 9 7950X", 699.00, 10),
        Product("Intel Core i7-12700K", 409.99, 5)

    ]
    
    gpus = [
        Product("AMD Radeon RX 6800 XT", 649.99, 7),
        Product("NVIDIA RTX 3080", 699.99, 5),
        Product("NVIDIA RTX 4090", 1599.99, 5),
        Product("AMD Radeon RX 7900 XTX", 999.99, 7),
        Product("NVIDIA RTX 3070", 499.99, 10)

    ]
    
    ram = [
        Product("Corsair Vengeance 16GB DDR4", 79.99, 20),
        Product("G.Skill Ripjaws V 32GB DDR4", 139.99, 10),
        Product("Corsair Vengeance 32GB DDR5", 149.99, 15),
        Product("G.Skill Trident Z 64GB DDR4", 249.99, 12),
        Product("Crucial Ballistix 16GB DDR4", 89.99, 18)

    ]
    
    motherboards = [
        Product("ASUS ROG Strix Z690-E", 299.99, 5),
        Product("MSI MPG B550 Gaming Edge WiFi", 199.99, 8),
        Product("Gigabyte B550 AORUS Elite", 139.99, 10),
        Product("ASRock X570 Phantom Gaming 4", 159.99, 6),
        Product("ASUS TUF Gaming B550-PLUS", 179.99, 5)
    ]

    
    chassis = [
        Product("NZXT H510", 69.99, 15),
        Product("Corsair 4000D Airflow", 89.99, 10),
        Product("Fractal Design Meshify C", 89.99, 8),
        Product("Cooler Master MasterBox Q300L", 69.99, 12),
        Product("Thermaltake V200", 79.99, 10)
    ]


    categories = {
        "CPUs": cpus,
        "GPUs": gpus,
        "RAM": ram,
        "Motherboards": motherboards,
        "Chassis": chassis

    }

    cart = ShoppingCart()

    while True:
        display_menu()
        choice = handle_input("Enter your choice: ", int)
        if choice is None or choice < 1 or choice > 4:
            invalid_attempts += 1
            if invalid_attempts >= 5:
                print("Too many invalid inputs. Closing the shop.")
                return
            print(f"Invalid choice. Please select a number between 1 and 4. You have {5 - invalid_attempts} attempts remaining.")
            continue

        if choice == 1:
            while True:
                print("\nAvailable Categories:")
                for i, category in enumerate(categories.keys(), 1):
                    print(f"{i}. {category}")
                cat_choice = handle_input("Select a category (or 0 to return): ", int)
                if cat_choice == 0:
                    break
                if cat_choice is None or cat_choice < 1 or cat_choice > len(categories):
                    print("Invalid category selection. Please try again.")
                    continue
                
                selected_category = list(categories.keys())[cat_choice - 1]
                print(f"\nAvailable {selected_category}:")
                for i, product in enumerate(categories[selected_category], 1):
                    print(f"{i}. {product.name} - ${product.price:.2f} (In Stock: {product.stock})")
                
                prod_choice = handle_input("Select a product to add to cart (or 0 to return): ", int)
                if prod_choice == 0:
                    continue
                if prod_choice is None or prod_choice < 1 or prod_choice > len(categories[selected_category]):
                    print("Invalid product selection. Please try again.")
                    continue
                
                product = categories[selected_category][prod_choice - 1]
                quantity = handle_input(f"Enter quantity to add (Max: {product.stock}): ", int)
                if quantity is None or quantity < 1:
                    print("Invalid quantity. Please try again.")
                    continue

                cart.add_item(product, quantity)

        elif choice == 2:
            if not cart.items:
                print("Your cart is empty.")
                continue
            
            cart.view_cart()
            product_choice = handle_input("Select a product from the cart (or 0 to return): ", int)
            if product_choice == 0:
                continue
            if product_choice is None or product_choice < 1 or product_choice > len(cart.items):
                print("Invalid selection. Please try again.")
                continue
            
            selected_item = cart.items[product_choice - 1]
            print(f"\nSelected Product: {selected_item['product'].name} - Quantity: {selected_item['quantity']}")
            print("Options:")
            print("1. Edit Quantity")
            print("2. Remove from Cart")
            action_choice = handle_input("Choose an option: ", int)
            if action_choice == 1:
                new_quantity = handle_input(f"Enter new quantity (Max: {selected_item['product'].stock + selected_item['quantity']}): ", int)
                if new_quantity is not None and new_quantity >= 0:
                    cart.update_item_quantity(selected_item['product'], new_quantity)
                else:
                    print("Invalid quantity. Returning to cart.")
            elif action_choice == 2:
                cart.remove_item(selected_item['product'])
            else:
                print("Invalid choice. Returning to cart.")
        
        elif choice == 3:
            total = cart.calculate_total()
            print(f"\nTotal amount to pay: ${total:.2f}")
            print("Thank you for shopping with us!")
            break
        elif choice == 4:
            print("Thank you for visiting the shop!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
