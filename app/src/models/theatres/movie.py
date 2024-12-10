class Movie:
    def __init__(self, title: str, duration: int):
        self.title: str    = title
        self.duration: int = duration # this is the duration in minutes

    def __str__(self):
        return f"{self.title} - (Length: {self.duration} min)"