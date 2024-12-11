import os
os.system("")

COLOR = {
    "HEADER" : "\033[95m",
    "RED" : "\033[91m",
    "ORANGE" : "\033[38;5;214m",
    "INDIGO" : "\033[38;5;54m",
    "GREEN" : "\033[92m",
    "YELLOW" : "\033[1;33m",
    "BLACK" : "\033[0;30m",
    "BROWN" : "\033[0;33m",
    "BLUE" : "\033[0;34m",
    "PURPLE" : "\033[0;35m",
    "CYAN" : "\033[0;36m",
    "LIGHT_GRAY" : "\033[0;37m",
    "DARK_GRAY" : "\033[1;30m",
    "LIGHT_RED" : "\033[1;31m",
    "LIGHT_GREEN" : "\033[1;32m",
    "LIGHT_BLUE" : "\033[1;34m",
    "LIGHT_PURPLE" : "\033[1;35m",
    "LIGHT_CYAN" : "\033[1;36m",
    "LIGHT_WHITE" : "\033[1;37m",
    "MAGENTA" : "\033[35m",
    "ENDC" : "\33[0m"
}
#BOLD = "\033[1m"
#FAINT = "\033[2m"
#ITALIC = "\033[3m"
#UNDERLINE = "\033[4m"
#BLINK = "\033[5m"
#NEGATIVE = "\033[7m"
#CROSSED = "\033[9m"

class Utilities:
    def display_seats_for_showtime(self, showtime: object):
        seat_matrix = showtime.get_seat_matrix()

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
        seat_matrix = showtime.get_seat_matrix()

        for row in seat_matrix:
            for seat in row:
                display = None
                if seat.is_available:
                    display = 0
                else:
                    display = 1
                print(display, end = " ")
            print()

    def rainbow_text(self, text):
        smooth_rainbow = [
            "\033[38;5;196m",  # Red
            "\033[38;5;202m",  # Orange
            "\033[38;5;214m",  # Light Orange
            "\033[38;5;226m",  # Yellow
            "\033[38;5;34m",   # Green
            "\033[38;5;50m",   # Light Green
            "\033[38;5;32m",   # Dark Green
            "\033[38;5;33m",   # Blueish Green
            "\033[38;5;37m",   # Light Blue
            "\033[38;5;61m",   # Blue
            "\033[38;5;63m",   # Deep Blue
            "\033[38;5;93m",   # Indigo
            "\033[38;5;129m",  # Violet
            "\033[38;5;162m",  # Purple
            "\033[38;5;197m",  # Magenta
            "\033[38;5;218m",  # Pink
            "\033[38;5;250m"   # Light Pink
        ]
        colored_text = ""
        color_index = 0

        for char in text:
            if char != " " and char != "\n":
                colored_text += smooth_rainbow[color_index] + char
                color_index = (color_index + 1) % len(smooth_rainbow)
            else:
                colored_text += char  # Preserve spaces and newlines without coloring

        colored_text += "\033[0m"  # Reset color at the end
        return colored_text
    
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')