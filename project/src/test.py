# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screenwidth=960
screenheight=540
screen = pygame.display.set_mode((screenwidth, screenheight))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

color = "black"
color1 = "green"
score=0;

font = pygame.font.Font('freesansbold.ttf', 20)
font2 = pygame.font.Font('freesansbold.ttf', 16)
 
# create a text surface object,
# on which text is drawn on it.
text = font.render('(z)Left Leg(1000)', True, "black")
text2 = font.render('(x)Right Leg(2500)', True, "black")
text3 = font.render('(c)Body (10K)', True, "black")
text4 = font.render('(v)Right Arm(50K)', True, "black")
text5 = font.render('(b)Left Arm(100K)', True, "black")
text6 = font.render('(n)Head (1M)', True, "black")
text7 = font2.render('Gear (100) +1/s', True, "black")
text8 = font2.render('WD40 (750) +5/s', True, "black")
text9 = font2.render('CPU (3,000) +25/s', True, "black")
text10 = font2.render('Thingy (20K) +200/s', True, "black")
text11 = font2.render('New Wires (111k) +1K/s', True, "black")
text12 = font2.render('Gold (500K) +4.5K/s', True, "black")
 
# create a rectangular object for the
# text surface object
textRect = text.get_rect()
textRect.center = ( (615/960)*screenwidth , (45/540)*screenheight)
textRect2 = text2.get_rect()
textRect2.center = ( (615/960)*screenwidth , (135/540)*screenheight)
textRect3 = text3.get_rect()
textRect3.center = ( (615/960)*screenwidth , (225/540)*screenheight)
textRect4 = text4.get_rect()
textRect4.center = ( (615/960)*screenwidth , (315/540)*screenheight)
textRect5 = text5.get_rect()
textRect5.center = ( (615/960)*screenwidth , (405/540)*screenheight)
textRect6 = text6.get_rect()
textRect6.center = ( (615/960)*screenwidth , (495/540)*screenheight)
textRect7 = text7.get_rect()
textRect7.center = ( (830/960)*screenwidth , (45/540)*screenheight)
textRect8 = text8.get_rect()
textRect8.center = ( (830/960)*screenwidth , (135/540)*screenheight)
textRect9 = text9.get_rect()
textRect9.center = ( (830/960)*screenwidth , (225/540)*screenheight)
textRect10 = text10.get_rect()
textRect10.center = ( (830/960)*screenwidth , (315/540)*screenheight)
textRect11 = text11.get_rect()
textRect11.center = ( (830/960)*screenwidth , (405/540)*screenheight)
textRect12 = text12.get_rect()
textRect12.center = ( (830/960)*screenwidth , (495/540)*screenheight)



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")


    self = pygame.transform.scale(pygame.image.load('Background.png'), ((screenwidth/2)-5,screenheight))
    screen.blit(self,(0,0))

    self1 = pygame.transform.scale(pygame.image.load('RBackground.jpg'), ((screenwidth/2)-5,screenheight))
    screen.blit(self1,((screenwidth/2)+5,0)) 
    score +=100
    
    if (score>=1000):
        color1="green"
    else:
        color1="gray"
    
    if (score>=2500):
        color2="green"
    else:
        color2="gray"
    if (score>=10000):
        color3="green"
    else:
        color3="gray"
    if (score>=50000):
        color4="green"
    else:
        color4="gray"
    if (score>=100000):
        color5="green"
    else:
        color5="gray"
    if (score>=1000000):
        color6="green"
    else:
        color6="gray"
    if (score>=100):
        color7="green"
    else:
        color7="gray"
    if (score>=750):
        color8="green"
    else:
        color8="gray"
    if (score>=3000):
        color9="green"
    else:
        color9="gray"
    if (score>=20000):
        color10="green"
    else:
        color10="gray"
    if (score>=111111):
        color11="green"
    else:
        color11="gray"
    if (score>500000):
        color12="green"
    else:
        color12="gray"
    
    

    
    # Drawing Rectangle
    pygame.draw.rect(screen, color, pygame.Rect(475, 0, 10, 540))
    pygame.draw.rect(screen, color1, pygame.Rect((525/960)*screenwidth, (10/540)*screenheight, (180/960)*screenwidth, (70/540)*screenheight))
    screen.blit(text, textRect)
    pygame.draw.rect(screen, color2, pygame.Rect((525/960)*screenwidth, (100/540)*screenheight, (180/960)*screenwidth, (70/540)*screenheight))
    screen.blit(text2, textRect2)
    pygame.draw.rect(screen, color3, pygame.Rect((525/960)*screenwidth, (190/540)*screenheight, (180/960)*screenwidth, (70/540)*screenheight))
    screen.blit(text3, textRect3)
    pygame.draw.rect(screen, color4, pygame.Rect((525/960)*screenwidth, (280/540)*screenheight, (180/960)*screenwidth, (70/540)*screenheight))
    screen.blit(text4, textRect4)
    pygame.draw.rect(screen, color5, pygame.Rect((525/960)*screenwidth, (370/540)*screenheight, (180/960)*screenwidth, (70/540)*screenheight))
    screen.blit(text5, textRect5)
    pygame.draw.rect(screen, color6, pygame.Rect((525/960)*screenwidth, (460/540)*screenheight, (180/960)*screenwidth, (70/540)*screenheight))
    screen.blit(text6, textRect6)
    
    pygame.draw.rect(screen, color7, pygame.Rect((740/960)*screenwidth, (10/540)*screenheight, (180/960)*screenwidth, (70/540)*screenheight))
    screen.blit(text7, textRect7)
    pygame.draw.rect(screen, color8, pygame.Rect((740/960)*screenwidth, (100/540)*screenheight, (180/960)*screenwidth, (70/540)*screenheight))
    screen.blit(text8, textRect8)
    pygame.draw.rect(screen, color9, pygame.Rect((740/960)*screenwidth, (190/540)*screenheight, (180/960)*screenwidth, (70/540)*screenheight))
    screen.blit(text9, textRect9)
    pygame.draw.rect(screen, color10, pygame.Rect((740/960)*screenwidth, (280/540)*screenheight, (180/960)*screenwidth, (70/540)*screenheight))
    screen.blit(text10, textRect10)
    pygame.draw.rect(screen, color11, pygame.Rect((740/960)*screenwidth, (370/540)*screenheight, (180/960)*screenwidth, (70/540)*screenheight))
    screen.blit(text11, textRect11)
    pygame.draw.rect(screen, color12, pygame.Rect((740/960)*screenwidth, (460/540)*screenheight, (180/960)*screenwidth, (70/540)*screenheight))
    screen.blit(text12, textRect12)
    
    
    
    
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

text0 = font.render('Score: '+ str(score), True, "black")
textRect0 = text0.get_rect()
textRect0.center = ( (110/960)*screenwidth , (485/540)*screenheight-10)
textp = font2.render('(press space)', True, "black")
textRectp = textp.get_rect()
textRectp.center = ( (110/960)*screenwidth , (485/540)*screenheight+18)

textm = font.render('Multiplier: '+ str(multiplier), True, "black")
textRectm = textm.get_rect()
textRectm.center = ( (365/960)*screenwidth , (485/540)*screenheight)



pygame.draw.rect(screen, "gray", pygame.Rect((1/96)*screenwidth, (44/54)*screenheight, 200, 90))
pygame.draw.rect(screen, "gray", pygame.Rect((265/960)*screenwidth, (44/54)*screenheight, 200, 90))
screen.blit(text0, textRect0)
screen.blit(textp, textRectp)
screen.blit(textm, textRectm)