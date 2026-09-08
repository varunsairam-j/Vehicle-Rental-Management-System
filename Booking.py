
from Vehicle_Customer import customers
from Vehicle_Data import vehicles, show_vehicles

# Book Vehicle
def book_vehicle():
    show_vehicles()

    vehicle_id = input("\nEnter Vehicle ID: ")
    customer_id = input("Enter Customer ID: ")

    vehicle = None
    customer = None

    for v in vehicles:
        if v.vehicle_id == vehicle_id:
            vehicle = v

    for c in customers:
        if c.customer_id == customer_id:
            customer = c

    try:
        if vehicle is None:
            raise Exception("Vehicle not found!")

        if customer is None:
            raise Exception("Customer not found!")

        if not vehicle.available:
            raise Exception("Vehicle is already rented!")

        days = int(input("Enter rental days: "))

        if days <= 0:
            raise Exception("Days must be greater than 0!")

        price = vehicle.rent_price(days)
        vehicle.rented_days = days
        vehicle.available = False

        with open("vehicle_status.txt", "w") as file:
            for v in vehicles:
                file.write(f"{v.vehicle_id} - {v.available} - {v.rented_days}\n")

        print("\n----- BOOKING SUCCESSFUL -----")
        print("Customer :", customer.name)
        print("Vehicle  :", vehicle.brand, vehicle.model)
        print("Days     :", days)
        print("Amount   :", price)

        with open("rental_summary.txt", "a") as file:
            file.write(f"\n{customer.customer_id} - {customer.name} - {vehicle.vehicle_id} - {vehicle.model} - {days} days - Rs.{price}\n")

    except ValueError:
        print("Please enter a valid number!")
    except Exception as e:
        print(f"\n{e}")
