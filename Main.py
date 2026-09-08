
from Vehicle_Customer import register_customer, load_customers
from Vehicle_Data import show_vehicles, load_vehicle_status
from Booking import book_vehicle
from Return_Vehicle import return_vehicle

load_customers()
load_vehicle_status()

# Main Menu
while True:
    print("\n===== VEHICLE RENTAL SYSTEM =====")
    print("\n1. Show Vehicles")
    print("2. Register Customer")
    print("3. Book Vehicle")
    print("4. Return Vehicle")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        show_vehicles()

    elif choice == "2":
        register_customer()

    elif choice == "3":
        book_vehicle()

    elif choice == "4":
        return_vehicle()

    elif choice == "5":
        print("\nThank you!")
        break

    else:
        print("Invalid choice!")
