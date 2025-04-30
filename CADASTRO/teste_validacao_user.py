cadastro = [{'Usuario': 'mparcos7'}]

def validandoUsuario(cadastro, user):
    for pessoas in cadastro:
        if pessoas['Usuario'] == user:
            print("Usuario ja existe!")
            return False


login = input("Insira o usuario: ")

print(validandoUsuario(cadastro, login))
print(cadastro)