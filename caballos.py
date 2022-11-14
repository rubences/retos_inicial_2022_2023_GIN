#problema de caballos tablero 8x8  
# calcular posibles movimientos validos de un caballo en un tablero de ajedrez
#cantidad de movimiento validos
#posicion inicial
#posicion final



def caballos(x,y):
    #posiciones validas
    posiciones = []
    #movimientos posibles
    movimientos = [[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1],[-1,2]]
    #recorrer movimientos
    for i in movimientos:
        #posicion x
        x1 = x + i[0]
        #posicion y
        y1 = y + i[1]
        #verificar que la posicion sea valida
        if x1 >= 0 and x1 < 8 and y1 >= 0 and y1 < 8:
            #agregar posicion a la lista
            posiciones.append([x1,y1])
    #retornar lista de posiciones
    return posiciones

#cantidad de movimientos validos
print(len(caballos(0,0)))



   

if __name__ == "__main__":
    import doctest

    doctest.testmod()