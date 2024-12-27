import os
import pyaes

# Função para descriptografar um arquivo
def descriptografar_arquivo(file_name, key):
    try:
        # Abrir o arquivo criptografado
        with open(file_name, "rb") as file:
            file_data = file.read()

        # Criar objeto AES para descriptografia
        aes = pyaes.AESModeOfOperationCTR(key)
        decrypt_data = aes.decrypt(file_data)

        # Remover o arquivo criptografado
        os.remove(file_name)

        # Criar o arquivo descriptografado
        original_file_name = file_name.replace(".ransomwaretroll", "")
        with open(original_file_name, "wb") as new_file:
            new_file.write(decrypt_data)

        print(f"Arquivo descriptografado: {file_name} -> {original_file_name}")
    except Exception as e:
        print(f"Erro ao descriptografar {file_name}: {e}")

# Função para percorrer diretórios e descriptografar arquivos
def descriptografar_pasta(pasta, key):
    for raiz, _, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            if arquivo.endswith(".ransomwaretroll"):
                caminho_arquivo = os.path.join(raiz, arquivo)
                descriptografar_arquivo(caminho_arquivo, key)

if __name__ == "__main__":
    # Caminho da pasta alvo
    pasta_alvo = input("Digite o caminho da pasta para descriptografar os arquivos: ")

    if os.path.exists(pasta_alvo) and os.path.isdir(pasta_alvo):
        # Chave de descriptografia (deve ser a mesma usada para criptografia)
        key = b"testeransomwares"  # Certifique-se de usar a chave correta
        descriptografar_pasta(pasta_alvo, key)
    else:
        print("Pasta inválida. Verifique o caminho e tente novamente.")
