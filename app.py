from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register

database = {"admin": "password123"}
donations = []
authorized_user = ""


while True:
    show_homepage()

    if authorized_user == "":  # Makes sure user is logged in
        print("You must be logged in to donate.\n")

    else:
        print("Logged in as: ", authorized_user)
    option = input("Select an option: ")

    if option == "1":  # Login
        username = input("Enter username: ")
        password = input("Enter password: ")
        username = username.lower()
        authorized_user = login(database, username, password)

    elif option == "2":  # Register
        username = input("Create a username: ")
        password = input("Create a password: ")
        username = username.lower()
        authorized_user = register(database, username)
        if authorized_user != "":
            database[authorized_user] = password

    elif option == "3":  # Donate
        if authorized_user == "":
            print("You must be logged in to donate.\n")
        else:
            donation_string = donate(authorized_user)
            donations.append(donation_string)

    elif option == "4":  # Show donation
        show_donations(donations)

    elif option == "5":  # Exit
        quit()

    else:  # Catches all other inputs.
        print("Please select an option from the menu.")
