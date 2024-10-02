# Reservation class
class Reservation:
    # Initializes the reservation details like ID, customer name, email, and room type
    def __init__(self, reservationID, customerName, email, roomType):
        self.reservationID = reservationID
        self.customerName = customerName
        self.email = email
        self.roomType = roomType

    # Gets the reservation ID
    def get_reservationID(self):
        return self.reservationID

    # Sets a new reservation ID
    def set_reservationID(self, reservationID):
        self.reservationID = reservationID

    # Gets the customer's name
    def get_customerName(self):
        return self.customerName

    # Updates the customer's name
    def set_customerName(self, customerName):
        self.customerName = customerName

    # Gets the customer's email
    def get_email(self):
        return self.email

    # Updates the customer's email
    def set_email(self, email):
        self.email = email

    # Gets the room type for the reservation
    def get_roomType(self):
        return self.roomType

    # Sets a new room type for the reservation
    def set_roomType(self, roomType):
        self.roomType = roomType


# Payment class
class Payment:
    # Initializes the payment with billing name, credit card number, room cost, and total amount
    def __init__(self, billingName, creditCardNumber, roomCost, totalAmount):
        self.billingName = billingName
        self.creditCardNumber = creditCardNumber
        self.roomCost = roomCost
        self.totalAmount = totalAmount

    # Gets the billing name
    def get_billingName(self):
        return self.billingName

    # Updates the billing name
    def set_billingName(self, billingName):
        self.billingName = billingName

    # Gets the last four digits of the credit card number
    def get_creditCardNumber(self):
        return self.creditCardNumber

    # Updates the credit card number
    def set_creditCardNumber(self, creditCardNumber):
        self.creditCardNumber = creditCardNumber

    # Gets the cost of the room
    def get_roomCost(self):
        return self.roomCost

    # Updates the room cost
    def set_roomCost(self, roomCost):
        self.roomCost = roomCost

    # Gets the total amount to be paid
    def get_totalAmount(self):
        return self.totalAmount

    # Updates the total amount
    def set_totalAmount(self, totalAmount):
        self.totalAmount = totalAmount


# Room class
class Room:
    # Initializes the room with its number, type, price, and features
    def __init__(self, roomNumber, roomType, price, features):
        self.roomNumber = roomNumber
        self.roomType = roomType
        self.price = price
        self.features = features

    # Gets the room number
    def get_roomNumber(self):
        return self.roomNumber

    # Updates the room number
    def set_roomNumber(self, roomNumber):
        self.roomNumber = roomNumber

    # Gets the room type (like suite or queen)
    def get_roomType(self):
        return self.roomType

    # Updates the room type
    def set_roomType(self, roomType):
        self.roomType = roomType

    # Gets the price per night for the room
    def get_price(self):
        return self.price

    # Updates the price of the room
    def set_price(self, price):
        self.price = price

    # Gets the list of features in the room
    def get_features(self):
        return self.features

    # Updates the features of the room
    def set_features(self, features):
        self.features = features


# Customer class
class Customer:
    # Initializes the customer details like ID, name, email, phone number, and address
    def __init__(self, customerID, name, email, phoneNumber, address):
        self.customerID = customerID
        self.name = name
        self.email = email
        self.phoneNumber = phoneNumber
        self.address = address

    # Gets the customer ID
    def get_customerID(self):
        return self.customerID

    # Updates the customer ID
    def set_customerID(self, customerID):
        self.customerID = customerID

    # Gets the customer's name
    def get_name(self):
        return self.name

    # Updates the customer's name
    def set_name(self, name):
        self.name = name

    # Gets the customer's email
    def get_email(self):
        return self.email

    # Updates the customer's email
    def set_email(self, email):
        self.email = email

    # Gets the customer's phone number
    def get_phoneNumber(self):
        return self.phoneNumber

    # Updates the customer's phone number
    def set_phoneNumber(self, phoneNumber):
        self.phoneNumber = phoneNumber

    # Gets the customer's address
    def get_address(self):
        return self.address

    # Updates the customer's address
    def set_address(self, address):
        self.address = address


# Example of creating objects and using getter/setter methods

# Creating a reservation object
reservation = Reservation(123, "Ted Vera", "tedvera@mac.com", "2 Queen Beds")
print("Reservation ID:", reservation.get_reservationID())
print("Customer Name:", reservation.get_customerName())

# Modifying the reservation
reservation.set_customerName("John Doe")
print("Updated Customer Name:", reservation.get_customerName())

# Creating a payment object
payment = Payment("Ted Vera", "9504", 59.95, 201.48)
print("Billing Name:", payment.get_billingName())
print("Total Amount:", payment.get_totalAmount())

# Creating a room object
room = Room(101, "Suite", 99.99, ["TV", "Wi-Fi", "Mini Bar"])
print("Room Number:", room.get_roomNumber())
print("Room Features:", room.get_features())

# Creating a customer object
customer = Customer(1, "Ted Vera", "tedvera@mac.com", "123-456-7890", "123 Main St")
print("Customer Email:", customer.get_email())
print("Customer Address:", customer.get_address())

# Updating the customer's phone number
customer.set_phoneNumber("800-588-2300")
print("Updated Phone Number:", customer.get_phoneNumber())

# Reservation information
reservation = Reservation("15549850358", "Ted Vera", "tedvera@mac.com", "2 Queen Beds / No Smoking / Desk / Safe / Coffee Maker / Hair Dryer")

# Payment information
payment = Payment("Ted H Vera", "9904", 89.95, 201.48)

# Room information
room = Room(1, "2 Queen Beds", 89.95, ["No Smoking", "Desk", "Safe", "Coffee Maker", "Hair Dryer"])

# Customer information
customer = Customer(101, "Ted Vera", "tedvera@mac.com", "505-661-1110", "2455 Trinity Drive, Los Alamos, NM 87544")

# Displaying the reservation information
print("Your Reservation Is Confirmed")
print("Your Name: " + customer.get_name())
print("Your Email: " + customer.get_email())
print("Priceline Trip Number: " + reservation.get_reservationID())
print("Hotel Confirmation Number: 52523687\n")

print("Hotel: Comfort Inn & Suites Los Alamos")
print("Address: " + customer.get_address())
print("Phone: " + customer.get_phoneNumber())
print("Check-In: Sun, Aug 22, 2010 - 03:00 PM")
print("Check-Out: Tue, Aug 24, 2010 - 12:00 PM")
print("Number of Rooms: " + str(room.get_roomNumber()))
print("Room Type: " + room.get_roomType())
print("Features: " + ", ".join(room.get_features()) + "\n")

# Summary of charges
print("Summary of Charges")
print("Billing Name: " + payment.get_billingName())
print("Credit Card: Mastercard (ending in " + payment.get_creditCardNumber() + ")")
print("Room Cost (per night):", payment.get_roomCost())
print("Rooms: 1")
print("Nights: 2")
print("Room Subtotal:", payment.get_roomCost() * 2)
print("Taxes and Fees: $21.58")
print("Total Charges:", payment.get_totalAmount())
