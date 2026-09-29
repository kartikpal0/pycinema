from cinema import auth, movies, booking


def main():
    auth.first_time_setup()
    while True:
        print("\n=====================")
        print("      Main Menu      ")
        print("=====================")
        print("1. Manage Movies (admin)")
        print("2. Book Tickets")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            movies.manage_movies()
        elif choice == "2":
            booking.start_booking()
        elif choice == "3":
            print("Thank you!")
            break
        else:
            print("Invalid Choice! Try Again!")


if __name__ == "__main__":
    main()
