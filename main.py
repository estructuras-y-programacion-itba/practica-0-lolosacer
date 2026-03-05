import random
def tirada(cant_dados):
    resultado=[]
    for i in range(cant_dados):
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
    
def puntaje(jugada_detectada, nro_tiro, categoria_elegida, dados):    
    # 1. Si elige un número (1 al 6)
    if categoria_elegida.isdigit() and nro_tiro==3:
        return numero_elegido(dados, int(categoria_elegida))
    
    # 2. Si elige una jugada especial
    if categoria_elegida == "G" and jugada_detectada == "Generala":
        return 80 if nro_tiro == 1 else 50
    
    if categoria_elegida == "P" and jugada_detectada == "Poker":
        return 45 if nro_tiro == 1 else 40
    
    if categoria_elegida == "F" and jugada_detectada == "Full":
        return 35 if nro_tiro == 1 else 30
    
    if categoria_elegida == "E" and jugada_detectada == "Escalera":
        return 25 if nro_tiro == 1 else 20
        
    # 3. Jugada Obligatoria: Si elige algo que no tiene o no es nada
    return 0
    



