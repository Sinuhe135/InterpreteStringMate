def hacerOperacion(operacion):
    corchetesAbiertos = 0
    parentesisAbiertos = 0

    #Suma resta
    indiceCaracter = len(operacion)-1
    while(indiceCaracter>=0):

        if(parentesisAbiertos ==0):
            corchetesAbiertos+=revisarCorchetes(operacion[indiceCaracter]) 

        if(corchetesAbiertos ==0):
            parentesisAbiertos+=revisarParentesis(operacion[indiceCaracter])

        if(parentesisAbiertos!=0 or corchetesAbiertos!=0):
            indiceCaracter-=1
            continue

        if (operacion[indiceCaracter] == "+"):

            if(indiceCaracter==0):
                return hacerOperacion("0") + hacerOperacion(operacion[(indiceCaracter+1):])
            elif(indiceCaracter==len(operacion)-1):
                raise ValueError("Signo positivo sin valor asociado")
            
            return hacerOperacion(operacion[:indiceCaracter]) + hacerOperacion(operacion[(indiceCaracter+1):])
        
        elif (operacion[indiceCaracter] == "-"):

            if(indiceCaracter==0):
                return hacerOperacion("0") - hacerOperacion(operacion[(indiceCaracter+1):])
            elif(indiceCaracter==len(operacion)-1):
                raise ValueError("Signo negativo sin valor asociado")
            
            return hacerOperacion(operacion[:indiceCaracter]) - hacerOperacion(operacion[(indiceCaracter+1):])
        
        indiceCaracter-=1

    #Checar agrupamiento sin par
    if(parentesisAbiertos!=0 or corchetesAbiertos!=0):
        raise ValueError("Error de agrupamiento")
    
    #Multiplicacion division
    indiceCaracter = len(operacion)-1
    while(indiceCaracter>=0):

        if(parentesisAbiertos ==0):
            corchetesAbiertos+=revisarCorchetes(operacion[indiceCaracter]) 

        if(corchetesAbiertos ==0):
            parentesisAbiertos+=revisarParentesis(operacion[indiceCaracter])

        if(parentesisAbiertos!=0 or corchetesAbiertos!=0):
            indiceCaracter-=1
            continue

        if (operacion[indiceCaracter] == "*"):

            if(indiceCaracter==0 or indiceCaracter==len(operacion)-1):
                raise ValueError("Signo de multiplicacion sin valor asociado")
            
            return hacerOperacion(operacion[:indiceCaracter]) * hacerOperacion(operacion[(indiceCaracter+1):])
        
        if (operacion[indiceCaracter] == "/"):

            if(indiceCaracter==0 or indiceCaracter==len(operacion)-1):
                raise ValueError("Signo de division sin valor asociado")
            
            return hacerOperacion(operacion[:indiceCaracter]) / hacerOperacion(operacion[(indiceCaracter+1):])
        
        indiceCaracter-=1    
    
    #Eliminar agrupamiento
    if(operacion[:1]=="(" and operacion[len(operacion)-1:]==")") or (operacion[:1]=="[" and operacion[len(operacion)-1:]=="]"):
        return hacerOperacion(operacion[1:-1])
    
    #Retornar numero
    if(operacion.isnumeric()):
        return float(operacion)
    else:
        raise ValueError("Error de sintaxis")

def revisarParentesis(caracter):
    if (caracter == "["): 
        return 1
    elif (caracter == "]"):
        return -1
    
    return 0

def revisarCorchetes(caracter):
    if (caracter == "("): 
        return 1

    elif (caracter == ")"):
        return -1
    
    return 0

            
print(hacerOperacion("((2-2/4)*8+3)*2"))