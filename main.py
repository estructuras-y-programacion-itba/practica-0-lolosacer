import random
def inicial():
    dados=[]
    for i in range(5):
        dados.append(random.randint(1,6))
    return dados

def tirada(dados):
    respuesta=input("Ingrese 0 si no quiere cambiar el dado, 1 si lo quiere cambiar. Ej; 01001:")
    for i in range(5):
        if respuesta[i] == '1':
            dados[i]=random.randint(1,6)
    return dados
    
def numero_elegido(dados, numero):
    suma = 0
    for dado in dados:
        if dado == numero:
            suma += numero
    return suma

def jugadas(dados):
    repeticiones=[]
    trio=False
    par=False
    
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
    if sorted(dados) == [1,2,3,4,5] or sorted(dados) == [2,3,4,5,6]:
            return "Escalera"
    if trio and par:
        return "Full"
    return "Nada"
    
def puntaje(jugada_detectada, nro_tiro, categoria_elegida,dados):    
    if categoria_elegida.isdigit() and nro_tiro==3:
        return numero_elegido(dados, int(categoria_elegida))
    if jugada_detectada == "Generala":
        return 80 if nro_tiro == 1 else 50
    if jugada_detectada == "Poker":
        return 45 if nro_tiro == 1 else 40
    if jugada_detectada == "Full":
        return 35 if nro_tiro == 1 else 30
    if jugada_detectada == "Escalera":
        return 25 if nro_tiro == 1 else 20
    return 0
    
def turno(nombre):
    print (f"Turno del jugador:{nombre}")
    dados=inicial()
    print(dados)
    nro_tiro=1
    while nro_tiro<=3:
        puntos=puntaje(jugadas(dados),nro_tiro,)

    



