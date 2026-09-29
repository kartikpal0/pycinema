from cinema import storage
from cinema.auth import login
from cinema.log_setup import get_logger

log = get_logger()
DEFAULT = ["Interstellar", "Se7en", "Tenet", "Shutter Island"]


def get_movies():
    return storage.load("movies.json", list(DEFAULT))


def add_movie(name):
    movies = get_movies()
    if name.strip() == "":
        return False
    if name in movies:
        return False
    movies.append(name)
    storage.save("movies.json", movies)
    log.info("Movie added: %s", name)
    return True


def remove_movie(name):
    movies = get_movies()
    if name not in movies:
        return False
    movies.remove(name)
    storage.save("movies.json", movies)
    log.info("Movie removed: %s", name)
    return True


def manage_movies():
    if not login():
        print("Incorrect ID or Password")
        return
    print("Welcome sir!")
    while True:
        print("\n== Movie Menu ==")
        print("1. Add Movie")
        print("2. Remove Movie")
        print("3. View Movies")
        print("4. Log Out")
        choice = input("Enter the command: ")
        if choice == "1":
            if add_movie(input("Enter movie name: ")):
                print("Movie Added Successfully!")
            else:
                print("Movie name empty or already exists!")
        elif choice == "2":
            if remove_movie(input("Enter movie name: ")):
                print("Movie Removed Successfully!")
            else:
                print("Movie Not Found!")
        elif choice == "3":
            movies = get_movies()
            if not movies:
                print("No movie is available. Add movies.")
            for i, m in enumerate(movies, 1):
                print(i, m)
        elif choice == "4":
            print("LOGGED OUT")
            break
        else:
            print("Invalid Choice! Try Again!")
