class Snack:
    def __init__(self, snack_id, name, price, available):
        self.snack_id = snack_id
        self.name = name
        self.price = price
        self.available = available

class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_snack(self, snack_id, name, price, available):
        snack = Snack(snack_id, name, price, available)
        self.inventory[snack_id] = snack

    def remove_snack(self, snack_id):
        if snack_id in self.inventory:
            del self.inventory[snack_id]

    def update_snack_availability(self, snack_id, new_availability):
        if snack_id in self.inventory:
            self.inventory[snack_id].available = new_availability

class SalesRecord:
    def __init__(self):
        self.sales_record = []

    def record_sale(self, snack_id, inventory):
        if snack_id in inventory.inventory:
            snack = inventory.inventory[snack_id]
            if snack.available:
                self.sales_record.append(snack_id)
                inventory.update_snack_availability(snack_id, False)
            else:
                print("Snack is not available for sale.")
        else:
            print("Snack not found in the inventory.")

# Create instances of the Inventory and SalesRecord classes
inventory = Inventory()
sales_record = SalesRecord()

# Allow users to add snacks with custom attributes
while True:
    print("1. Add a snack")
    print("2. Remove a snack")
    print("3. Update snack availability")
    print("4. Record a sale")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        snack_id = int(input("Enter snack ID: "))
        name = input("Enter snack name: ")
        price = float(input("Enter snack price: "))
        available = input("Is the snack available (yes/no): ").lower() == 'yes'
        inventory.add_snack(snack_id, name, price, available)
        print("Snack added to inventory.")

    elif choice == '2':
        snack_id = int(input("Enter snack ID to remove: "))
        inventory.remove_snack(snack_id)
        print("Snack removed from inventory.")

    elif choice == '3':
        snack_id = int(input("Enter snack ID to update availability: "))
        new_availability = input("Is the snack available (yes/no): ").lower() == 'yes'
        inventory.update_snack_availability(snack_id, new_availability)
        print("Availability updated.")

    elif choice == '4':
        snack_id = int(input("Enter snack ID for the sale: "))
        sales_record.record_sale(snack_id, inventory)
        print("Sale recorded.")

    elif choice == '5':
        break

# Display the current inventory
print("Current Inventory:")
for snack_id, snack in inventory.inventory.items():
    print(f"Snack ID: {snack_id}, Name: {snack.name}, Price: {snack.price}, Available: {snack.available}")

# Display the sales record
print("Sales Record:")
for snack_id in sales_record.sales_record:
    snack = inventory.inventory.get(snack_id)
    if snack:
        print(f"Snack ID: {snack_id}, Name: {snack.name}, Price: {snack.price}")
