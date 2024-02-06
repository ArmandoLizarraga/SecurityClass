from cryptography.fernet import Fernet

#Generar la clave
clave = Fernet.generate_key()

#Instanciar fernet
f = Fernet(clave)
print("Clave: ",clave, '\n')
#Encriptar en menasje, b lo convierte en bits
token = f.encrypt(b'Dame mi equipo omega perra')

#Imprimir el mensaje encriptado
print('Mensaje encriptado:', token)

#Desencriptar
print('Mensaje desencriptado:', f.decrypt(token),  '\n')

#Desencriptar clave de compañero
fernet = Fernet(b'KX4KhSXQnpxzm5ANgqBPC6BkKsMJOUMYlNpCCs8R15Q=')
token1 = fernet.decrypt(b'gAAAAABluwk9vCyi_h2ElkGJdlYRcDgJLwJpbJXuvNawFwvfQcBGOreylrXlraEU6cpJiMUokABd0lvlTjV02z806_krIBMfwQ==')
print('Mensaje que recibi:', token1)
