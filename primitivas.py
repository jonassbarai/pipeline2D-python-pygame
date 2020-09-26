
import math
from operator import attrgetter
class Ponto:
    def __init__(self, x = 0, y = 0, z = 0): #construtor.  self é oculto
        self.x = x
        self.y = y
        self.z = z
    pass

class Aresta:
    def __init__(self, yMax, xYMin, umSobreM, yMin):
        self.yMax = yMax
        self.xYMin = xYMin
        self.umSobreM = umSobreM
        self.yMin = yMin
    
    def CriacaoArestas(listaVertices):
        listaArestas = []

        listaVertices.append(listaVertices[0])
        for i in range(0, len(listaVertices) -1):
            if listaVertices[i].y > listaVertices[i+1].y:
                yMax = listaVertices[i].y
                yMin = listaVertices[i+1].y
                xYMin = listaVertices[i+1].x
            else:
                yMax = listaVertices[i+1].y
                yMin = listaVertices[i].y
                xYMin = listaVertices[i].x
            deltaX = listaVertices[i+1].x - listaVertices[i].x
            deltaY = listaVertices[i+1].y - listaVertices[i].y
            if deltaY==0:
                deltaY=1
            umSobreM = deltaX / deltaY
            
            arestaAtual = Aresta(yMax, xYMin, umSobreM, yMin)
            listaArestas.append(arestaAtual)
        return listaArestas
    pass     

