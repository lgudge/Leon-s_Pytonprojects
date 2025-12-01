# The Total seats
TOTAL_SEATS = 20

# Defining the different seats
first_class_seats = {1, 2, 3, 4}
emergency_seats = {9, 10, 11, 12}
first_class_fee = 150.00


taken_seats = set()


def display_seats():
    print("\nSLM Seats Layout")
    for seat in range(1, TOTAL_SEATS + 1):
        status = "TAKEN" if seat in taken_seats else "AVAILABLE"
        seat_type = ""

        if seat in first_class_seats:
            seat_type = "(First Class)"
        elif seat in emergency_seats:
            seat_type = "(Emergency Row)"

        print(f"Seat {seat:2}: {status:10} {seat_type}")



def purchase_seat(seat_num):
    if seat_num in taken_seats:
        print("That seat is already taken. Choose another please.\n")
        return False

    # First_class payment
    if seat_num in first_class_seats:
        print(f"Seat {seat_num} is FIRST CLASS. Fee: ${first_class_fee:.2f}")
        confirm = input("Do you want to continue? Type (yes/no): ").strip().lower()
        if confirm != "yes":
            print("Purchase cancelled.\n")
            return False

    # Emergency row prompt
    if seat_num in emergency_seats:
        print("You selected an EMERGENCY EXIT ROW seat.")
        print("You MUST be able and willing to assist during an emergency.")
        confirm = input("Do you accept this responsibility? Type (yes/no): ").strip().lower()
        if confirm != "yes":
            print("Purchase cancelled.\n")
            return False

    taken_seats.add(seat_num)
    print(f"Seat {seat_num} successfully purchased!\n")
    return True


# Loop
print("Welcome to Suriname Airways Seat Purchase System!")

while True:
    display_seats()

    choice = input("Do you want to purchase a seat? Type (yes/no): ").strip().lower()
    if choice != "yes":
        break

    try:
        seat = int(input(f"Enter a seat number (1–{TOTAL_SEATS}): "))
        if seat < 1 or seat > TOTAL_SEATS:
            print("Invalid seat number.\n")
            continue
    except ValueError:
        print("Please enter a valid number.\n")
        continue

    purchase_seat(seat)

print("\nThank you for using Suriname Airways Seat Purchase System!")
print("Safe travels! And hope you fly with us again.;)")