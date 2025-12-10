from genre import Genre


class Song:

    def __init__(self, name, duration, release_date, genre: Genre):
        self.name = name
        self.duration = duration
        self.releaseDate = release_date
        self.genre = genre



    def __str__(self):
        return f"Song: {self.name})"