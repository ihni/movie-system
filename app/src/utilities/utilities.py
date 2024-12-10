import os
os.system("")

COLOR = {
    "HEADER" : "\033[95m",
    "RED" : "\033[91m",
    "GREEN" : "\033[92m",
    "YELLOW" : "\033[1;33m",
    "ENDC" : "\33[0m"
}

class Utilities:
    def display_seats_for_showtime(self, showtime: object):
        seat_matrix = showtime.get_seating_matrix()

        for row in seat_matrix:
            for seat in row:
                display = f"{seat.name}"
                if seat.is_available:
                    display += f"{COLOR["GREEN"]}x0{COLOR["ENDC"]}"
                else:
                    display += f"{COLOR["RED"]}x1{COLOR["ENDC"]}"
                print(display, end=" ")
            print()

    def display_seats_binary(self, showtime: object):
        seat_matrix = showtime.get_seating_matrix()

        for row in seat_matrix:
            for seat in row:
                display = None
                if seat.is_available:
                    display = 0
                else:
                    display = 1
                print(display, end = " ")
            print()