import os
from sys import exit
import pygame
from primitivas import *
from transformadas import *
from Recorte import *
from DesenhaTela import *

windowTitle = 'Computação Gráfica - Aula 1'
screenWidth = 701
screenHeight = 701

passoX = 0
passoY = 0
zoom = 0 
vai = 0
	
# PYGAME ******************************

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
windowSurface = pygame.display.set_mode((screenWidth, screenHeight), 0, 24)
pygame.display.set_caption(windowTitle)
pixArray = pygame.PixelArray(windowSurface)
pygame.key.set_repeat(1, 10)
	
runProgram = True
while runProgram:
# Programa ******************************
	
	# Apagando todos os pixels
	for i in range (0, pixArray.shape[0]):
		for j in range (0, pixArray.shape[1]):
			pixArray[i, j] = 0x000000
	

	#Primitivas.LinhaReta(Ponto(10,15), Ponto(150,300), pixArray, 0xFFFFFF)
	#Primitivas.LinhaReta(Ponto(10,300), Ponto(150,300), pixArray, 0xFF00FF)
	#Primitivas.LinhaBresenhamBaixa(Ponto(150,180), Ponto(228,200), pixArray, 0x00FF00)
	#Primitivas.LinhaBresenhamAlta(Ponto(200,60), Ponto(250,300), pixArray, 0xAAAA00)
	#Primitivas.LinhaBresenham(Ponto(200,60), Ponto(250,300), pixArray, 0x00FF00)

	viewport =ViewPort(Ponto(0+passoX,0+passoY),Ponto(700+passoX+zoom,700+passoY+zoom),Ponto(0,0),Ponto(700,700))
	
	meusPontos=[Ponto(300, 400), Ponto(700,350),Ponto(610,400),Ponto(650,200)]	
	trianguloCoordenadas=[Ponto(50,150),Ponto(150,150),Ponto(100,50)]			
	quadradoCoordenadas=[Ponto(50,150),Ponto(150,150),Ponto(150,200),Ponto(50,200)]
	bj1Coordenadas=[Ponto(940,350),Ponto(880,430),Ponto(810,390), Ponto(870,310)]
	hexagonoCoordenadas =[Ponto(50,350),Ponto(100,300),Ponto(150,300),Ponto(200,350),Ponto(150,400),Ponto(100,400)]

	#DesenhaPonto(Ponto(699,699),viewport,pixArray,0xFFFFFF)
	#DesenhaPonto(Ponto(699,700),viewport,pixArray,0xFFFFFF)
	#DesenhaPonto(Ponto(700,699),viewport,pixArray,0xFFFFFF)
	#DesenhaPonto(Ponto(700,700),viewport,pixArray,0xFFFFFF)
	
	#DesenhaReta(Ponto(300,-30),Ponto(704,700),viewport,pixArray, 0x00FF00)

	#DesenhaReta(Ponto(300,400),Ponto(300,600),viewport,pixArray, 0x00FF00)
	#DesenhaReta(Ponto(150,180), Ponto(228,200),viewport, pixArray, 0x00FF00)
	#DesenhaReta(Ponto(150,180), Ponto(228,200),viewport, pixArray, 0x00FF00)
	#DesenhaReta(Ponto(0,0), Ponto(700,700),viewport, pixArray, 0x00FF00)
	#DesenhaReta(Ponto(500,0), Ponto(0,500),viewport, pixArray, 0x00FF00)
	

	
	#print(Recorte.recorteReta(Ponto(50,30), Ponto(699,500),viewport))
	
	#Modificações - Estrutura
	DesenhaReta(Ponto(0,600),Ponto(1500,600),viewport,pixArray, 0xFFFFFF)

	#trapezioCoordenadas=[Ponto(400,200),Ponto(450,140),Ponto(550,140),Ponto(600,200)]
	#listaTransformada=[MatrizTranslacao(0,100)]
	#NovoTrapezio = transformada(trapezioCoordenadas,listaTransformada)
	#DesenhaScanLine(NovoTrapezio,viewport,pixArray,0xe59400)
	#quadradoCoordenadas=[Ponto(450,200),Ponto(550,200),Ponto(550,300),Ponto(450,300)]
	#listaTransformada=[MatrizTranslacao(0,100)]
	#NovoQuadrado = transformada(quadradoCoordenadas,listaTransformada)
	#DesenhaScanLine(NovoQuadrado,viewport,pixArray,0x664200)

	DesenhaReta(Ponto(123,515),Ponto(164,521),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(123,515),Ponto(123,392),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(123,392),Ponto(164,386),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(122,396),Ponto(100,392),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(100,392),Ponto(164,380),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(100,392),Ponto(100,384),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(100,384),Ponto(164,370),viewport,pixArray, 0xFFFFFF)

	DesenhaReta(Ponto(164,342),Ponto(148,334),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(148,334),Ponto(256,304),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(164,339),Ponto(256,314),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(148,334),Ponto(148,312),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(148,312),Ponto(256,284),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(164,530),Ponto(164,339),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(164,530),Ponto(256,540),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(256,540),Ponto(256,315),viewport,pixArray, 0xFFFFFF)

	DesenhaReta(Ponto(256,540),Ponto(328,525),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(328,525),Ponto(328,339),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(328,339),Ponto(256,314),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(346,338),Ponto(256,304),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(328,341),Ponto(346,338),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(346,338),Ponto(346,317),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(346,317),Ponto(256,284),viewport,pixArray, 0xFFFFFF)

	DesenhaReta(Ponto(600,600),Ponto(600,0),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(328,501),Ponto(531,480),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(531,480),Ponto(551,480),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(551,480),Ponto(600,480),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(328,410),Ponto(531,438),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(531,440),Ponto(531,480),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(328,413),Ponto(531,440),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(328,405),Ponto(531,435),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(531,440),Ponto(531,435),viewport,pixArray, 0xFFFFFF)

	DesenhaReta(Ponto(531,440),Ponto(600,440),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(531,440),Ponto(600,440),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(531,435),Ponto(600,435),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(531,438),Ponto(600,438),viewport,pixArray, 0xFFFFFF)

	#arma
	DesenhaReta(Ponto(157,18),Ponto(422,18),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(366,17),Ponto(385,10),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(385,10),Ponto(422,10),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(422,10),Ponto(422,18),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(400,10),Ponto(421,1),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(422,18),Ponto(422,27),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(422,1),Ponto(422,9),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(187,14),Ponto(192,18),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(187,14),Ponto(158,13),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(158,13),Ponto(156,11),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(156,11),Ponto(154,9),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(154,9),Ponto(148,9),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(156,11),Ponto(154,9),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(154,9),Ponto(148,9),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(148,9),Ponto(146,13),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(146,13),Ponto(146,22),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(156,11),Ponto(154,9),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(154,9),Ponto(148,9),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(148,9),Ponto(146,13),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(146,13),Ponto(146,22),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(148,23),Ponto(151,23),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(151,23),Ponto(156,18),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(156,18),Ponto(156,13),viewport,pixArray, 0xFFFFFF)
	#DesenhaReta(Ponto(150,23),Ponto(145,25),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(272,19),Ponto(272,70),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(272,70),Ponto(421,70),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(272,53),Ponto(422,53),viewport,pixArray, 0xFFFFFF)
	#DesenhaReta(Ponto(338,52),Ponto(339,70),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(274,71),Ponto(273,98),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(274,71),Ponto(273,98),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(274,71),Ponto(268,98),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(272,98),Ponto(167,98),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(421,28),Ponto(170,28),viewport,pixArray, 0xFFFFFF)
	#DesenhaReta(Ponto(531,480),Ponto(531,446),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(148,23),Ponto(146,22),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(151,23),Ponto(152,22),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(271,53),Ponto(253,53),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(422,28),Ponto(425,34),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(425,34),Ponto(425,45),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(425,45),Ponto(422,53),viewport,pixArray, 0xFFFFFF)

	DesenhaReta(Ponto(422,52),Ponto(425,58),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(425,58),Ponto(425,67),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(425,67),Ponto(421,69),viewport,pixArray, 0xFFFFFF)

	DesenhaReta(Ponto(254,54),Ponto(257,47),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(257,47),Ponto(257,30),viewport,pixArray, 0xFFFFFF)

	DesenhaReta(Ponto(272,100),Ponto(270,112),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(270,112),Ponto(268,121),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(268,121),Ponto(254,124),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(254,124),Ponto(245,124),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(245,124),Ponto(237,128),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(237,128),Ponto(231,134),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(231,134),Ponto(229,143),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(229,143),Ponto(225,152),viewport,pixArray, 0xFFFFFF)
	# dual way
	DesenhaReta(Ponto(225,152),Ponto(216,166),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(216,166),Ponto(203,172),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(203,172),Ponto(186,176),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(186,176),Ponto(168,175),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(168,175),Ponto(154,170),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(154,170),Ponto(145,160),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(145,160),Ponto(143,157),viewport,pixArray, 0xFFFFFF)
	# dual way#1 arrumar
	DesenhaReta(Ponto(225,152),Ponto(211,164),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(211,164),Ponto(199,170),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(199,170),Ponto(189,172),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(189,173),Ponto(171,171),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(171,171),Ponto(157,167),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(157,167),Ponto(150,161),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(150,161),Ponto(147,153),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(147,153),Ponto(147,142),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(147,142),Ponto(150,134),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(150,134),Ponto(164,122),viewport,pixArray, 0xFFFFFF)
	# dual way #2
	DesenhaReta(Ponto(143,157),Ponto(124,156),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(124,156),Ponto(115,160),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(115,160),Ponto(104,169),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(104,169),Ponto(97,184),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(97,184),Ponto(92,204),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(92,204),Ponto(91,258),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(2,258),Ponto(91,258),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(2,258),Ponto(17,192),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(17,192),Ponto(27,160),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(27,160),Ponto(43,138),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(43,138),Ponto(57,128),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(57,128),Ponto(69,107),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(69,107),Ponto(73,91),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(73,91),Ponto(73,78),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(73,78),Ponto(116,63),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(116,63),Ponto(131,50),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(131,51),Ponto(147,26),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(140,38),Ponto(131,40),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(131,40),Ponto(124,40),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(124,40),Ponto(115,46),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(115,46),Ponto(112,64),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(124,40),Ponto(123,34),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(123,34),Ponto(110,28),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(110,28),Ponto(101,28),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(110,28),Ponto(97,30),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(97,30),Ponto(97,33),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(97,33),Ponto(109,38),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(109,38),Ponto(115,46),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(163,122),Ponto(179,116),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(179,116),Ponto(197,115),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(197,115),Ponto(215,120),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(215,120),Ponto(227,128),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(227,128),Ponto(231,136),viewport,pixArray, 0xFFFFFF)
	#gatilho
	DesenhaReta(Ponto(158,127),Ponto(168,131),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(168,131),Ponto(175,131),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(175,131),Ponto(195,118),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(195,118),Ponto(182,140),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(182,140),Ponto(184,153),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(184,153),Ponto(189,159),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(189,159),Ponto(199,162),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(199,162),Ponto(199,165),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(199,165),Ponto(187,164),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(187,164),Ponto(179,158),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(179,158),Ponto(176,151),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(176,151),Ponto(175,145),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(175,145),Ponto(175,132),viewport,pixArray, 0xFFFFFF)
	#end gatilho
	
	DesenhaReta(Ponto(77,249),Ponto(18,249),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(77,249),Ponto(18,249),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(18,249),Ponto(14,242),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(14,242),Ponto(21,207),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(21,207),Ponto(33,180),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(33,180),Ponto(47,154),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(47,154),Ponto(64,140),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(64,140),Ponto(78,133),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(78,133),Ponto(89,133),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(89,133),Ponto(100,161),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(100,161),Ponto(90,172),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(90,172),Ponto(83,202),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(83,202),Ponto(77,248),viewport,pixArray, 0xFFFFFF)
