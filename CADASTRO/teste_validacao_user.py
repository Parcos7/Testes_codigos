#CODIGO SÓ EM PYTHON
#cadastro = [{'Usuario': 'mparcos7'}]
#def validandoUsuario(cadastro, user):
#    for pessoas in cadastro:
#        if pessoas['Usuario'] == user:
#            print("Usuario ja existe!")
#            return False


#login = input("Insira o usuario: ")

#print(validandoUsuario(cadastro, login))
#print(cadastro)

# CODIGO CONVERSANDO COM POSTGRESQL
#def validarUser(nome, id, senha):
#    cursor.execute("SELECT usuario FROM Usuarios WHERE usuario = '%s';" % (id))
#    resultado = cursor.fetchall()
#    if resultado:
#        return print('Usuario já existente')
#    else:
#       return cursor.execute("INSERT INTO Usuarios(nome, usuario, senha) VALUES('%s', '%s', '%s');" % (nome, id, senha))
