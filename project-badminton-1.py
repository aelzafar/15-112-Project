import pygame
from math import *


pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Telekinesis Goodminton v2.0")
background=pygame.image.load("background.png").convert()

y_men = 500
y_racket = 480

manIMG1 = pygame.image.load("man1.png")
manIMG2 = pygame.image.load("man2.png")

# Getting stick man's length
manLength = manIMG1.get_rect()[2]

racket1IMG = pygame.image.load("racket1.png")
racket2IMG = pygame.image.load("racket2.png")

# Getting rackets' lengths
rack_rad = racket1IMG.get_rect()[3]

# Loading the net and setting coordinates
netIMG = pygame.image.load("net.png")
netLength = netIMG.get_rect()[2]
net_x = 400 - (netLength/2)
net_y = 400


# Class for stickman image
class MAN:
    def __init__( self , x , img ):
        self.img = img
        self.x = x
    def DrawImg( self , x ):
        self.x = x
        screen.blit( self.img , ( x , y_men ) )
    def MoveMan( self , dx ):
        self.DrawImg( self.x + dx )

# Class for Racket image
class RACKET:
    def __init__( self , x  , y , img ):
        self.img = img
        self.x = x
        self.y = y
    def DrawImg( self , x , y ):
        self.x = x
        self.y = y
        screen.blit( self.img , ( x , y ) )
    def Move( self , dx ):
        self.DrawImg( self.x + dx , self.y )
    def Rotate( self ):
        self.y = sqrt( (rack_rad^2) - (self.x^2) )
        self.DrawImg( self.x , self.y )
        self.x += 1
        print str( self.x ) + " and " + str( self.y )


MovementFactor = 0.5

# Initializing the objects of classes for the two stickmen and their rackets
man1 = MAN( 100 , manIMG1 )
man2 = MAN( 800-100-manLength, manIMG2 )
racket1 = RACKET( 100 , y_racket , racket1IMG )
racket2 = RACKET( 800-100-manLength , y_racket , racket2IMG )

done=False
while not done:
    screen.fill([0,0,0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    x1 = x2 = 0

    # Checking for key presses and performing the corresponding actions
    key_pressed = pygame.key.get_pressed()
    if( key_pressed[pygame.K_LEFT] ):
        x2 = -1 * MovementFactor
    if( key_pressed[pygame.K_RIGHT] ):
        x2 = MovementFactor
    key_pressed = pygame.key.get_pressed()
    if( key_pressed[pygame.K_a] ):
        x1 = -1 * MovementFactor
    if( key_pressed[pygame.K_d] ):
        x1 = MovementFactor
    if( key_pressed[pygame.K_SPACE] ):
        pressed_flag = True

    # Drawing the stickmen and rackets based on the coordinates
    screen.blit(background,(0,0))
    man1.MoveMan( x1 )
    man2.MoveMan( x2 )
    racket1.Move( x1 )
    # if pressed_flag is True:
        # racket1.Rotate()
    racket2.Move( x2 )
    screen.blit( netIMG , ( net_x , net_y ) )


    pygame.display.update()




pygame.quit()
