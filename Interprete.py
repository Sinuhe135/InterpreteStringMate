
def hacerOperacion(operacion):
    corchetesAbiertos = 0 #Poner soporte de corchetes. Si se habre un corchete deja de detectar parentesis y vicecersa
    parentesisAbiertos = 0
    
    indiceCaracter = len(operacion)-1
    while(indiceCaracter>=0):

        if (operacion[indiceCaracter] == "("): 
            parentesisAbiertos+=1

        elif (operacion[indiceCaracter] == ")"):
            parentesisAbiertos-=1

        if(parentesisAbiertos!=0):
            indiceCaracter-=1
            continue

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

    #Checar parentesis sin par
    if(parentesisAbiertos!=0):
        raise ValueError("Parentesis sin par")
    
    #Eliminar parentesis
    if(operacion[:1]=="(" and operacion[len(operacion)-1:]==")"):
        return hacerOperacion(operacion[1:-1])
    
    # try:
    return int(operacion)
    # except:
    #     raise ValueError("Error de sintaxis")
            
print(hacerOperacion("((5-7)-[10+4)]"))