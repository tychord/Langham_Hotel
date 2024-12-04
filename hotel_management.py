import time
import os

# Add a new room to the room list
def add_room(room_list):
    room_id = input("Enter Room ID: ")
    room_type = input("Enter Room Type (Single/Double/Suite): ")
    room_price = float(input("Enter Room Price: "))
    room_list.append({"Room ID": room_id, "Room Type": room_type, "Price": room_price})
    print("Room added successfully.")

# Remove a room from the room list
def delete_room(room_list):
    room_id = input("Enter Room ID to delete: ")
    for room in room_list:
        if room["Room ID"] == room_id:
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
            print(f"Room ID: {room['Room ID']}, Type: {room['Room Type']}, Price: ${room['Price']}")

# Allocate a room to a customer
def allocate_room(room_list, allocation_list):
    room_id = input("Enter Room ID to allocate: ")
    for room in room_list:
        if room["Room ID"] == room_id:
            customer_name = input("Enter Customer Name: ")
            allocation_list.append({"Room ID": room_id, "Customer Name": customer_name})
            room_list.remove(room)
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
    room_id = input("Enter Room ID to deallocate: ")

    # Output the room ID entered
    print(f" Room ID {room_id} Deallocated Sucessfully: ")
    
    # Check if the room ID is allocated to a customer
    room_found = False
    customer_name = None  # Initialize customer_name here
    
    for allocation in allocation_list:
        if allocation["Room ID"] == room_id:
            room_found = True
            customer_name = allocation["Customer Name"]  # Assign the customer name
            
            # Find the room in the original list (room_list) to get the price
            for room in room_list:
                if room["Room ID"] == room_id:
                    print(f"Room {room_id} deallocated from {customer_name}.")
                    room_list.append({"Room ID": room_id, "Room Type": "Unknown", "Price": room['Price']})
                    allocation_list.remove(allocation)  # Remove from the allocation list
                    print(f"Room {room_id} deallocated successfully.")
                    return

    if not room_found:
        print(f"Room {room_id} is not allocated to any customer.")

# Create a backup of room allocation data
def backup_file():
    try:
        # File paths
        original_file = "LHMS_Studentid.txt"
        backup_file = f"LHMS_Studentid_Backup_{time.strftime('%Y%m%d_%H%M%S')}.txt"

        # Ensure the file exists
        if not os.path.exists(original_file):
            print(f"Error: The file '{original_file}' does not exist.")
            return

        # Read the file and create a backup
        with open(original_file, 'r') as file:
            content = file.read()

        if not content.strip():
            print(f"The file '{original_file}' is empty. Nothing to backup.")
            return

        with open(backup_file, 'a') as backup:
            backup.write(content)

        print(f"Backup successful! Content backed up to: {backup_file}")

        # Clear original file content
        with open(original_file, 'w') as file:
            file.truncate(0)
        print(f"Original file '{original_file}' content cleared.")

    except IOError as e:
        print(f"File operation error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Save room allocation to a file
def save_room_allocation(allocation_list):
    with open("LHMS_Studentid.txt", 'w') as file:
        for allocation in allocation_list:
            file.write(f"Room ID: {allocation['Room ID']}, Customer: {allocation['Customer Name']}\n")
    print("Room allocation saved to file.")

# Show room allocation details from a file
def show_room_allocation():
    try:
        with open("LHMS_Studentid.txt", 'r') as file:
            content = file.read()
            if content:
                print("Room Allocation Details:")
                print(content)
            else:
                print("No room allocations found in the file.")
    except FileNotFoundError:
        print("The file 'LHMS_Studentid.txt' does not exist.")
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
