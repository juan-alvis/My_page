from email.mime import image

import pygame
import constantes
class Personaje():
    def __init__(self,x,y,image):
        self.flip = False #Voltear la imagen del personaje
        self.image=image
        self.shape =pygame.Rect(0,0,constantes.width_personaje,constantes.height_personaje)
        self .shape.center = (x,y)

    def dibujar(self, interfaz):
        imagen_flip=pygame.transform.flip(self.image, self.flip, flip_y=False)
        interfaz.blit(imagen_flip, self.shape)#Dibujar personaje con imagen
        #pygame.draw.rect(interfaz, constantes.color_personaje, self.shape, width=1) #Dibujar personaje con cuadrado, widht=1 es para que solo dibuje el borde del cuadrado
    
    def movimiento(self, delta_x, delta_y):
        if delta_x<0:
            self.flip=True
        if delta_x>0:
            self.flip=False
        self.shape.x=self.shape.x + delta_x
        self.shape.y=self.shape.y + delta_y