import os

from song import Song
from user import User


class PlayList:

    def __init__(self, name, user: User):
        self.name = name
        self.user = user
        self.songs = []

    def add_song(self, song : Song):
        self.songs.append(song)

    def save_to_file(self):
        filename = f"./{self.user.username}/{self.name}.txt"
        directory = os.path.dirname(filename)
        if directory:
            os.makedirs(directory, exist_ok=True)

        with open(filename, 'w', encoding='utf-8') as f:
            for song in self.songs:
                f.write(f"{song.name}\n")

        print(f"\nPlaylist guardada exitosamente en el archivo: '{filename}'")

    def __str__(self):
        return f"PlayList: {self.name} ({len(self.songs)} canciones)"