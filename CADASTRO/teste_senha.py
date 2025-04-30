senha = "Rob123erto6$"

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

    print(validarSequencia(validarDigit))
    return validar == 2 and validarSequencia(validarDigit) == False 

print("Senha valida!" if validando(senha)else "Senha Invalida!")
               