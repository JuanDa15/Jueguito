import pygame
import math
width = 1280
high = 920
middle = [width/2,high/2]

#Funcion que crea una linea
def createLine(window,initialPos,finalPos,color):
    pygame.draw.line(window, color, initialPos, finalPos, 2)
    pygame.display.flip()
    
#Funcion para dibujar un triangulo, la cual recibe la ventana y 3 puntos
def CreateTriangle(window,pointA,pointB,pointC):
    pygame.draw.line(window, [255,255,255], [pointA[0],pointA[1]], [pointB[0],pointB[1]], 2)
    pygame.draw.line(window, [255,255,255], [pointB[0],pointB[1]], [pointC[0],pointC[1]], 2)
    pygame.draw.line(window, [255,255,255], [pointC[0],pointC[1]], [pointA[0],pointA[1]], 2)
    pygame.display.flip()
    
def CreateTriangleList(window,listPos,color):
    pygame.draw.line(window, color, [listPos[0][0],listPos[0][1]], [listPos[1][0],listPos[1][1]], 2)
    pygame.draw.line(window, color, [listPos[1][0],listPos[1][1]], [listPos[2][0],listPos[2][1]], 2)
    pygame.draw.line(window, color, [listPos[2][0],listPos[2][1]], [listPos[0][0],listPos[0][1]], 2)
    pygame.display.flip()

def drawPolygon(window,color,positions):
    pygame.draw.polygon(window,color, positions, 1)
    pygame.display.flip()

def drawPolygonSolid(window,color,positions):
    pygame.draw.polygon(window,color, positions)
    pygame.display.flip()
#---------------------------------------------------------------------------------------------
#Funcion que crea un triangulo a partir de un punto recibido por el click
#parametros: ventana, punto
def CreateTriangleClick(window,point):
    PointB = [point[0]+50,point[1]]
    PointC = [point[0]+50,point[1]-50]
    
    pygame.draw.line(window,[255,255,255], point,PointB,2)
    pygame.draw.line(window,[255,255,255], PointB,PointC,2)
    pygame.draw.line(window,[255,255,255], PointC,point,2)
    pygame.display.flip()
#---------------------------------------------------------------------------------------------
#Funcion que dibuja un punto la cual tiene por parametros la ventana, centro, color
def CreatePoint(window,Center,color):
    pygame.draw.circle(window,color, Center, 5)
    pygame.display.flip()

def Createcircle(window,Center,color,radius):
    pygame.draw.circle(window,color, Center, radius,1)
    pygame.display.flip()
#---------------------------------------------------------------------------------------------
#Funcion que actualiza las posiciones de un arreglo(modelo)
#parametros: Ventana sobre la cual se trabaja, Listas de Posiciones
def UpdatePoint(window,LeftList,RightList):
    for position in LeftList:
        position[0] = position[0] - 2
        if position[0] < 0:
            position[0] = 1080
        CreatePoint(window,position,[255,0,0])
    for position in RightList:
        position[0] = position[0] + 2
        if position[0] > 1080:
            position[0] = 0
        CreatePoint(window,position,[255,255,0])
    clock.tick(60)
    window.fill([0,0,0])
#---------------------------------------------------------------------------
#Funcion que convierte tuplas en listas de enteros
#parametros: recibe una tupla , retorna una lista
def ConvertIntList(tuple):
    Xcoord = int (tuple[0])
    Ycoord = int (tuple[1])
    return [Xcoord,Ycoord]
#-----------------------------------------------------------------------------------------
#Funcion que une dos triangulos a travez de lineas
#parametros: recibe la ventana, el punto de inicio del primer triangulo y el punto de inicio del segundo
def linkTriangles(window,pointA,pointB):
    pygame.draw.line(window, [255,255,255], pointA, pointB, 1)
    pygame.draw.line(window, [255,255,255], [pointA[0]+50,pointA[1]], [pointB[0] + 50, pointB[1]], 1)
    pygame.draw.line(window, [255,255,255], [pointA[0]+50,pointA[1] - 50], [pointB[0] + 50,pointB[1] - 50], 1)
    pygame.display.flip()
#--------------------------------------------------------------------------
#funcion que dibuja un patron
#parametros: recibe la ventana, el alto de la ventana y la posicion en la que empieza el x
def drawPatron(window,high,xposition):
    high = high - 5
    sideLenght = 15 #Medida en pixeles
    pygame.draw.line(window, [255,0,255], [xposition,(high - sideLenght)], [(xposition + sideLenght),(high - sideLenght)], 1)
    pygame.draw.line(window, [255,0,255], [(xposition + sideLenght),(high - sideLenght)],[(xposition + sideLenght),high], 1)
    pygame.draw.line(window, [255,0,255], [(xposition + sideLenght),high], [xposition,high], 1)
    pygame.draw.line(window, [255,0,255], [xposition,high], [xposition,(high - (sideLenght - 5))], 1)
    pygame.draw.line(window, [255,0,255], [xposition,(high - (sideLenght - 5))], [sideLenght - 5 + xposition,(high - (sideLenght - 5))],1)
    pygame.draw.line(window, [255,0,255], [sideLenght - 5 + xposition,(high - (sideLenght - 5))], [sideLenght - 5 + xposition,high - (sideLenght - 10)], 1)
    pygame.draw.line(window, [255,0,255], [sideLenght - 5 + xposition,high - (sideLenght - 10)], [sideLenght - 10 + xposition,high - (sideLenght - 10)], 1)
    pygame.display.flip()