#	DesenhaReta(Ponto(267,71),Ponto(265,111),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(144,157),Ponto(144,133),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(144,133),Ponto(126,131),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(126,131),Ponto(112,125),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(112,125),Ponto(106,113),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(106,113),Ponto(102,103),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(102,103),Ponto(100,75),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(100,75),Ponto(88,78),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(88,78),Ponto(74,78),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(166,31),Ponto(166,99),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(166,31),Ponto(173,28),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(240,28),Ponto(240,98),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(239,36),Ponto(193,36),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(193,36),Ponto(191,34),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(193,36),Ponto(191,34),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(191,34),Ponto(192,32),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(192,32),Ponto(195,30),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(195,30),Ponto(238,30),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(238,54),Ponto(192,54),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(192,54),Ponto(190,56),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(190,56),Ponto(190,63),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(190,63),Ponto(193,63),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(193,63),Ponto(238,63),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(238,86),Ponto(195,86),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(193,63),Ponto(238,63),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(239,86),Ponto(191,86),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(191,86),Ponto(192,93),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(192,93),Ponto(194,96),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(194,96),Ponto(237,96),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(75,79),Ponto(134,156),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(68,108),Ponto(118,158),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(60,124),Ponto(71,136),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(98,162),Ponto(103,168),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(45,138),Ponto(54,147),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(88,180),Ponto(96,188),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(32,154),Ponto(41,163),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(83,205),Ponto(92,214),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(23,173),Ponto(31,181),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(80,231),Ponto(91,241),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(17,192),Ponto(24,199),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(75,249),Ponto(83,258),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(16,203),Ponto(21,208),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(63,250),Ponto(69,257),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(12,215),Ponto(18,221),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(44,249),Ponto(53,258),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(9,230),Ponto(15,235),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(25,250),Ponto(33,258),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(7,245),Ponto(21,258),viewport,pixArray, 0xFFFFFF)

	#bala
	DesenhaReta(Ponto(466 + vai,32),Ponto(466 + vai,58),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(466 + vai,58),Ponto(473 + vai,58),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(473 + vai,58),Ponto(473 + vai,32),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(473 + vai,32),Ponto(466 + vai,32),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(472 + vai,35),Ponto(475 + vai,35),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(475 + vai,35),Ponto(475 + vai,55),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(475 + vai,55),Ponto(473 + vai,55),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(475 + vai,35),Ponto(477 + vai,32),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(477 + vai,32),Ponto(540 + vai,32),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(540 + vai,32),Ponto(550 + vai,34),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(550 + vai,34),Ponto(559 + vai,41),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(559 + vai,41),Ponto(560 + vai,50),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(560 + vai,50),Ponto(552 + vai,55),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(552 + vai,55),Ponto(540 + vai,58),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(540 + vai,58),Ponto(476 + vai,58),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(476 + vai,58),Ponto(475 + vai,55),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(519 + vai,58),Ponto(519 + vai,32),viewport,pixArray, 0xFFFFFF)
	DesenhaReta(Ponto(531 + vai,58),Ponto(531 + vai,32),viewport,pixArray, 0xFFFFFF)

	#quadrante inferior

	for i in range(100,400,7):
		for j in range(800,1100,7):
			DesenhaPonto(Ponto(i,j),viewport,pixArray,0xFFFFFF)
	for i in range(150,350,5):
		for j in range(850,1050,5):
			DesenhaPonto(Ponto(i,j),viewport,pixArray,0xFFFFFF)
	for i in range(200,300,3):
		for j in range(900,1000,3):
			DesenhaPonto(Ponto(i,j),viewport,pixArray,0xFFFFFF)

	#quadrante direito
	DesenhaScanLine(bj1Coordenadas,viewport,pixArray,0xABCDE0)

	listatrasnformada=[MatrizTranslacao(900,-200),MatrizRotacao(30)]
	HexagonoTranslacao=transformada(hexagonoCoordenadas,listatrasnformada)	
	DesenhaPoligono(HexagonoTranslacao,viewport,pixArray,0xABCDE0)
	

	#DesenhaReta(Ponto(425,67),Ponto(422,52),viewport,pixArray, 0xFFFFFF)
	#Modificacoes Personagem
	#meusPontos1 = Primitivas.CirculoBresenham(Ponto(365 ,449), 15, pixArray, 0xFFFFFF)
	#for i in range (0, 9):
		#meusPontos2 = Primitivas.CirculoBresenham(Ponto(365 ,454), i, pixArray, 0xFFFFFF)
		#i+=1
	#for i in range (0, 5):
		#meusPontos2 = Primitivas.CirculoBresenham(Ponto(365 ,454), i, pixArray, 0x000000)
		#i+=1
	#for i in range (0, 2):
		#meusPontos2 = Primitivas.CirculoBresenham(Ponto(365 ,454), i, pixArray, 0xFFFFFF)
		#i+=1

	#trapezioCoordenadas=[Ponto(360,475),Ponto(350,475),Ponto(352,470),Ponto(360,465),Ponto(370,466),Ponto(375,470),Ponto(379,475)]
	#listaTransformada=[MatrizTranslacao(0,100)]
	#NovoTrapezio = transformada(trapezioCoordenadas,listaTransformada)
	#DesenhaPoligono(trapezioCoordenadas,viewport,pixArray,0xFFFFFF)

	#quadradoCoordenadas=[Ponto(462,472),Ponto(361,459),Ponto(368,459),Ponto(363,459)]
	#quadradoCoordenadas=[Ponto(450,200),Ponto(550,200),Ponto(550,300),Ponto(450,300)]
	#listaTransformada=[MatrizTranslacao(0,100)]
	#NovoQuadrado = transformada(quadradoCoordenadas,listaTransformada)
	#DesenhaScanLine(NovoQuadrado,viewport,pixArray,0x664200)

	#lista1 = [MatrizEspelhamento('x')]
	#Primitivas.Poligono(transformada(DesenhaReta,lista1),pixArray,0xFFFFFF)

	# Atualizando a tela do PyGame
	pygame.display.update()

	# Recebimento de input do Pygame:
	waitKey = True
	while waitKey:
		events = pygame.event.get()
		for event in events:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_DOWN:
					passoY += 50
					waitKey = False
				if event.key == pygame.K_UP:
					passoY -= 50
					waitKey = False
				if event.key == pygame.K_LEFT:
					passoX -= 50
					waitKey = False
				if event.key == pygame.K_RIGHT:
					passoX += 50
					waitKey = False	
				if event.key == pygame.K_w:
					zoom -= 50
					waitKey = False	
				if event.key == pygame.K_s:
					zoom += 50
					waitKey = False		
				if event.key == pygame.K_v:
					vai += 50
					waitKey = False	
					

			# Esperando para sair do Pygame	(clicar no X da janela)
			if event.type == pygame.QUIT:					
				pygame.quit()
				waitKey = False
				runProgram = False
			
exit()