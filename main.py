import pygame
import sys

from genre import Genre
from playlist import PlayList
from song import Song

global current_user
MEDIA_DIR = "./media/"

songs = [Song("circles", "3:35", "2019-08-30", Genre.POP),
         Song("birds_of_a_feather", "4:14", "2021-11-19", Genre.POP),
         Song("99999999-Acid Blood", "3:31", "2020-16-12",Genre.TECHNO),
         Song("Aitana-Los Angeles", "2:38","2024-01-4",Genre.POP),
         Song("Anuel-feat Badbunny-La ultima vez", "5:00", "2023-04-9", Genre.TRAP),
         Song("Beny jr-2019", "2:33", "2012-05-4", Genre.DRILL),
         Song("Beny jr-Mbappe,Bellingham,Vinicius Jr", "2:54", "2015-02-23", Genre.DRILL),
         Song("Carl Cox-Finder", "3:26", "2010-03-12", Genre.TECHNO),
         Song("Cascada-Everytime we touch","3:17","2014-12-4",Genre.POP),
         Song("Chris stussy-Go","3:16","2000-05-12",Genre.TECHNO),
         Song("Cupido-La pared","4:50","2012-01.23",Genre.RAP),
         Song("Eminem feat.Rihanna-Love the way you lie","4:26","2000-01-24",Genre.POP),
         Song("Gym clase - stereo hearts ","3:36","2002-05-12",Genre.POP),
         Song("Jambo-Indira Paganotto ","6:11","2007-02-14",Genre.TECHNO),
         Song("Jokki feat.Cupido-Estoy de bajon","2:49","2008-06-30",Genre.POP),
         Song("Julieta Venega-A donde va el Viento","2:43","2012-09-12",Genre.POP),
         Song("Julieta Venega-Limon y sal","3:25","2005-11-27",Genre.POP),
         Song("Lyaz-Replay","3:02","2014-11-06",Genre.POP),
         Song("Nico moreno feat.Samuel-See me coming","4:16","2023-04-20",Genre.TECHNO),
         Song("Nico Moreno-My black rave","6:52","2021-09.23",Genre.TECHNO),
         Song("Nico moreno-You make me horny","4:54","2019-12-20",Genre.TECHNO),
         Song("Obsku feat.Tomike.Ive arrived","2:31","2007-03-11",Genre.TECHNO),
         Song("onlynumbers festejó.Slayer Diesel-Resson to die ","4:25","1999-02-17",Genre.TECHNO),
         Song("Pawsa feat.Nate Doggs-Pick up the phone","3:44","2023-11-12",Genre.TECHNO),
         Song("Pimp Flaco-Te gusta conducir","3:20","2018-08-12",Genre.RAP),
         Song("Radio macade-dime dónde está el camino","4:18","2009,02-12",Genre.POP),
         Song("Rihanna - Don't Stop The Music","4:26","2012-08-23",Genre.POP),
         Song("Rihanna-SyM","4:03","2003-01-23",Genre.POP),
         Song("Rihanna-Umbrella","4:36","2006-12-25",Genre.POP),
         Song("Robbie Williams-Feel","4:22","2019-04-30",Genre.POP),
         Song("Sean Paul-Got 2 luv U","3:26","2012-05-23",Genre.TECHNO),
         Song("Whitney Houston-Its not right but its ok","2:32","2005-02-14",Genre.TECHNO)
         ]


def reproduce_song(song):
    # Inicializar el mixer
    pygame.mixer.init()

    # Cargar canción
    pygame.mixer.music.load(MEDIA_DIR + song + ".mp3")

    # Reproducir
    pygame.mixer.music.play()

    print(f"Reproduciendo {song}... ")
    while True:
        comando = input("Pulsa (pausa, reanudar, stop, salir): ").strip().lower()

        if comando == "pausa":
            pygame.mixer.music.pause()
        elif comando == "reanudar":
            pygame.mixer.music.unpause()
        elif comando == "stop":
            pygame.mixer.music.stop()
        elif comando == "salir":
            pygame.mixer.music.stop()
            break
        else:
            print("Comando no válido")

