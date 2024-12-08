from .seat import Seat

class Theatre:
    def __init__(self, location: str, total_rows: int, total_columns: int):
        """
        Initialize the Tneatre object.
        
        :param location: Location string
        :param total_rows: Int
        :param total_columns: Int
        """
        self.location: str = location
        self.total_rows: int = total_rows
        self.total_columns: int = total_columns
        self.total_seats: int = total_rows * total_columns
        self.seats: list[list[object]] = self.generate_seats()
    
    def generate_seats(self):
        ''' Uses a matrix to generate the seating for the theatre '''
        seat_matrix: list = []
        for row in range(self.total_rows):
            row_seats: list = []
            for column in range(self.total_columns):
                seat: object = Seat(row, column)
                row_seats.append(seat)
            seat_matrix.append(row_seats)
        return seat_matrix

    def get_seat_position(self, seat_name):
        row_part: str = ''.join(filter(str.isalpha, seat_name))
        column_part: str = ''.join(filter(str.isdigit, seat_name))

        column: int = int(column_part) - 1
        row: int = 0

        for index, char in enumerate(reversed(row_part)):
            row += (ord(char) - ord('A')) * (26 ** index)
        return row, column

    def __str__(self):
        return f"{self.movies} playing at theatre {self.location}"