class Primitivas:
    def ScanLine(listaVertices, matrizTela, cor):
        # criar as arestas
            # Podemos criar uma estrutura só pra elas
        # construir a TA
        ta = Aresta.CriacaoArestas(listaVertices)
        ta.sort(key = attrgetter('yMin'), reverse=False)

        #Selecionar a menor coordenada de Y na Ta
        yAtual = ta[0].yMin

            # ordenar a Ta pelo ymin
        # inicializar a TAA
        taa = []

        # laço 
        while len(ta) > 0 or len(taa) > 0:
            # pego os valores do yatual = ymin da Ta e jogo na TAA
            # Jogo na Taa

            # Atualizar os valores de X na TAA
            for i in range(0, len(taa)):
                taa[i].xYMin += taa[i].umSobreM

            #Verificar quem entra (yMin = yAtual)
            for i in range(len(ta) -1, -1, -1):
                if(ta[i].yMin == yAtual):
                    taa.append(ta.pop(i))   

            # Verificar quem sai (yMax = yAtual)
            for i in range(len(taa) - 1, -1, -1):
                if(taa[i].yMax == yAtual):
                    taa.pop(i)
            # Ordenar a TAA em relação a X
            taa.sort(key = attrgetter('xYMin'), reverse=False)

            # Arredondar esquerda pra cima e direita pra baixo
            # pintar no intervalo xi até xf
          
            #pintar os Pixels(arredondando)
            for i in range(0, len(taa)-1, 2):
                # Chamar bresenham funciona entre o Pi e o Pf
                xInicial = int(taa[i].xYMin + 0.5)
                xFinal = int(taa[i+1].xYMin)
                for xAtual in range(xInicial, xFinal +1):
                    matrizTela[xAtual, yAtual] = cor

            # incrementar y
            yAtual += 1

        pass
        
    def LinhaReta(pontoInicial, pontoFinal, matrizTela, cor):
    #Calculando e pintando na tela 
        deltaX = pontoFinal.x - pontoInicial.x
        deltaY = pontoFinal.y - pontoInicial.y
        
        m = deltaY / deltaX
        
        b = pontoInicial.y - m * pontoInicial.x

        for x in range(pontoInicial.x, pontoFinal.x):
            y = m * x + b
            matrizTela[x, int(y)] = cor
        pass

    #Linha Reta
    #Problemas em utilizar a equacao da Reta em CG
    #não criamos retas verticais, pois na mat. um f(x) só pode ter um valor de y para cada X e uma vertical seria inumeros valores para um mesmo X
    #outro ponto é indo de frente pra trás, teria q criar uns condicionais para solucionar o problema
    #O terceiro problema seria a demora do algoritmo. Pras muitas retas acaba sendo custoso pois pode ter milhares de retas em uma mesma cena
  
    def LinhaDDA(pontoInicial, pontoFinal, matrizTela, cor):
        
        deltaX = pontoFinal.x - pontoInicial.x
        deltaY = pontoFinal.y - pontoInicial.y

        if abs(deltaX) > abs(deltaY):
            i = abs(deltaX) 
        else:
            i = abs(deltaY)

        incrementoX = deltaX / i
        incrementoY = deltaY / i

        x = pontoInicial.x
        y = pontoInicial.y

        for k in range(i):
            matrizTela[int(x), int(y)] = cor
            x += incrementoX
            y += incrementoY
        pass

    #LinhaDDA
    #Parte do seguinte principio: Eventualmente vamos ter que pintar um pixel, nisso n precisamos fazer um calculo exato de cada pixel, Pintando um dos outros que estão ao redor
    #De um jeito ou de outro, se o incremento ficar em X OU Y vai ser uma constante por ser o Coeficiente Angular. 
    #Podendo fazer os calc dos outros pontos, graças ao valor constante que ja foi calculada (utilizando os acumuladores)


    def LinhaBresenhamBaixa(pontoInicial, pontoFinal, matrizTela, cor):

        deltaX = pontoFinal.x - pontoInicial.x
        deltaY = pontoFinal.y - pontoInicial.y

        incrementoY = 1

        if deltaY < 0:
            incrementoY = -1
            deltaY *= -1

        d = 2 * deltaY - deltaX

        y = pontoInicial.y

        for x in range(pontoInicial.x, pontoFinal.x):
            
            matrizTela[x, y] = cor

            if d > 0:
                y += incrementoY
                d -= 2 * deltaX
            
            d += 2 * deltaY

        pass

    def LinhaBresenhamAlta(pontoInicial, pontoFinal, matrizTela, cor):
       
        deltaX = int(pontoFinal.x - pontoInicial.x)
        deltaY = int(pontoFinal.y - pontoInicial.y)
        
        incrementoX = 1

        if deltaX < 0:
            incrementoX=-1
            deltaX= -1 * deltaX
        
        d = 2 * deltaX - deltaY
        x = pontoInicial.x

        for y in range(pontoInicial.y,pontoFinal.y):
            matrizTela[x,y] = cor
            if d >  0:
                x = x + incrementoX
                d = d - 2 * deltaY

            d= d+2 * deltaX
        pass

    def LinhaBresenham(pontoInicial, pontoFinal, matrizTela, cor):
        deltaX = pontoFinal.x - pontoInicial.x
        deltaY = pontoFinal.y - pontoInicial.y

        if abs(deltaY) < abs(deltaX):
            if pontoInicial.x > pontoFinal.x:
                Primitivas.LinhaBresenhamBaixa(pontoFinal,pontoInicial,matrizTela,cor)
            else:
                Primitivas.LinhaBresenhamBaixa(pontoInicial,pontoFinal,matrizTela,cor)
        else:
            if pontoInicial.y > pontoFinal.y:
                Primitivas.LinhaBresenhamAlta(pontoFinal,pontoInicial,matrizTela,cor)
            else:
                Primitivas.LinhaBresenhamAlta(pontoInicial,pontoFinal,matrizTela,cor)

        pass

    def Poligono(listaPontos, matrizTela, cor):
        # passando por todos os pontos, par a par e criar uma linha entre eles
        for i in range(0, len(listaPontos) - 1):
            Primitivas.LinhaBresenham(listaPontos[i], listaPontos[i + 1], matrizTela, cor)
        # No final eu tenho que ligar o ultimo ponto com o primeiro
        Primitivas.LinhaBresenham(listaPontos[len(listaPontos) -1], listaPontos[0], matrizTela, cor)
        pass  


    def CirculoBresenham(pontoCentral, raio, matrizTela, cor):
        x = 0 
        y = raio
        d = 1 - raio

        Primitivas.CirculoBresenhamSimetria(pontoCentral, Ponto(x,y), matrizTela, cor)

        while x < y:
            if d < 0:
                d = d + 2 * x + 3
            else:
                d = d + 2 * (x - y) + 5
                y = y - 1
            x = x + 1
            Primitivas.CirculoBresenhamSimetria(pontoCentral, Ponto(x,y), matrizTela, cor)

        pass

    def CirculoBresenhamSimetria(pontoCentral, pontoAtual, matrizTela, cor):
        matrizTela[pontoCentral.x + pontoAtual.x, pontoCentral.y + pontoAtual.y] = cor
        matrizTela[pontoCentral.x + pontoAtual.y, pontoCentral.y + pontoAtual.x] = cor
        matrizTela[pontoCentral.x + pontoAtual.y, pontoCentral.y - pontoAtual.x] = cor
        matrizTela[pontoCentral.x + pontoAtual.x, pontoCentral.y - pontoAtual.y] = cor
        matrizTela[pontoCentral.x - pontoAtual.x, pontoCentral.y - pontoAtual.y] = cor
        matrizTela[pontoCentral.x - pontoAtual.y, pontoCentral.y - pontoAtual.x] = cor
        matrizTela[pontoCentral.x - pontoAtual.y, pontoCentral.y + pontoAtual.x] = cor
        matrizTela[pontoCentral.x - pontoAtual.x, pontoCentral.y + pontoAtual.y] = cor
        pass
    pass

    