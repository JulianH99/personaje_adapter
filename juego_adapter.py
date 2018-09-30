"""
@author: JulianH99
@author: David S

"""
import pygame
import sys
import os
from pygame.locals import *

from adapters import CharacterAdapter

#Variables
WIDTH=1000
HEIGHT=640
#Variable boolean
playing = True

#funcion principal
def main_loop():
    pygame.init()
    colorTexto = (125,10,212)
    #texto indicativo
    fuente = pygame.font.SysFont('Arial',30)
    texto = fuente.render("Presione la barra espaciadora"+
                          "para disparar",0,colorTexto)

    ventana = pygame.display.set_mode((WIDTH,HEIGHT))
    #imagen de fondo
    fondo = pygame.image.load(os.path.join('imagenes', 'backg.png')).convert()
    
    #Titulo
    pygame.display.set_caption('Animacion personaje disparando')
    #crear objeto jugador
    character = CharacterAdapter()

    print(dir(character))

    

    #Ciclo del juego
    while True:
        #"dibuja" la imagen de fondo y el texto indicativo
        ventana.blit(fondo,(0,0))
        ventana.blit(texto,(300,100))
        character.paint(ventana)
        if len(character.listaDisparo)>0:
            for x in character.listaDisparo:
                x.dibujar(ventana)
                x.recorrido()
                if x.rect.left< -10:
                    character.listaDisparo.remove(x)
        character.move()
        for evento in pygame.event.get():
            if playing == True:                
            #para cerrar con X
                if evento.type == QUIT:
                    pygame.quit()
                    sys.exit()
                #eventos en que se utilizan teclas     
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == K_LEFT:
                        character.rect.left-=character.velocidad
                    elif evento.key == K_RIGHT:
                        character.rect.right+=character.velocidad
                    elif evento.key==K_SPACE:
                        x,y=character.rect.center
                        character.shoot(x,y)
        pygame.display.update()
#llamada a funcion principal



if __name__ == '__main__':
    main_loop()
