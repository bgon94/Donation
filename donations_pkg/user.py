def login(database, username, password):
    """Makes sure username and password matches whats in database. Returns username."""

    for key in database:
        if username == key and password == database[key]:
            print("Login Successful.  Welcome ", username, "\n")
            return username

    print("Username or password is incorrect.  If you do not have an account, please Register. \n")
    return ""


def register(database, username):
    """Checks to make sure username is not already created, returns username"""
    for key in database:
        if username == key:
            print("Username already exists\n")
            return ""
    print("Username has been registered\n")
    return username
