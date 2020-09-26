from primitivas import *
from transformadas import *


INSIDE = 0  # 0000 
LEFT = 1    # 0001 
RIGHT = 2   # 0010 
BOTTOM = 4  # 0100 
TOP = 8     # 1000

# | bitwise or
# & bitwise and

def CodigoBin(ponto,viewport): 
    x_max = viewport.pontoMaxJD.x
    y_max = viewport.pontoMaxJD.y
    x_min = viewport.pontoMinJD.x
    y_min = viewport.pontoMinJD.y

    codigo = 0b0000
    if ponto.x < x_min:      # Esquerda
        codigo+=0b0001 
    if ponto.x > x_max:    # direita
        codigo+=0b0010 
    if ponto.y < y_min:      # esquerda
        codigo+=0b0100  
    if ponto.y > y_max:    # abaixo
        codigo+=0b1000 
  
    return codigo

def limitaEsquerda(listaVertices, x_min):
    recorteEsquerda=[]
    listaVertices.append(listaVertices[0])
    for i in range(0,len(listaVertices)-1):
        if listaVertices[i].x  >= x_min  and listaVertices[i+1].x >= x_min:
            recorteEsquerda.append(listaVertices[i+1])
        elif listaVertices[i].x  >=x_min  and listaVertices[i+1].x <= x_min:
            yNovo = listaVertices[i].y + (listaVertices[i+1].y -listaVertices[i].y) *(x_min - listaVertices[i].x) / (listaVertices[i+1].x - listaVertices[i].x) 
            xNovo = x_min
            listaVertices[i]=Ponto(xNovo,yNovo)
            recorteEsquerda.append(Ponto(xNovo,yNovo))
        elif listaVertices[i].x  <= x_min  and listaVertices[i+1].x >= x_min:
            yNovo = listaVertices[i].y + (listaVertices[i+1].y -listaVertices[i].y) *(x_min - listaVertices[i].x) / (listaVertices[i+1].x - listaVertices[i].x)
            xNovo = x_min
            listaVertices[i]=Ponto(xNovo,yNovo)
            recorteEsquerda.append(Ponto(xNovo,yNovo))
            recorteEsquerda.append(listaVertices[i+1])
    return recorteEsquerda

def limitaDireita(listaVertices, x_max):
  
    recorteDireita=[]
    ponto1=listaVertices[0]
    listaVertices.append(ponto1)
    for i in range(0,len(listaVertices)-1):
        if listaVertices[i].x  <= x_max  and listaVertices[i+1].x <= x_max:
            recorteDireita.append(listaVertices[i+1])
        elif listaVertices[i].x  <= x_max  and listaVertices[i+1].x >= x_max:
            yNovo =listaVertices[i].y + (listaVertices[i+1].y -listaVertices[i].y) *(x_max - listaVertices[i].x) / (listaVertices[i+1].x - listaVertices[i].x) 
            xNovo = x_max
            listaVertices[i]=Ponto(xNovo,yNovo)
            recorteDireita.append(Ponto(xNovo,yNovo))
        elif listaVertices[i].x  >= x_max  and listaVertices[i+1].x <= x_max:
            yNovo = listaVertices[i].y + (listaVertices[i+1].y -listaVertices[i].y) *(x_max - listaVertices[i].x) / (listaVertices[i+1].x - listaVertices[i].x)
            xNovo = x_max
            listaVertices[i]=Ponto(xNovo,yNovo)
            recorteDireita.append(Ponto(xNovo,yNovo))
            recorteDireita.append(listaVertices[i+1])
    return recorteDireita

def limitaCima(listaVertices, y_max):
    recorteCima=[]
    listaVertices.append(listaVertices[0])
    for i in range(0,len(listaVertices)-1):
        if listaVertices[i].y  <= y_max  and listaVertices[i+1].y <= y_max:
            recorteCima.append(listaVertices[i+1])
        elif listaVertices[i].y  <= y_max  and listaVertices[i+1].y >= y_max:
            yNovo = y_max 
            xNovo =listaVertices[i].x + (listaVertices[i+1].x - listaVertices[i].x) * (y_max - listaVertices[i].y) / (listaVertices[i+1].y - listaVertices[i].y)
            listaVertices[i]=Ponto(xNovo,yNovo)
            recorteCima.append(Ponto(xNovo,yNovo))
        elif listaVertices[i].y  >= y_max  and listaVertices[i+1].y <= y_max:
            yNovo = y_max
            xNovo = listaVertices[i].x + (listaVertices[i+1].x - listaVertices[i].x) * (y_max - listaVertices[i].y) / (listaVertices[i+1].y - listaVertices[i].y)
            listaVertices[i]=Ponto(xNovo,yNovo)
            recorteCima.append(Ponto(xNovo,yNovo))
            recorteCima.append(listaVertices[i+1])
    return recorteCima

