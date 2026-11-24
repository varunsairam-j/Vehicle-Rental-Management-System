# Vehicle Rental Management System



## Project Overview



The Vehicle Rental Management System is a Python-based application developed to manage vehicle rentals efficiently. The system allows users to view vehicle availability, register customers, book vehicles, calculate rental charges, process vehicle returns, and maintain rental records.



The project is designed using Object-Oriented Programming concepts and demonstrates inheritance, method overriding, polymorphism, and encapsulation. It also uses exception handling, file handling, functions, and modular programming.



## Key Features



- Vehicle availability management

- Car and Bike categories

- Customer registration and record storage

- Vehicle booking

- Rental duration and price calculation

- Vehicle return processing

- Late return charge calculation

- Rental transaction history

- Persistent customer records

- Persistent vehicle rental status

- Input validation and exception handling



## Technologies Used



- Python 3.x

- Object-Oriented Programming

- Exception Handling

- File Handling

- Modular Programming



## OOP Concepts Used



### Inheritance

Car and Bike classes inherit common properties from the Vehicle class.



### Method Overriding

Car and Bike classes provide their own implementation of the `rent_price()` method.



### Polymorphism

The same `rent_price()` method calculates different rental amounts based on the vehicle type.



### Encapsulation

Vehicle and customer data and their related methods are organized within classes.



## Project Structure


Vehicle-Rental-Management-System

│

├── Main.py

├── Vehicle_Customer.py

├── Vehicle_Data.py

├── Booking.py

├── Return_Vehicle.py

├── customers.txt

├── vehicle_status.txt

└── rental_summary.txt

