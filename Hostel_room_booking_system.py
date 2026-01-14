bookings = []

def book_room():
    name = input("Enter customer name: ")
    room_type = input("Enter room type: ")
    bookings.append({"name": name, "room_type": room_type})
    print("Room booked successfully")

def view_bookings():
    if not bookings:
        print("No bookings available")
    else:
        for booking in bookings:
            print(booking["name"], "- Room Type:", booking["room_type"])

def main():
    while True:
        print("1. Book Room")
        print("2. View Bookings")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            book_room()
        elif choice == "2":
            view_bookings()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