def reproduce_playList(name):
    pygame.mixer.init()

    current_playlist_songs = []
    for playlist in current_user.playlists:
        if playlist.name == name:
            current_playlist_songs = playlist.songs

    if not current_playlist_songs:
        print("La playlist no existe o está vacía.")
        return

    index = 0
    print("################################################")
    print("Songs in the playlist:")
    for song in current_playlist_songs:
        print(f"- {song.name:<35} - {song.duration}")
    print("################################################")

    def play_song(i):
        pygame.mixer.music.load(MEDIA_DIR + current_playlist_songs[i].name + ".mp3")
        pygame.mixer.music.play()
        print(f"Reproduciendo {current_playlist_songs[i].name}...")

    play_song(index)

    while True:
        comando = input("Pulsa (siguiente, pausa, reanudar, stop, salir): ").strip().lower()

        if comando == "siguiente":
            index = (index + 1) % len(current_playlist_songs)  # ciclo por la playlist
            play_song(index)
        elif comando == "pausa":
            pygame.mixer.music.pause()
        elif comando == "reanudar":
            pygame.mixer.music.unpause()
        elif comando == "stop":
            pygame.mixer.music.stop()
        elif comando == "salir":
            pygame.mixer.music.stop()
            break
        else:
            print("Comando no válido")


def login():
    from login import Login
    print_logo()
    global current_user
    login = Login()
    login.load_users()

    while True:
        print("\t\t\t\t1. Login\t\t\t\t2. Create User")
        print("\t\t\t\t\t\t     0. Salir")
        print("\n**********************************************************************")

        choice = input("Elige una opción: ")

        if choice == '1':
            if login.is_login_correct():
                current_user = login.get_current_user()
                return True
        elif choice == '2':
            login.create_new_user()
        elif choice == '3':
            print("Saliendo de la aplicación.")
            return False
        else:
            print("Opción no válida. Inténtalo de nuevo.")


def menu():
    while True:
        print_logo()

        print("\t1. Reproducir PlayList\t\t\t2. Reproducir Canción")
        print("\t3. Crear Playlist\t\t\t\t4. Tu Wrapped")
        print("\t\t\t 5. Todas Las Canciones De Spoty")
        print("\t\t\t\t\t\t  0. Salir")
        print("\n**********************************************************************")

        try:
            choice = int(input("Elige una opción: "))

            if choice == 1:
                for playlist in current_user.playlists:
                    print(f"- {playlist.name}")
                reproduce_playList(input("Ingresa el nombre de la playList: "))

            elif choice == 2:
                for song in songs:
                    print(f"- {song.name}")
                reproduce_song(input("Ingresa el nombre de la canción: "))

            elif choice == 3:
                playlist_name = input("Ingresa el nombre de la nueva playlist: ")
                new_playlist = current_user.create_playlist(playlist_name)
                while True:
                    for song in songs:
                        print(f"- {song.name}")
                    song_name = input("Ingresa el nombre de la canción a agregar (o 'salir' para terminar): ")
                    if song_name.lower() == 'salir':
                        break
                    song_found = False
                    for song in songs:
                        if song.name == song_name:
                            new_playlist.add_song(song)
                            song_found = True
                            break
                    if not song_found:
                        raise NameError("La canción no existe en la base de datos.")
                new_playlist.save_to_file()

            elif choice == 4:
                print("TODO: Wrapped")
                # Tu Wrapped
                # Aquí puedes implementar la funcionalidad de Wrapped
                # Debe de aparecer: Tu usuario,
                # cuantas playlist tienes,
                # tu canción mas usada en distintas plalylist,
                # tu género más escuchado,
                # Artista favorito
            elif choice == 5:
                print("Te mostrare todas canciones de spotify ")
                for song in songs:
                    print(f"- {song.name}")
                print("Estas son las canciones ")
            elif choice == 0:
                print("Adiós!")
                sys.exit(0)
            else:
                print("[ERROR] Tu opción es incorrecta. ¡Intenta de nuevo!")
        except ValueError:
            print("[ERROR] Debes escribir un número válido!")
        except Exception as e:
            print(f"[ERROR] {e}")

def print_logo():
    print("**********************************************************************")
    print("*                                                                    *")
    print("*                             SPOTIFY                                *")
    print("*                                                                    *")
    print("**********************************************************************\n")

if __name__ == "__main__":
    while not login():
        pass
    menu()