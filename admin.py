def editInfo(edit, update):
    with open("database/movieDatabase.txt", "r") as file:
        fileData = file.read()
        fileData = fileData.replace(edit, update)
    with open("database/movieDatabase.txt", "w") as file:
        file.write(fileData)


def adminLogin():
    Username = input("Enter your username:")
    Password = input("Enter your Password:")

    if not len(Username or Password) < 1:
        if True:
            db = open("database/adminDatabase.txt", "r")
            data = []
            passData = []
            for i in db:
                key, value = i.split(",")
                value = value.strip()
                data.append(key)
                passData.append(value)
                data = dict(zip(data, passData))
            try:
                if Username in data:
                    hashed = data[Username].strip('value')
                    hashed = hashed.replace("'", "")

                    try:
                        if Password == hashed:
                            print("Login success!")
                            print("******Welcome ", Username, "*******")
                            adminDashboard()
                        else:
                            print("Wrong password")

                    except:
                        print("Incorrect passwords or username")
                else:
                    print("Username doesn't exist")
            except:
                print("Password or username doesn't exist")
        else:
            print("Error logging into the system")

    else:
        print("Please attempt login again")


def adminDashboard():
    print("1. Add New Movie Info")
    print("2. Edit Movie Info")
    print("3. Delete Movies")
    print("4. Logout")
    option = int(input("Enter your option:"))
    if option == 1:
        addMovie()
    elif option == 2:
        editMovie()
    elif option == 3:
        deleteMovie()
    elif option == 4:
        adminLogout()
    else:
        print("Please enter a valid option")
        adminDashboard()


def addMovie():
    title = input("Title: ")
    genre = input("Genre: ")
    length = input("Length: ")
    cast = input("Cast: ")
    director = input("Director: ")
    rating = input("Admin rating: ")
    language = input("Language: ")
    numberOfShows = input("Number of shows in a day: ")
    firstShow = input("First show: ")
    intervalTime = input("Interval time: ")
    gapBetShow = input("Gap between shows: ")
    capacity = input("Capacity: ")
    # timing = int(length.replace("mins","")) + int(intervalTime.replace("mins","")) + int(gapBetShow.replace("mins",""))+"mins"
    movieInfo = {"Title": title,
                 "Genre": genre,
                 "Length": length,
                 "Cast": cast,
                 "Director": director,
                 "Admin rating": rating,
                 "Language": language,
                 "Number of shows in a day": numberOfShows,
                 "First show": firstShow,
                 "Interval time": intervalTime,
                 "Gap between shows": gapBetShow,
                 "Capacity": capacity}

    with open("database/movieDatabase.txt", 'w') as file:
        for key, value in movieInfo.items():
            file.write('%s:%s\n' % (key, value))
        # file.close()

    adminDashboard()

def editMovie():
    movieData = open("database/movieDatabase.txt", "r")
    movie = input("Enter movie name:")
    query = []
    info = []
    for i in movieData:
        key, value = i.split(":")
        value = value.strip()
        query.append(key)
        info.append(value)
        movieList = dict(zip(query, info))
        movieName = movieList["Title"].strip('value')
    if movie == movieName:
        view = open("database/movieDatabase.txt","r")
        for i in view:
            print(i)
        print("1. Title"+"\n"
              "2. Genre"+"\n"
              "3. Length"+"\n"
              "4. Cast"+"\n"
              "5. Director"+"\n"
              "6. Admin rating"+"\n"
              "7. Number of shows in a day"+"\n"
              "8. First show"+"\n"
              "9. Interval time"+"\n"
              "10. Gap between shows"+"\n"
              "11. Capacity"+"\n")
        option = input("Choose the field you want to edit:")
        if option == "1":
            update = input("Update the Title:")
            edit = movieList["Title"].strip('value')
            editInfo(edit,update)

        if option == "2":
            update = input("Update the Genre:")
            edit = movieList["Genre"].strip('value')
            editInfo(edit,update)

        if option == "3":
            update = input("Update the Length:")
            edit = movieList["Length"].strip('value')
            editInfo(edit,update)

        if option == "4":
            update = input("Update the Cast:")
            edit = movieList["Cast"].strip('value')
            editInfo(edit,update)

        if option == "5":
            update = input("Update the Director:")
            edit = movieList["Director"].strip('value')
            editInfo(edit,update)

        if option == "6":
            update = input("Update the Admin rating:")
            edit = movieList["Admin rating"].strip('value')
            editInfo(edit,update)

        if option == "7":
            update = input("Update the Number of shows:")
            edit = movieList["Number of shows in a day"].strip('value')
            editInfo(edit,update)

        if option == "8":
            update = input("Update the First show:")
            edit = movieList["First show"].strip('value')
            editInfo(edit,update)

        if option == "9":
            update = input("Update the Interval time:")
            edit = movieList["Interval time"].strip('value')
            editInfo(edit,update)

        if option == "10":
            update = input("Update the Gap between shows:")
            edit = movieList["Gap between shows"].strip('value')
            editInfo(edit,update)

        if option == "11":
            update = input("Update the Capacity:")
            edit = movieList["Capacity"].strip('value')
            editInfo(edit,update)

    adminDashboard()


def deleteMovie():
    movieData = open("database/movieDatabase.txt", "r")
    remove = input("Enter the movie title you want to delete:")
    query = []
    info = []
    for i in movieData:
        key, value = i.split(":")
        value = value.strip()
        query.append(key)
        info.append(value)
        movieList = dict(zip(query, info))
        movieName = movieList["Title"].strip('value')
    if movieName == remove:
        file = open("database/movieDatabase.txt","w")
        file.truncate()
    else:
        print("Movie does not exists")

    adminDashboard()

def adminLogout():
    exit()


