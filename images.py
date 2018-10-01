import pygame, os, time
 

pygame.init()

photo_list, photo_n = [], 0
photo = None

display_width = 500
display_height = 600

black = (0,0,0)                                                             #defining some basic colours
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
blue = (0,0,255)
bright_red = (255,0,0)
bright_green = (0,255,0)

largeText = pygame.font.SysFont('Segoe UI',100)
medlargeText = pygame.font.SysFont('Segoe UI',60)
mediumText = pygame.font.SysFont('Segoe UI',40)
medsmallText = pygame.font.SysFont('Segoe UI',30)
smallText = pygame.font.SysFont('Segoe UI',18)


gameDisplay = pygame.display.set_mode( (display_width, display_height) )
clock = pygame.time.Clock()
    
def image_quit():
    import step1
    step1.Android()

def button(msg, x, y, w, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x :
        textSurf, textRect = text_objects(msg, medlargeText)
        textRect.center = ( x+(w/2), y )
        gameDisplay.blit(textSurf, textRect)
        if click[0] ==1 and action != None:
            action()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def previous():
    time.sleep(0.5)
    global photo_n, photo_list, photo
    if photo_n > 0:
        photo_n -= 1
    else:
        photo_n = len(photo_list)-1
    photo = pygame.image.load('images\\'+photo_list[photo_n])
    size = photo.get_size()
    if size[0] >= size[1]:
        photo = pygame.transform.scale(photo, (480,int(480*size[1]/size[0])))
    else:
        photo = pygame.transform.scale(photo, (int(480*size[0]/size[1]),480))


def nextt():
    time.sleep(0.5)
    global photo_n, photo_list, photo
    if photo_n < len(photo_list)-1:
        photo_n += 1
    else:
        photo_n = 0
    photo = pygame.image.load('images\\'+photo_list[photo_n])
    size = photo.get_size()
    if size[0] >= size[1]:
        photo = pygame.transform.scale(photo, (480,int(480*size[1]/size[0])))
    else:
        photo = pygame.transform.scale(photo, (int(480*size[0]/size[1]),480))


def image_intro():
    global photo_n, photo_list, photo
    time.sleep(0.5)
    photo_list = os.listdir('images')                                 #list containing names of musicfiles
    photo = pygame.image.load('images\\'+photo_list[photo_n])
    intro = True
    while intro:
        for event in pygame.event.get():
##            print event
            if event.type == pygame.QUIT:
                image_quit()
            
        gameDisplay.fill(white)
        size = photo.get_size()
        if size[0] >= size[1]:
            photo = pygame.transform.scale(photo, (480,int(480*size[1]/size[0])))
        else:
            photo = pygame.transform.scale(photo, (int(480*size[0]/size[1]),480))

        gameDisplay.blit(photo, ((display_width-size[0])/2,(display_height-size[1])/2))
        textSurf, textRect = text_objects(photo_list[photo_n], medsmallText)
        textRect.center = ( display_width/2, 20 )
        gameDisplay.blit(textSurf, textRect)
        button('>', display_width-50, display_height/2, 50, nextt)
        button('<', 0, display_height/2, 50, previous)

        pygame.display.update()
        clock.tick(120)
