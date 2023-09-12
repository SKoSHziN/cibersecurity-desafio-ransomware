import os
from cryptography.fernet import Fernet

# Pegar nome do usuario para a chave
def get_username():
    if os.name == 'posix':  # Verifica se é um sistema Unix-like (Linux, mac>
        return os.getenv('USER')
    elif os.name == 'nt':  # Verifica se é o Windows
        return os.getenv('USERNAME')
    else:
        return "noname"

# Carrega a chave do usuario
def load_key_for_user():
    username = get_username()  # Obtém o nome de usuário do sistema
    key_file = f"{username}.key"  # Nome da chave com base no usuário

    if os.path.isfile(key_file):
        with open(key_file, 'rb') as file:
            key = file.read()
        return key
    else:
        return None  # Chave do usuario não encontrada

if __name__ == "__main__":
    key = load_key_for_user()

    if key:
        print("Chave carregada com sucesso!")
    else:
        print("Arquivo de chave nao encontrada para recuperacao dos dados.")

# Descriptografar um arquivo com a chave
def decrypt_file(key, filename):
    fernet = Fernet(key)
    with open(filename, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(filename, 'wb') as file:
        file.write(decrypted_data)

# Pasta onde os arquivos estão criptografados
pasta_alvo = './teste'

# Percorrer todos os arquivos na pasta e subpastas e descriptografá-los
for root, _, files in os.walk(pasta_alvo):
    for file in files:
        file_path = os.path.join(root, file)
        decrypt_file(key, file_path)

print('Todos os arquivos foram descriptografados')
