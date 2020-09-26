from primitivas import *
from transformadas import *
from Recorte import *
from CohenSutherlandClip import *

def DesenhaPonto(ponto,viewport,matrizTela,cor):
    estaNaTela = Recorte.recortePonto(ponto,viewport)   
    listaPonto=[ponto]    
    if estaNaTela:
        NovoPonto=Mapeamento(listaPonto,viewport)
        matrizTela[NovoPonto[0].x][NovoPonto[0].y] = cor    
    pass
def DesenhaReta(ponto1,ponto2,viewport,matrizTela,cor):   
    listaReta=[ponto1,ponto2]
    naTela= Recorte.recorteReta(ponto1,ponto2,viewport)    
    if naTela:
        Novospontos = Mapeamento(listaReta,viewport)        
        Primitivas.LinhaBresenham(Novospontos[0],Novospontos[1],matrizTela,cor) 
    pass

def DesenhaPoligono(listaVertices, viewport,matrizTela,cor): 
    verticesRecortados =Recorte.recortePoligono(listaVertices,viewport)   
    if(len(verticesRecortados)>0):
        Novospontos = Mapeamento(verticesRecortados,viewport)
        Primitivas.Poligono(Novospontos,matrizTela, cor)
    pass
def DesenhaScanLine(listaVertices, viewport,matrizTela,cor):
    verticesRecortados =Recorte.recortePoligono(listaVertices,viewport)   
    if(len(verticesRecortados)>0):
        Novospontos = Mapeamento(verticesRecortados,viewport)
        Primitivas.ScanLine(Novospontos,matrizTela, cor)
    pass


