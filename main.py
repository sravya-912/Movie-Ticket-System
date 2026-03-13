class Movie:
    def __init__(self, title, genre, duration, ticket_price):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.ticket_price = ticket_price

    def display_movie_info(self):
        print("Title:", self.title)
        print("Genre:", self.genre)
        print("Duration:", self.duration)
        print("Ticket Price:", self.ticket_price)

movie1 = Movie("Harry Potter", "fiction", 148, 12)
movie2 = Movie("The Lion King", "animation", 88, 10)
movie3 = Movie("Avengers", "action", 181, 15)

movie1.display_movie_info()
movie2.display_movie_info()
movie3.display_movie_info()

class Theater:
    def __init__(self, name, total_seats):
        self.name = name
        self.total_seats = total_seats
        self.seats = []

        # Create seats from 1 to total_seats
        for i in range(1, total_seats + 1):
            self.seats.append(i)

    def show_available_seats(self):
        print("Available seats:", self.seats)

    def book_seat(self, seat_number):
        if seat_number in self.seats:
            self.seats.pop(seat_number)
            print("Seat", seat_number, "booked successfully.")
        else:
            print("Seat not available.")

    def cancel_seat(self, seat_number):
        if seat_number not in self.seats and seat_number <= self.total_seats:
            self.seats.append(seat_number)
            print("Seat", seat_number, "canceled successfully.")
        else:
            print("Cancel failed")
            
theater = Theater("City Theater", 50)

theater.show_available_seats()
theater.book_seat(5)
theater.book_seat(5)
theater.cancel_seat(5)
theater.show_available_seats()