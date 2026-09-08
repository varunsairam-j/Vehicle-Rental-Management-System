
from Vehicle_Data import vehicles

# Return Vehicle
def return_vehicle():
    vehicle_id = input("Enter Vehicle ID: ")

    for v in vehicles:
        if v.vehicle_id == vehicle_id:
            if v.available:
                print("\nThis vehicle is not rented.")
                return

            actual_days = int(input("Enter actual days used: "))
            late_days = actual_days - v.rented_days

            if late_days > 0:
                late_charge = late_days * 300
            else:
                late_charge = 0
                
            v.available = True
            v.rented_days = 0

            with open("vehicle_status.txt", "w") as file:
                for vehicle in vehicles:
                    file.write(f"{vehicle.vehicle_id} - {vehicle.available} - {vehicle.rented_days}\n")
            
            print("\n----- RETURN SUMMARY -----")
            print("Vehicle     :", v.model)
            print("Late Days   :", max(late_days, 0))
            print("Late Charge :", late_charge)
            print("\nVehicle returned successfully!")

            with open("rental_summary.txt", "a") as file:
                file.write(f"RETURN - {vehicle_id} - Late Days: {max(late_days, 0)} - Late Charge: Rs.{late_charge}\n")
            return

    print("Vehicle not found!")