#-----------------------------------------------------------------------------------------------------------
#funciones que mueven un poligono a la derecha y a la izquierda
#reciben como parametro la ventana y la lista de posiciones
def movePolygonLeft(positions,window):
    window.fill([0,0,0])
    pygame.draw.polygon(window, [255,0,0], positions, 1)
    for position in positions:
        position[0] = position[0] - 5
        if position[0] < 0:
            position[0] = 1090
    pygame.display.flip()

def movePolygonRight(positions,window):
    window.fill([0,0,0])
    pygame.draw.polygon(window, [255,0,0], positions, 1)
    for position in positions:
        position[0] = position[0] + 5
        if position[0] > 1080:
            position[0] = 0
    pygame.display.flip()
#---------------------------------------------------------------------
#Funcion que dibuja un plano cartesiano
#parametros:  ventana y el punto donde inicia el plano
def drawPlane(window,center):
    pygame.draw.line(window, [255,255,255], [center[0],0], [center[0],high], 1)
    pygame.draw.line(window, [255,255,255], [0,center[1]], [width,center[1]], 1)
    pygame.display.flip()
#-----------------------------------------------------------------------
#funcion que actualiza la posicion donde esta el medio dell plano
#parametro: posicion nueva
def updateMiddle(pos):
    coordX = pos[0]
    coordY = pos[1]
    middle = [coordX,coordY]
    return middle
#---------------------------------------------------------------------------
def orderPoints(window,center):
    point1 = [center[0] + 100,center[1] + 100]
    point2 = [center[0] - 100,center[1] + 50]
    point3 = [center[0] + 100,center[1] - 50]
    point4 = [center[0] - 100,center[1] - 100]
    
    CreatePoint(window,point1,[255,255,255])
    CreatePoint(window,point2,[255,255,255])
    CreatePoint(window,point3,[255,255,255])
    CreatePoint(window,point4,[255,255,255])
#------------------------------------------------------------------------------
#transfformacion de cualquier punto a cualquiera de los 4 cuadrantes
#parametros: centro del plano cartesiano, posicion a transformar
#retorna la posicion transformada
def transformada1Cuadrante(center,pos):
    transformX = pos[0] - center[0]
    transformY = center[1] - pos[1]
    return [transformX,transformY]

def transformada2Cuadrante(center,pos):
    transformX = pos[0] - center[0]
    transformY = center[1] - pos[1]
    return [transformX,transformY]

def transformada3Cuadrante(center,pos):
    transformX = pos[0] - center[0]
    transformY = center[1] - pos[1]
    return [transformX,transformY]

def transformada4Cuadrante(center,pos):
    transformX = pos[0] - center[0]
    transformY = center[1] - pos[1]
    return [transformX,transformY]
#----------------------------------------------------------------------
#transforma coordenadas cartesianas a coordenadas de pantalla
#parametro: recibe el centro del plano cartesiano y la posicion   
def CartToScreen(middle,point):
    coordX = middle[0] + point[0]
    coordY = middle[1] - point[1]
    return [coordX,coordY]
#-----------------------------------------------------------------------------
#Convertir coordenadas de pantalla a coordenadas cartesianas
#parametros: Recibe el centro  y la posicion
def ScreenToCart(center,pos):
    if((pos[0] >= center[0]) and (pos[1] <= center[1])):
        PosTransformada = transformada1Cuadrante(center,pos)
        return PosTransformada
    elif((pos[0] < center[0]) and (pos[1] <= center[1])):
        PosTransformada = transformada2Cuadrante(center,pos)
        return PosTransformada
    elif((pos[0] < center[0]) and (pos[1] > center[1])):
        PosTransformada = transformada3Cuadrante(center,pos)
        return PosTransformada
    elif((pos[0] >= center[0]) and (pos[1] > center[1])): 
        PosTransformada = transformada4Cuadrante(center,pos)
        return PosTransformada
    

def CartesianoAPantalla(Centro,Punto): #pasa de coordenadas cartesianas a pantalla
    PuntoX = Centro[0] + Punto[0]
    PuntoY = Centro[1] - Punto[1]
    PuntoFinal = [PuntoX,PuntoY]
    return PuntoFinal

