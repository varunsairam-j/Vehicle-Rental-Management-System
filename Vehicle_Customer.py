
# Parent Class
class Vehicle:
    def __init__(self, vehicle_id, brand, model, year):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.year = year
        self.available = True
        self.rented_days = 0

    def rent_price(self, days):
        return 0

# Child Class
class Car(Vehicle):
    def rent_price(self, days):
        return days * 1500

# Child Class
class Bike(Vehicle):
    def rent_price(self, days):
        return days * 700


# Customer Class
class Customer:
    def __init__(self, customer_id, name, phone):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone

customers = []

# Register Customer
def register_customer():
    cid = input("\nEnter Customer ID: ")
    name = input("Enter Customer Name: ")
    phone = input("Enter Phone Number: ")

    customers.append(Customer(cid, name, phone))

    with open("customers.txt", "a") as file:
        file.write(f"{cid} - {name} - {phone}\n")

    print("\nCustomer registered successfully!")

# Load Existing Customers
def load_customers():
    try:
        with open("customers.txt", "r") as file:
            for line in file:
                cid, name, phone = line.strip().split(" - ")
                customers.append(Customer(cid, name, phone))
    except FileNotFoundError:
        pass
