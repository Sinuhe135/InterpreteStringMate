
def hacerOperacion(operacion):
    indiceCaracter = len(operacion)-1
    while(indiceCaracter>=0):
        if (operacion[indiceCaracter] == "+"):

            if(indiceCaracter==0):
                return hacerOperacion("0") + hacerOperacion(operacion[(indiceCaracter+1):])
            elif(indiceCaracter==len(operacion)-1):
                raise ValueError("Signo positivo sin valor asociado")
            
            return hacerOperacion(operacion[:indiceCaracter]) + hacerOperacion(operacion[(indiceCaracter+1):])
        
        if (operacion[indiceCaracter] == "-"):

            if(indiceCaracter==0):
                return hacerOperacion("0") - hacerOperacion(operacion[(indiceCaracter+1):])
            elif(indiceCaracter==len(operacion)-1):
                raise ValueError("Signo negativo sin valor asociado")
            
            return hacerOperacion(operacion[:indiceCaracter]) - hacerOperacion(operacion[(indiceCaracter+1):])
        
        indiceCaracter-=1
        
    return int(operacion)
            
print(hacerOperacion("-20-3+40"))