def PantallaACartesiano(Medio, Punto):
    C = 0
    if Punto[0] >= Medio[0] and Punto[1] <= Medio[1]:
        C = 1
    if Punto[0] < Medio[0] and Punto[1] <= Medio[1]:
        C = 2
    if Punto[0] < Medio[0] and Punto[1] > Medio[1]:
        C = 3
    if Punto[0] >= Medio[0] and Punto[1] > Medio[1]:
        C = 4

    if C == 1:
        PuntoX = Punto[0] - Medio[0]
        PuntoY = Medio[1] - Punto[1]
        PuntoFinal = [PuntoX,PuntoY]
        return PuntoFinal
    if C == 2:
        PuntoX = Punto[0] - Medio[0]
        PuntoY = Medio[1] - Punto[1]
        PuntoFinal = [PuntoX,PuntoY]
        return PuntoFinal
    if C == 3:
        PuntoX = Punto[0] - Medio[0]
        PuntoY = Medio[1] - Punto[1]
        PuntoFinal = [PuntoX,PuntoY]
        return PuntoFinal
    if C == 4:
        PuntoX = Punto[0] - Medio[0]
        PuntoY = Medio[1] - Punto[1]
        PuntoFinal = [PuntoX,PuntoY]
        return PuntoFinal
#--------------------------------------------------------------------------------
#Funcion que suma vectores
#recibe la magnitud del vector 1 y del vector 2 
#Devuelve la magnitud del 3 vector
def vectorAdd(vector1Lenght,vector2lenght):
    productx = vector1Lenght[0] + vector2lenght[0]
    producty = vector1Lenght[1] + vector2lenght[1]
    return [productx,producty]
#------------------------------------------------------------------------
#Funcion que saca la pendiente de una recta
#parametros: Recibe 2 puntos de la recta, retorna la pendiente
def getSlope(Point1,Point2):
    Ycoord = float(Point2[1] - Point1[1])
    Xcoord = float(Point2[0] - Point1[0])
    Slope = float(Ycoord/Xcoord)
    return Slope
#------------------------------------------------------------------------
#Funcion que saca el corte de la recta con el eje y
#paremetros: recibe como parametro  un punto y la pendiente de la recta,returna el punto de corte
def corteY(point,slope):
    b = float(point[1]- (slope * point[0]))
    return b
#---------------------------------------------------------------------------
#funcion que dibuja la ecucacion de una recta
def recta(window,middle,pendiente,Corte):
    x = 0
    y = 0
    index = 0 - middle[0]
    while index < width:
        x = index
        y = (pendiente*x) + Corte
        t = CartToScreen(middle,[x,y])
        pygame.draw.circle(window, [255,255,255],[int(t[0]),int(t[1])], 2)
        index += 1
        pygame.display.flip()
        
#funcon que escala una figura a la medida deseada
def escalar (point,PorcentajeEscalamiento):
    CordEscaladaX = point[0] * PorcentajeEscalamiento
    CordEscaladaY = point[1] * PorcentajeEscalamiento
    return [CordEscaladaX,CordEscaladaY]

#-------------------------------------------------
#Funcion para rotar un punto en forma horaria, para que funcione en forma antihoraria enviar el angulo en negativo
def RotacionHoraria(point,angle):
    x = point[0]
    y = point[1]
    Xrot = ((x*(math.cos(math.radians(angle)))) + (y*(math.sin(math.radians(angle)))))
    Yrot = (((-1*x)*(math.sin(math.radians(angle)))) + (y*(math.cos(math.radians(angle)))))
    return [int(Xrot),int(Yrot)]
#-------------------------------------------------------------------
#Funcion para trasladar un punto
#paremetros,Punto,Dezplazamiento x, Desplazamiento en y
def Traslacion(point, CantX,CantY):
    XTrasladada = point[0] + CantX
    Ytrasladada = point[1] + CantY
    return [XTrasladada,Ytrasladada]
#-------------------------------------------------------------------
def CartesianToPolars(Position):
    p = math.sqrt(Position[0]**2 + Position[1]**2)
    angle = math.atan(Position[0]/Position[1])
    return[angle,p]

def PolarToCartesian(p,angle):
    angleRadians = math.radians(angle)
    X = p * math.cos(angleRadians)
    Y = p * math.sin(angleRadians)
    return [int(X),int(Y)]

def SelectColor(ColorName):
    if ColorName == 'Yellow':
        return [255,255,0]
    if ColorName == 'Blue':
        return [0,0,255]
    if ColorName == 'Red':
        return [255,0,0]
    if ColorName == 'Green':
        return [0,255,0]
    if ColorName == 'White':
        return [255,255,255]
    if ColorName == 'Purple':
        return [255,0,255]
    if ColorName == 'Light Blue':
        return [0,255,255]
    if ColorName == 'Gray1':
        return [100,100,100]
    if ColorName == 'Gray2':
        return [200,200,200]
    if ColorName == 'Gray3':
        return [50,50,50]