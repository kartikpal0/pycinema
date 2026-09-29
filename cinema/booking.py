from cinema import movies, pricing, seats, storage
from cinema.validators import get_int
from cinema.log_setup import get_logger

log = get_logger()


def pick_movie():
    movie_list = movies.get_movies()
    if not movie_list:
        print("No movies are available! Ask admin to add movies.")
        return None
    print("\nAvailable Movies:")
    for i, m in enumerate(movie_list, 1):
        print(str(i) + ". " + m)
    choice = get_int("\nChoose a movie: ", 1, len(movie_list))
    return movie_list[choice - 1]


def pick_tickets():
    print("\nTicket Prices:")
    for kind, price in pricing.PRICES.items():
        print(kind, ": Rs.", price)
    while True:
        a = get_int("\nEnter number of Adult tickets: ")
        s = get_int("Enter number of Student tickets: ")
        c = get_int("Enter number of Child tickets: ")
        if a + s + c > 0:
            return a, s, c
        print("You must purchase at least one ticket.")


def pick_seats(movie, count):
    chosen = []
    booked = seats.get_booked(movie)
    for i in range(count):
        while True:
            seat = input("Enter seat number for ticket " + str(i + 1) + ": ").upper().strip()
            if seat not in seats.ALL_SEATS:
                print("Invalid seat number!")
            elif seat in booked:
                print("Seat is already occupied!")
            elif seat in chosen:
                print("You already selected this seat!")
            else:
                chosen.append(seat)
                break
    return chosen


def print_receipt(movie, a, s, c, bill, chosen):
    p = pricing.PRICES
    print("\n========================================")
    print("           BOOKING SUMMARY")
    print("========================================")
    print("Movie:", movie)
    print("Adult   :", a, "x Rs.", p["Adult"], "= Rs.", bill["adult_cost"])
    print("Student :", s, "x Rs.", p["Student"], "= Rs.", bill["student_cost"])
    print("Child   :", c, "x Rs.", p["Child"], "= Rs.", bill["child_cost"])
    print("----------------------------------------")
    print("Seats:", ", ".join(chosen))
    print("Subtotal: Rs.", bill["subtotal"])
    print("Student Discount: Rs.", bill["student_discount"])
    print("Group Discount: Rs.", bill["group_discount"])
    print("FINAL TOTAL: Rs.", bill["final"])
    print("========================================")


def start_booking():
    while True:
        print("\n===== PYCINEMA BOOKING SYSTEM =====")
        movie = pick_movie()
        if movie is None:
            return
        a, s, c = pick_tickets()
        bill = pricing.calculate(a, s, c)
        total = bill["total_tickets"]

        if len(seats.get_available(movie)) < total:
            print("Not enough seats left for", movie, "- try fewer tickets.")
            continue

        seats.show_grid(movie)
        chosen = pick_seats(movie, total)
        if not seats.book(movie, chosen):
            print("Booking failed, a seat was taken. Try again.")
            log.error("Booking conflict for %s %s", movie, chosen)
            continue

        print_receipt(movie, a, s, c, bill, chosen)
        history = storage.load("bookings.json", [])
        history.append({"movie": movie, "seats": chosen, "total": bill["final"]})
        storage.save("bookings.json", history)
        log.info("Booked %s seats %s total %s", movie, chosen, bill["final"])

        print("\n1. Book Another Ticket")
        print("2. Return to Main Menu")
        if input("Enter your choice: ") != "1":
            break
