from primitivas import *
import math

def MatrizTranslacao(TX,TY):    
   return [[1,0,TX],[0,1,TY],[0,0,1]]
   
def MatrizEscala(SX,SY):
    return [[SX,0,0],[0,SY,0],[0,0,1]]

def MatrizRotacao(graus):
    sin = math.sin(graus)
    cos = math.cos(graus)

    return [[cos,-sin,0],[sin,cos,0],[0,0,1]]

def MatrizEspelhamento(eixo):
    if eixo =='x':
        return [[1,0,0],[0,-1,0],[0,0,1]]
    elif eixo =='y':
        return [[-1,0,0],[0,1,0],[0,0,1]] 
    else:
        return [[-1,0,0],[0,-1,0],[0,0,1]]

def MatrizCisalhamento(eixo,SH):
    if eixo =='x':
        return [[1,SH,0],[0,1,0],[0,0,1]]
    else:
        return [[1,0,0],[SH,1,0],[0,0,1]]

#modificar essa função para que funcione com uma lista de matrizes
#for inverso
def multiplicaMatriz(A,B):
    C=[]
    for linha in range(len(A)):
        #cria linha vazia
        C.append([])
        for coluna in range(len(B[0])):
        #adiciona uma nova coluna na linha
            C[linha].append(0)
            for k in range(len(A[0])):
                C[linha][coluna] += A[linha][k] *B[k][coluna]
    return C

def multiplicaVariasMatrizes(listaMatrizes):
    matrizAux = multiplicaMatriz(listaMatrizes[len(listaMatrizes)-2],listaMatrizes[len(listaMatrizes)-1])
    for m in range(len(listaMatrizes)-3, -1, -1):
        matrizAux = multiplicaMatriz(listaMatrizes[m],matrizAux)

    return matrizAux

def pontoCentral(listaVertices):
    mediaX=0
    mediaY=0
    for i in range(0,len(listaVertices)):
        mediaX += listaVertices[i].x
        mediaY += listaVertices[i].y
    mediaX =int(mediaX/len(listaVertices))
    mediaY = int(mediaY/len(listaVertices))

    return Ponto(mediaX,mediaY)    

def transformada(listaVertices,listaTransformadas):
    listaVerticeNovos =[]
    pcentro = pontoCentral(listaVertices)    
    listaTransformadas.insert(0,MatrizTranslacao(pcentro.x,pcentro.y))
    listaTransformadas.append(MatrizTranslacao(-pcentro.x,-pcentro.y))
    for i in range(0,len(listaVertices)):
        
        MatrizPonto = [[listaVertices[i].x],[listaVertices[i].y],[1]]
        resultado = multiplicaVariasMatrizes(listaTransformadas)
        resultado = multiplicaMatriz(resultado,MatrizPonto)        

        xNovo=int(resultado[0][0])
        yNovo=int(resultado[1][0])
        zNovo=int(resultado[2][0])
        listaVerticeNovos.append(Ponto(xNovo,yNovo,zNovo))      

    return listaVerticeNovos


class ViewPort:
    def __init__ (self,pontoMinJD,pontoMaxJD,pontoMinVP,pontoMaxVP):
        self.pontoMinJD = pontoMinJD
        self.pontoMaxJD = pontoMaxJD
        self.pontoMinVP = pontoMinVP        
        self.pontoMaxVP = pontoMaxVP
        
    pass

def Mapeamento(listaVertices,viewport):
    equacao1=(viewport.pontoMaxVP.x-viewport.pontoMinVP.x)/(viewport.pontoMaxJD.x-viewport.pontoMinJD.x)
    equacao2=(viewport.pontoMaxVP.y-viewport.pontoMinVP.y)/(viewport.pontoMaxJD.y-viewport.pontoMinJD.y)
    listaVerticeNovos =[]
    mapeamentoVP =[MatrizTranslacao(viewport.pontoMinVP.x,viewport.pontoMinVP.y),MatrizEscala(equacao1,equacao2),MatrizTranslacao(-viewport.pontoMinJD.x,-viewport.pontoMinJD.y)]
    for i in range(0,len(listaVertices)):                
        matrizPonto = [[listaVertices[i].x],[listaVertices[i].y],[1]]    
        resultado = multiplicaVariasMatrizes(mapeamentoVP)
        resultado = multiplicaMatriz(resultado,matrizPonto)    

        xNovo=int(resultado[0][0])
        yNovo=int(resultado[1][0])
        zNovo=int(resultado[2][0])
        listaVerticeNovos.append(Ponto(xNovo,yNovo,zNovo))      

    return listaVerticeNovos



