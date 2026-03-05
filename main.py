import random
def tirada(cant_dados):
    resultado=[]
    for i in range(cant_dados)
        resultado.append(random.randint(1,6))            
    return resultado
    
def numero_elegido(dados, numero):
    suma = 0
    for dado in dados:
        if dado == numero:
            suma += numero
    return suma

def jugadas(dados):
    repeticiones=[]
    for i in range(1,7):
        repeticiones=dados.count(i)
        if repeticiones==5:
            return "Generala"
        elif repeticiones==4:
            return "Poker"
        elif repeticiones==3:
            trio=True
        elif repeticiones==2:
            par=True
    if dados = [1,2,3,4,5] or dados == [2,3,4,5,6]:
            return "Escalera"
    if trio and par:
        return "Full"
    return "Nada"
    
def puntaje(jugada):
    if jugada == "Generala":
        return 50
    elif jugada == "Poker":
        return 40
    elif jugada == "Full":
        return 30
    elif jugada == "Escalera":
        return 20
    else:
        return 0

