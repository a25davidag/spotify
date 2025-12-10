


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.playlists = []

    def create_playlist(self, name):
        from playlist import PlayList

        new_playlist = PlayList(name, self)
        self.playlists.append(new_playlist)
        print(f"Usuario {self.username} creó la playlist: {name}")
        return new_playlist

    def get_playlist_by_name(self, name):
        for playlist in self.playlists:
            if playlist.name == name:
                return playlist
        return None

    def charge_playlists_from_files(self):
        import os
        import main
        from playlist import PlayList

        user_directory = f"./{self.username}/"
        if not os.path.exists(user_directory):
            return

        for filename in os.listdir(user_directory):
            if filename.endswith(".txt"):
                playlist_name = filename[:-4]
                playlist = PlayList(playlist_name, self)

                with open(os.path.join(user_directory, filename), 'r', encoding='utf-8') as f:
                    for line in f:
                        song_name = line.strip()
                        if song_name:
                            for song in main.songs:
                                if song.name == song_name:
                                    playlist.add_song(song)

                self.playlists.append(playlist)


    def __str__(self):
        return (f"Usuario: {self.username}\n"
                f"Número de PlayLists: {len(self.playlists)}")