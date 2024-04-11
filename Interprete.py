
def hacerOperacion(operacion):
    if(operacion==""):
        return 0
        
    indiceCaracter = len(operacion)-1
    while(indiceCaracter>=0):
        if (operacion[indiceCaracter] == "+"):
            return hacerOperacion(operacion[:indiceCaracter]) + hacerOperacion(operacion[(indiceCaracter+1):])
        if (operacion[indiceCaracter] == "-"):
            return hacerOperacion(operacion[:indiceCaracter]) - hacerOperacion(operacion[(indiceCaracter+1):])
        indiceCaracter-=1
    return int(operacion)
            
print(hacerOperacion("-20-3+40"))