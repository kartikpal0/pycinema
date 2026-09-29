from cinema import storage

ROWS = "ABCDEFGHIJ"
SEATS_PER_ROW = 10
ALL_SEATS = [r + str(n) for r in ROWS for n in range(1, SEATS_PER_ROW + 1)]


def get_booked(movie):
    return storage.load("seats.json", {}).get(movie, [])


def get_available(movie):
    booked = get_booked(movie)
    return [s for s in ALL_SEATS if s not in booked]


def book(movie, seats):
    data = storage.load("seats.json", {})
    booked = data.get(movie, [])
    for s in seats:
        if s not in ALL_SEATS or s in booked:
            return False
    data[movie] = booked + list(seats)
    storage.save("seats.json", data)
    return True


def show_grid(movie):
    booked = get_booked(movie)
    print("\n========== SEAT MAP ==========")
    for i in range(0, len(ALL_SEATS), SEATS_PER_ROW):
        for seat in ALL_SEATS[i:i + SEATS_PER_ROW]:
            print("[X]" if seat in booked else "[" + seat + "]", end=" ")
        print()
    print("[X] = BOOKED")
