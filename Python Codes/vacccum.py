# Vacuum Cleaner Problem - User Input Version

def vacuum_cleaner():
    # Taking input for room status
    room = {}
    room["A"] = int(input("Enter status of Room A (1 = Dirty, 0 = Clean): "))
    room["B"] = int(input("Enter status of Room B (1 = Dirty, 0 = Clean): "))

    # Taking input for starting location
    location = input("Enter starting location of vacuum (A/B): ").strip().upper()

    # Cleaning process
    while True:
        print(f"\nVacuum is in Room {location}")

        if room[location] == 1:
            print(f"Room {location} is dirty. Cleaning...")
            room[location] = 0
            print(f"Room {location} is now clean.")
        else:
            print(f"Room {location} is already clean.")

        # Move to the other room
        if location == "A":
            location = "B"
        else:
            location = "A"

        # Stop if all rooms are clean
        if all(value == 0 for value in room.values()):
            print("\nAll rooms are clean. Stopping vacuum.")
            break

# Run the vacuum cleaner
vacuum_cleaner()
