
def show_homepage():
    """Prints donation homepage with options"""

    print("       === DonateMe Homepage ===       ")
    print("---------------------------------------")
    print("|   1. Login    |   2. Register       |")
    print("---------------------------------------")
    print("|   3. Donate   |   4. Show Donations |")
    print("---------------------------------------")
    print("|             5. Exit                 |")
    print("---------------------------------------\n")


def donate(username):
    """Takes user donation input, concats with username to new variable. Returns new variable"""

    donation_amt = input("Enter amount to donate: ")

    donation_string = username + " donated $" + str(donation_amt)
    print("Thank you for the donation!")
    return donation_string


def show_donations(donations):
    """Prints donation list"""

    print("\n ------ All Donations -----")
    if donations == []:
        print("Currently, there are no donations. Be the first!")
    else:
        for d in donations:
            total = d
            print(d)
