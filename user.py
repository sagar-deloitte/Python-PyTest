import admin


def register():
    Username = input("Enter a username:")
    Password1 = input("Create password:")
    Password2 = input("Confirm Password:")
    db = open("database/userDatabase.txt", "r")
    dataArray = []
    for i in db:
        key, value = i.split(",")
        value = value.strip()
        c = key, value
        dataArray.append(key)
    if not len(Password1) <= 8:
        db = open("database/userDatabase.txt", "r")
        if not Username is None:
            if len(Username) < 1:
                print("Please provide a username")
                register()
            elif Username in dataArray:
                print("Username exists")
                register()
            else:
                if Password1 == Password2:
                    db = open("database/userDatabase.txt", "a")
                    db.write(Username + ", " + str(Password1) + "\n")
                    print("User created successfully!")
                    print("Please login to proceed:")

                else:
                    print("Passwords do not match")
                    register()
    else:
        print("Password too short")


def welcome():
    print("Welcome to your dashboard")


def userLogin():
    Username = input("Enter your username:")
    Password = input("Enter your Password:")

    if not len(Username or Password) < 1:
        if True:
            db = open("database/userDatabase.txt", "r")
            dataArray = []
            passData = []
            for i in db:
                key, value = i.split(",")
                value = value.strip()
                dataArray.append(key)
                passData.append(value)
                data = dict(zip(dataArray, passData))
            try:
                if Username in data:
                    hashed = data[Username].strip('value')
                    hashed = hashed.replace("'", "")
                    try:
                        if Password == hashed:

                            print("Login success!")
                            print("Hi", Username)
                            welcome()
                            welcomeUser()
                        else:
                            print("Wrong username or password")

                    except:
                        print("Failure")
                else:
                    print("Username doesn't exist")
            except:
                print("Password or username doesn't exist")
        else:
            print("Error logging into the system")

    else:
        print("Please attempt login again")
        userLogin()


def home():
    print("******Welcome to BookMyShow*******")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    option = int(input("Enter your option:"))
    if option == 1:
        register()
    elif option == 2:
        print("1. Admin Login")
        print("2. User Login")
        option = int(input("Enter your option:"))
        if option == 1:
            admin.adminLogin()
        elif option == 2:
            userLogin()
        else:
            print("Please enter a valid option")
    elif option == 3:
        exit()
    else:
        print("Please enter a valid option")

def bookTicket():
    bookTicket.availableSeats = 60
    print("Available number of seats are ", bookTicket.availableSeats)
    bookSeats = int(input("Number of seat you want to book:"))
    bookTicket.availableSeats = int(bookTicket.availableSeats)-bookSeats
    print("Thanks for booking")
    welcomeUser()


def cancelTicket():
    cancelSeats = int(input("Number of seats you want to cancel:"))
    bookTicket.availableSeats = int(bookTicket.availableSeats)+cancelSeats
    print("Available seats: "+bookTicket.availableSeats)


def welcomeUser():
    print("1. Jaws")
    print("2. Robot")
    print("3. Cancel ticket")
    option = input("Enter option:")
    if option == "1":
        data = open("database/movieDatabase.txt","r")
        for i in data:
            print(i)
        bookTicket()
    elif option == "3":
        cancelTicket()


home()
