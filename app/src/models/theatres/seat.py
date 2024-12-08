class Seat:
    def __init__(self, row: int, column: int):
        self.row:           int = row
        self.column:        int = column
        self.is_available: bool = True
        self.name:          str = self.generate_name()

    def generate_name(self) -> str:
        ''' Returns a string of the seats name depending on its row and column '''
        row_letter: str =  ""
        row_index:  int = self.row

        while row_index >= 0:
            row_letter = chr(row_index % 26 + ord('A')) + row_letter
            row_index  = row_index // 26 - 1  # Move to the next "digit"

        column_number: int = self.column + 1  # Convert column index to 1-based
        return f"{row_letter}{column_number}"
    
    def reserve(self) -> bool:
        self.is_available: bool = False

    def release(self) -> bool:
        self.is_available: bool = True

    def __str__(self):
        return f"{self.name} - ({self.is_available})"