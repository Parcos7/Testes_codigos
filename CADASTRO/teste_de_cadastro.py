cadastro = [{"Nome": "Marcos", "Usuario": "mparcos7", "Senha": "M@9rcos_15"}, {"Nome": "ROSA", "Usuario": "mparcos7", "Senha": "M@9rcos_15"}]


dadosC = open('Dados.txt', 'w')
dadosC.write(' ' * 20 + 'Dados incluso dos Usuarios\n\n')
for dado in cadastro:
    Vdados = list(dado.values())
    Kdados = list(dado.keys())
    for i in range (len(dado)):
        dadosC.write('%s: %s\n\n' % (Kdados[i], Vdados[i]))