
from Vehicle_Customer import Car, Bike

# Vehicle List
vehicles = [Car("C001", "Toyota", "Innova Crysta", 2024),
            Car("C002", "Hyundai", "Creta", 2024),
            Car("C003", "Maruti", "Swift", 2023),
            Car("C004", "Honda", "City", 2024),
            Car("C005", "Tata", "Nexon", 2023),
            Bike("B001", "Royal Enfield", "Classic 350", 2024),
            Bike("B002", "Yamaha", "MT-15", 2024),
            Bike("B003", "Honda", "Activa 6G", 2023),
            Bike("B004", "TVS", "Apache RTR", 2024),
            Bike("B005", "Bajaj", "Pulsar", 2023)]

# Display Vehicles 
def show_vehicles():
    print("\nID     Brand           Model              Status")
    print("-" * 50)

    for v in vehicles:
        status = "Available" if v.available else "Rented"
        print(f"{v.vehicle_id:<6} {v.brand:<15} {v.model:<18} {status}")

# Load Vehicle Status
def load_vehicle_status():
    try:
        with open("vehicle_status.txt", "r") as file:
            for line in file:
                vehicle_id, available, rented_days = line.strip().split(" - ")

                for v in vehicles:
                    if v.vehicle_id == vehicle_id:
                        v.available = available == "True"
                        v.rented_days = int(rented_days)
    except FileNotFoundError:
        pass
