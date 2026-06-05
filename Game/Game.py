import pygame
import constantes
from Personaje  import Personaje

pygame.init()

ventana = pygame.display.set_mode((constantes.height, 
                                   constantes.width))
pygame.display.set_caption("JUEGUITO")

def escalar_img(image,scala):
    w=image.get_width()
    h=image.get_height()
    nueva_imagen=pygame.transform.scale(image,size=(w*scala,h*scala))
    return nueva_imagen

animaciones=[]
for i in range (10):
    img=pygame.image.load (f"D:/codes/computer-science/Game/assets/image ({i}).png")
    img=escalar_img(img, constantes.scala_personaje)
    animaciones.append(img)
#player_image=pygame.image.load ("D:/codes/computer-science/Game/assets/image.png")#Ir a la dirección de la 1ra imagen del personaje
player_image=escalar_img(player_image,constantes.scala_personaje)
player_image=pygame.transform.scale(player_image,(player_image.get_width()*constantes.scala_personaje,player_image.get_height()*constantes.scala_personaje))

jugador = Personaje (x=50, y=50, image=player_image)


mover_arriba=False 
mover_abajo=False
mover_izquierda=False
mover_derecha=False #Estados de movimiento del personaje

#Controlar el frame rate
reloj=pygame.time.Clock()

run=True #This is for dont close the window immediately
while run:
    #Que vaya a 60 frames por segundo
    reloj.tick(constantes.FPS)
    ventana.fill(constantes.color_bg)

    #Calcular el movimiuento del personaje
    delta_x=0
    delta_y=0

    if mover_derecha==True:
        delta_x=constantes.velocidad
    if mover_izquierda==True:
        delta_x=-constantes.velocidad
    if mover_arriba==True:
        delta_y=-constantes.velocidad
    if mover_abajo==True:
        delta_y=constantes.velocidad               
    jugador.dibujar(ventana)
    
    #Mover al jugador
    jugador.movimiento(delta_x, delta_y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_a:
                mover_izquierda=True
            if event.key==pygame.K_d:
                mover_derecha=True
            if event.key==pygame.K_w:
                mover_arriba=True            
            if event.key==pygame.K_s:
                mover_abajo=True

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_a:
                mover_izquierda=False
            if event.key==pygame.K_d:
                mover_derecha=False
            if event.key==pygame.K_w:
                mover_arriba=False            
            if event.key==pygame.K_s:
                mover_abajo=False
    pygame.display.update()
pygame.quit()
