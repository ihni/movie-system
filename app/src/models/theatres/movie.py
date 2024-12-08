class Movie:
    def __init__(self, title: str, genre: str, duration: int):
        self.title: str    = title
        self.genre: str    = genre
        self.duration: int = duration # this is the duration in minutes

    def __str__(self):
        return f"{self.title} - (Length: {self.duration} min)"