import time
import os

# File name constant
FILE_NAME = "LHMS_850003145.txt"

# Add a new room to the room list
def add_room(room_list):
    room_id = input("Enter Room ID: ")
    room_type = input("Enter Room Type (Single/Double/Suite): ")
    while True:
        try:
            room_price = float(input("Enter Room Price: "))
            break
        except ValueError:
            print("Invalid price. Please enter a valid number.")
    room_list.append({"Room ID": room_id, "Room Type": room_type, "Price": room_price, "Allocated": False})
    print("Room added successfully.")

# Remove a room from the room list
def delete_room(room_list):
    room_id = input("Enter Room ID to delete: ")
    for room in room_list:
        if room["Room ID"] == room_id:
            if room.get("Allocated", False):
                print(f"Room {room_id} is currently allocated and cannot be deleted.")
                return
            room_list.remove(room)
            print(f"Room {room_id} deleted.")
            return
    print(f"Room {room_id} not found.")

# Display details of all rooms
def display_rooms(room_list):
    if not room_list:
        print("No rooms available.")
    else:
        for room in room_list:
            status = "Allocated" if room.get("Allocated", False) else "Available"
            print(f"Room ID: {room['Room ID']}, Type: {room['Room Type']}, Price: ${room['Price']}, Status: {status}")

# Allocate a room to a customer
def allocate_room(room_list, allocation_list):
    room_id = input("Enter Room ID to allocate: ")
    for room in room_list:
        if room["Room ID"] == room_id:
            if room.get("Allocated", False):
                print(f"Room {room_id} is already allocated.")
                return
            customer_name = input("Enter Customer Name: ")
            allocation_list.append({"Room ID": room_id, "Customer Name": customer_name})
            room["Allocated"] = True
            print(f"Room {room_id} allocated to {customer_name}.")
            return
    print(f"Room {room_id} not available.")

# Display details of room allocations
def display_allocation_details(allocation_list):
    if not allocation_list:
        print("No rooms allocated.")
    else:
        for allocation in allocation_list:
            print(f"Room ID: {allocation['Room ID']}, Allocated to: {allocation['Customer Name']}")

# Handle billing and deallocation of rooms
def billing_and_deallocation(room_list, allocation_list):
    if not allocation_list:
        print("No allocations to deallocate.")
        return

    room_id = input("Enter Room ID to deallocate: ")
    print(f"Room ID {room_id} deallocated successfully.")

    room_found = False
    customer_name = None

    for allocation in allocation_list:
        if allocation["Room ID"] == room_id:
            room_found = True
            customer_name = allocation["Customer Name"]

            for room in room_list:
                if room["Room ID"] == room_id:
                    room["Allocated"] = False
                    allocation_list.remove(allocation)
                    print(f"Room {room_id} deallocated from {customer_name}.")
                    return

            # Handle case where room details are not in the room list
            room_list.append({"Room ID": room_id, "Room Type": "Unknown", "Price": 0, "Allocated": False})
            allocation_list.remove(allocation)
            print(f"Room {room_id} deallocated from {customer_name} with default values.")
            return

    if not room_found:
        print(f"Room {room_id} is not allocated to any customer.")

# Create a backup of room allocation data
def backup_file():
    try:
        backup_file = f"{FILE_NAME.replace('.txt', '')}_Backup_{time.strftime('%Y%m%d_%H%M%S')}.txt"

        if not os.path.exists(FILE_NAME):
            print(f"Error: The file '{FILE_NAME}' does not exist.")
            return

        with open(FILE_NAME, 'r') as file:
            content = file.read()

        if not content.strip():
            print(f"The file '{FILE_NAME}' is empty. Nothing to backup.")
            return

        with open(backup_file, 'w') as backup:  # Use write mode to avoid concatenation
            backup.write(content)

        print(f"Backup successful! Content backed up to: {backup_file}")

    except IOError as e:
        print(f"File operation error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Save room allocation to a file
def save_room_allocation(allocation_list):
    with open(FILE_NAME, 'w') as file:
        for allocation in allocation_list:
            file.write(f"Room ID: {allocation['Room ID']}, Customer: {allocation['Customer Name']}\n")
    print("Room allocation saved to file.")

# Show room allocation details from a file
def show_room_allocation():
    try:
        with open(FILE_NAME, 'r') as file:
            content = file.read()
            if content:
                print("Room Allocation Details:")
                print(content)
            else:
                print("No room allocations found in the file.")
    except FileNotFoundError:
        print(f"The file '{FILE_NAME}' does not exist.")
    except IOError as e:
        print(f"Error reading the file: {e}")

# Main menu to handle hotel management tasks
def hotel_management_menu():
    room_list = []  # List of rooms
    allocation_list = []  # List of allocated rooms

    while True:
        print("\nHotel Management System Menu:")
        print("1. Add Room")
        print("2. Delete Room")
        print("3. Display Rooms Details")
        print("4. Allocate Rooms")
        print("5. Display Room Allocation Details")
        print("6. Billing & De-Allocation")
        print("7. Save the Room Allocation to a File")
        print("8. Show the Room Allocation from a File")
        print("9. Backup the Room Allocation")
        print("0. Exit Application")

        choice = input("Enter your choice (0-9): ")

        if choice == "1":
            add_room(room_list)
        elif choice == "2":
            delete_room(room_list)
        elif choice == "3":
            display_rooms(room_list)
        elif choice == "4":
            allocate_room(room_list, allocation_list)
        elif choice == "5":
            display_allocation_details(allocation_list)
        elif choice == "6":
            billing_and_deallocation(room_list, allocation_list)
        elif choice == "7":
            save_room_allocation(allocation_list)
        elif choice == "8":
            show_room_allocation()
        elif choice == "9":
            backup_file()
        elif choice == "0":
            print("Exiting Application...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Run the application
hotel_management_menu()