def limitaBaixo(listaVertices, y_min):
    recorteBaixo=[]
    listaVertices.append(listaVertices[0])
    for i in range(0,len(listaVertices)-1):
        if listaVertices[i].y  >= y_min  and listaVertices[i+1].y >= y_min:
            recorteBaixo.append(listaVertices[i+1])
        elif listaVertices[i].y  >= y_min  and listaVertices[i+1].y <= y_min:
            yNovo = y_min 
            xNovo =listaVertices[i].x + (listaVertices[i+1].x - listaVertices[i].x) * (y_min - listaVertices[i].y) / (listaVertices[i+1].y - listaVertices[i].y)
            listaVertices[i]=Ponto(xNovo,yNovo)
            recorteBaixo.append(Ponto(xNovo,yNovo))
        elif listaVertices[i].y  <= y_min  and listaVertices[i+1].y >= y_min:
            yNovo = y_min
            xNovo = listaVertices[i].x + (listaVertices[i+1].x - listaVertices[i].x) * (y_min - listaVertices[i].y) / (listaVertices[i+1].y - listaVertices[i].y)
            listaVertices[i]=Ponto(xNovo,yNovo)
            recorteBaixo.append(Ponto(xNovo,yNovo))
            recorteBaixo.append(listaVertices[i+1])
    return recorteBaixo
    
class Recorte:   

    def recortePonto(ponto, viewport):
        if(viewport.pontoMaxJD.x > ponto.x 
        and viewport.pontoMinJD.x < ponto.x
        and viewport.pontoMaxJD.y > ponto.y
        and viewport.pontoMinJD.y < ponto.y ):            
            return True       
        return False

    def recorteReta(ponto1,ponto2,viewport): 
        x_max = viewport.pontoMaxJD.x
        y_max = viewport.pontoMaxJD.y
        x_min = viewport.pontoMinJD.x
        y_min = viewport.pontoMinJD.y  
   
        code1 = CodigoBin(ponto1,viewport) 
        code2 = CodigoBin(ponto2,viewport) 
        accept = False
  
        while True:  
        
            if code1 == 0 and code2 == 0: 
                accept = True
                break
    
        
            elif (code1 & code2) != 0: 
                break  
            
            else:  
                
                x = 1.0
                y = 1.0
                if code1 != 0: 
                    code_out = code1 
                else: 
                    code_out = code2   
                
                if code_out & TOP:                 
                    
                    x = ponto1.x + (ponto2.x - ponto1.x) * (y_max - ponto1.y) / (ponto2.y - ponto1.y) 
                    y = y_max 
    
                if code_out & BOTTOM:                   
                    
                    x = ponto1.x + (ponto2.x - ponto1.x) *(y_min - ponto1.y) / (ponto2.y - ponto1.y) 
                    y = y_min
                    
                if code_out & RIGHT:                  
                    
                    y = ponto1.y + (ponto2.y - ponto1.y) * (x_max - ponto1.x) / (ponto2.x - ponto1.x) 
                    x = x_max             
    
                if code_out & LEFT:                  
                    
                    y = ponto1.y + (ponto2.y - ponto1.y) *(x_min - ponto1.x) / (ponto2.x - ponto1.x) 
                    x = x_min 

                if code_out == code2: 
                    ponto2.x = x 
                    ponto2.y = y 
                    code2 = CodigoBin(ponto2,viewport)

                else: 
                    ponto1.x = x 
                    ponto1.y = y 
                    code1 = CodigoBin(ponto1,viewport)
                    
        return accept

    def recortePoligono(listaVertices,viewport):
        x_max = viewport.pontoMaxJD.x
        y_max = viewport.pontoMaxJD.y
        x_min = viewport.pontoMinJD.x
        y_min = viewport.pontoMinJD.y
        verticesRecortados=[]
        limitadoEsquerda=[]
        limitadoBaixo=[]
        limitadoDireita=[]

        limitadoEsquerda=limitaEsquerda(listaVertices,x_min)
        if len(limitadoEsquerda)>0:
            limitadoBaixo = limitaBaixo(limitadoEsquerda,y_min)    
        if len(limitadoBaixo)>0:            
            limitadoDireita = limitaDireita(limitadoBaixo,x_max)
        if len(limitadoDireita)>0:
            #print(limitadoDireita[0].x,limitadoBaixo[1].x,limitadoBaixo[2].x) 
            verticesRecortados = limitaCima(limitadoDireita,y_max)
            #print(verticesRecortados[0].x,verticesRecortados[1].x,verticesRecortados[2].x)         

        return verticesRecortados      
        
    pass