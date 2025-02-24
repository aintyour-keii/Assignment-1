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

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            print("Your cart contains:")
            for item in self.items:
                print(f"{item['quantity']} {item['product'].name}(s) - ${item['product'].price * item['quantity']:.2f}")
            
            print("\nCart Options:")
            print("1. Add Item to Cart")
            print("2. Remove Item from Cart")
            print("3. Return to Main Menu")
            
            action_choice = input("\nWould you like to add an item to the cart or return to the main menu? (add/return): ")
            if action_choice.lower() == "add":
                return 1
            elif action_choice.lower() == "return":
                return 3
            else:
                print("Invalid choice. Returning to main menu.")
                return 3

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
        choice = handleadd_input("Enter your choice: ", int)
        if choice is None or choice < 1 or choice > 4:
            invalid_attempts += 1
            if invalid_attempts >= 5:
                print("Too many invalid inputs. Closing the shop.")
                return
            print(f"Invalid choice. Please select a number between 1 and 4. You have {5 - invalid_attempts} attempts remaining.")
            continue


        if choice == 1:
            print("\nAvailable Products:")
            for category, products in categories.items():
                print(f"\n{category}:")
                for product in products:
                    print(f"  {product.name} - ${product.price:.2f} (In Stock: {product.stock})")

        elif choice == 2:
            cart.view_cart()
            cart_choice = handle_input("Enter your cart option: ", int)
            if cart_choice is None or cart_choice < 1 or cart_choice > 3:
                invalid_attempts += 1
                if invalid_attempts >= 5:
                    print("Too many invalid inputs. Closing the shop.")
                    return
                print(f"Invalid choice. Please select a number between 1 and 3. You have {5 - invalid_attempts} attempts remaining.")
                continue

            
            if cart_choice == 1:
                print("\nSelect a category:")
                for i, category in enumerate(categories.keys(), 1):
                    print(f"{i}. {category}")
                cat_choice = handle_input("Enter category number: ", int)
                if cat_choice is None:
                    invalid_attempts += 1
                    if invalid_attempts >= 5:
                        print("Too many invalid inputs. Closing the shop.")
                        return
                    print(f"Invalid input. You have {5 - invalid_attempts} attempts remaining.")
                    continue
                cat_choice -= 1
                selected_category = list(categories.keys())[cat_choice]
                
                print(f"\nAvailable {selected_category}:")
                for i, product in enumerate(categories[selected_category], 1):
                    print(f"{i}. {product.name} - ${product.price:.2f} (In Stock: {product.stock})")
                    
                prod_choice = handle_input("Enter product number: ", int)
                if prod_choice is None:
                    invalid_attempts += 1
                    if invalid_attempts >= 5:
                        print("Too many invalid inputs. Closing the shop.")
                        return
                    print(f"Invalid input. You have {5 - invalid_attempts} attempts remaining.")
                    continue
                prod_choice -= 1
                product = categories[selected_category][prod_choice]
                quantity = handle_input(f"Enter quantity to add (Max: {product.stock}): ", int)
                if quantity is None:
                    invalid_attempts += 1
                    if invalid_attempts >= 5:
                        print("Too many invalid inputs. Closing the shop.")
                        return
                    print(f"Invalid input. You have {5 - invalid_attempts} attempts remaining.")
                    continue

                if product:
                    cart.add_item(product, quantity)
                else:
                    print("Product not found.")
            elif cart_choice == 2:
                print("\nSelect a category:")
                for i, category in enumerate(categories.keys(), 1):
                    print(f"{i}. {category}")
                cat_choice = handle_input("Enter category number: ", int)
                if cat_choice is None:
                    invalid_attempts += 1
                    if invalid_attempts >= 5:
                        print("Too many invalid inputs. Closing the shop.")
                        return
                    print(f"Invalid input. You have {5 - invalid_attempts} attempts remaining.")
                    continue
                cat_choice -= 1
                selected_category = list(categories.keys())[cat_choice]
                
                print(f"\nAvailable {selected_category}:")
                for i, product in enumerate(categories[selected_category], 1):
                    print(f"{i}. {product.name} - ${product.price:.2f} (In Stock: {product.stock})")
                    
                prod_choice = handle_input("Enter product number: ", int)
                if prod_choice is None:
                    invalid_attempts += 1
                    if invalid_attempts >= 5:
                        print("Too many invalid inputs. Closing the shop.")
                        return
                    print(f"Invalid input. You have {5 - invalid_attempts} attempts remaining.")
                    continue
                prod_choice -= 1
                product = categories[selected_category][prod_choice]

                if product:
                    cart.remove_item(product)
                else:
                    print("Product not found.")
            elif cart_choice == 3:
                continue
            else:
                print("Invalid choice. Returning to main menu.")

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
