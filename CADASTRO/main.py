import psycopg2

conn = psycopg2.connect(
    host = 'localhost',
    port ='5432',
    user = 'postgres',
    password = '123',
    database = 'postgres'
)

cursor = conn.cursor()
cursor.execute("CREATE TABLE Usuarios(id SERIAL PRIMARY KEY, nome VARCHAR(100), senha VARCHAR(10), usuario VARCHAR(100));")
cursor.execute("INSERT INTO Usuarios(nome, senha, usuario) VALUES ('Admin', 'Admin@243', 'Admin');")
def cadastrar( x):
    def validando(senha):
        def validarSequencia(validarDigit):
            inicio = validarDigit[0]
            fim = validarDigit[-1]
            if isinstance(fim, str):
                validarDigit.remove(fim)
                fim = validarDigit[-1]
            if inicio > fim:
                return sorted(list(validarDigit)) == list(range(fim, inicio + 1))
            return list(validarDigit) == list(range(inicio, fim + 1))              
        validar = 0
        validarDigit = []
        for char in senha:
            if validar == 2:
                pass
            elif char == char.upper() and validar == 0 or char in "@,.><?;:|*&¨%$#@!_-=+":
                validar += 1
            if char.isdigit():
                a = int(char)
                validarDigit.append(a)
            else:
                validarDigit.append(char)
        for i in range(len(validarDigit)):
            for j in range(i +1, len(validarDigit)):   
                if isinstance(validarDigit[i], str):
                    validarDigit.remove(validarDigit[i])
                elif isinstance(validarDigit[i + 1], str) and isinstance(validarDigit[i - 1], str):
                    validarDigit.remove(validarDigit[i])
        return validar == 2 and validarSequencia(validarDigit) == False 
            
    def validarUser(nome, id, senha):
        cursor.execute("SELECT usuario FROM Usuarios WHERE usuario = '%s';" % (id))
        resultado = cursor.fetchall()
        if resultado:
            return print('Usuario já existente')
        else:
            return cursor.execute("INSERT INTO Usuarios(nome, usuario, senha) VALUES('%s', '%s', '%s');" % (nome, id, senha))
    #até aqui eu mechi 
    match x:    
        case 'login':
            login = input("Digite o usuario ou Email: ")
            senha = input("Digite a senha: ")
            cursor.execute("SELECT usuario, senha, email FROM Usuarios WHERE usuario = '%s' OR email = '%s' AND senha = '%s'" % (login, login, senha))
            resultado = cursor.fetchall()
            if resultado:
                print("Seja bem-vindo!!!")
            else:
                print("Senha ou usuario invalida!!")

        case 'Attsenha':
            login = input("Digite o usuario ou Email: ")
            senha = input("Digite a senha: ")
            cursor.execute("SELECT usuario, senha, email FROM Usuarios WHERE usuario = '%s' OR email = '%s' AND senha = '%s'" % (login, login, senha))
            resultado = cursor.fetchall()
            if resultado:
                Newsenha = input("Digite a nova senha: ")
                if validando(Newsenha):             
                    cursor.execute("UPDATE Usuarios SET senha = '%s' WHERE usuario = '%s' OR email = '%s'" % (Newsenha, login, login))
                    print("Nova senha cadastrada!!\n\n")
                else:
                    print("Senha invalida! precisa de 1 letra maiuscula, caractere especial, não pode conter numeros sequencias")    
        case 'Cadastro':
            entNome = input("Insira o Nome: ")
            nome = entNome[:1].upper()
            nome += entNome[1:]
            id = input("insira seu Usuario: ")
            senha = input("Insira sua senha: ")
            email = input("Insira o email: ")
            if validando(senha):
                validarUser(nome, id, senha, email)
                print("CADASTRO REALIZADO COM SUCESSO!!\n\n")
            else:
                print("Senha invalida! precisa de 1 letra maiuscula, caractere especial, não pode conter numeros sequencias")
            
try:
    while True:
        escolha = int(input("Escolha a opção:\n1 - Cadastrar || 2- login || 3 - Alterar senha ||4 - Verificar Dados||5 - Baixar Dados: "))  
        match escolha:
            case 1:
                x = 'Cadastro'
                cadastrar(x)
            case 2:
                x = 'login'
                cadastrar(x)
            case 3:
                x = 'Attsenha'
                cadastrar(x)
            case 4:
                cursor.execute('SELECT * FROM Usuarios')
                for row in cursor.fetchall():
                    print(row)
            case 5:
                dadosC = open('Dados.txt', 'w')
                dadosC.write(' ' * 20 + 'Dados incluso dos Usuarios\n\n')
                cursor.execute("SELECT * FROM Usuarios")
                resultados = cursor.fetchall()
                for pessoa in resultados:
                    dadosC.write('Dados da %s° pessoa:\n\n' % (pessoa[0]))
                    dadosC.write('Nome: %s\n\nUsuario: %s\n\nSenha: %s\n\nE-mail: %s\n\n' % (pessoa[1], pessoa[2], pessoa[3], pessoa[4]))
                print("Arquivo TXT salvo com sucesso! ")
except:
    print("ERRO!")
