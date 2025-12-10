import hashlib

from user import User

USERS_FILE_PATH = "./login/users.txt"
import os
users = []
current_user = None

class Login:

    def __init__(self):
        pass

    def hash_password(self, password: str) -> str:
        """Hashea la contraseña usando SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()

    def create_login_directory(self):
        """Crea el directorio './login' si no existe."""
        directory = os.path.dirname(USERS_FILE_PATH)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)


    def load_users(self):
        """Carga los usuarios desde el fichero y puebla la lista global 'users'."""
        global users
        self.create_login_directory()

        try:
            with open(USERS_FILE_PATH, 'r', encoding='utf-8') as f:
                for line in f:
                    parts = line.strip().split(',')
                    if len(parts) == 2:
                        username, hashed_password = parts
                        users.append(User(username, hashed_password))

        except FileNotFoundError:
            print("")

    def create_new_user(self):
        """Permite crear un nuevo usuario y guarda su hash en el fichero."""
        print("\n--- CREAR NUEVO USUARIO ---")

        username = input("Elige nombre de usuario: ")

        # Comprobar si ya existe
        for user in users:
            if user.username == username:
                print(f"Error: El usuario '{username}' ya existe. Intenta iniciar sesión.")
                return

        password = input("Elige contraseña: ")
        hashed_pwd = self.hash_password(password)

        # 1. Guardar en el archivo (añadir modo 'a' para append)
        self.create_login_directory()
        try:
            with open(USERS_FILE_PATH, 'a', encoding='utf-8') as f:
                f.write(f"{username},{hashed_pwd}\n")

            # 2. Recargar la lista global 'users'
            self.load_users()

            print(f"\n¡Usuario '{username}' creado y registrado exitosamente!")
        except Exception as e:
            print(f"Error al guardar el usuario: {e}")

    def is_login_correct(self):
        """Función para autenticar un usuario existente."""
        global current_user

        # Aseguramos que la lista 'users' esté poblada antes de buscar
        if not users:
            print("No hay usuarios registrados para iniciar sesión.")
            return False

        username = input("Ingresa tu nombre de usuario: ")
        password = input("Ingresa tu contraseña: ")

        # Hasheamos la contraseña ingresada para compararla con el hash guardado
        input_hashed_pwd = self.hash_password(password)

        for user in users:
            # Comparamos el nombre y el HASH de la contraseña
            if user.username == username and user.password == input_hashed_pwd:
                print(f"\n¡Bienvenido de nuevo, {username}!")
                current_user = user
                current_user.charge_playlists_from_files()
                return True

        # Si el bucle termina sin un match:
        print("\nUsuario o contraseña incorrectos.")
        return False

    def get_current_user(self):
        global current_user
        return current_user