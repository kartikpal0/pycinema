
# PyCinema - Movie Ticket Booking System

## Overview
PyCinema is a command-line movie ticket booking system written in Python.
An admin manages the list of movies, and customers pick a movie, choose
ticket types, select seats on a seat map, and get a bill with discounts applied.

## Features
- Admin account created on first run, password stored as a salted hash
- Add, remove and view movies (saved between runs)
- Separate seat map (10 x 10) for every movie
- Adult, Student and Child tickets
- 10% student discount (2+ student tickets) and 5% group discount (5+ tickets)
- Input validation on every prompt
- Bookings and events logged to `logs/pycinema.log`

## Technologies
- Python 3.8 or newer (standard library only, no pip install needed)
- JSON for storage, `unittest` for testing, Git for version control

## Project Structure
```
main.py            entry point
cinema/            auth, movies, pricing, seats, booking, storage, validators, log_setup
tests/             unit tests
data/              JSON data (created automatically)
logs/              log file (created automatically)
```

## How to Install and Run
```
python --version
git clone https://github.com/kartikpal0/pycinema.git
cd pycinema
python main.py
```
On the first run you will be asked to create the admin ID and password.
Choose 1 in the main menu to manage movies, or 2 to book tickets.

## How to Test
```
python -m unittest discover tests
```

## Screenshots
                          MAIN MENU 

<img width="907" height="512" alt="Screenshot 2026-09-30 111751" src="https://github.com/user-attachments/assets/52ca4aba-ed42-4c84-88bc-9a0b4b9ba58d" />



                      SEAT MAP AND TICKET PRICES
<img width="1021" height="662" alt="Screenshot 2026-09-30 111829" src="https://github.com/user-attachments/assets/5c61b271-7b7c-43a2-9d46-fea96b345b48" />

          
                     ADMIN INTERFACE
<img width="971" height="499" alt="Screenshot 2026-09-30 111926" src="https://github.com/user-attachments/assets/243d1a60-298c-4b85-8c3b-e5711574210d" />



