import pygame, os, time

note = ''
name = ''

pygame.init()

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

pause = False

gameDisplay = pygame.display.set_mode( (display_width, display_height) )
clock = pygame.time.Clock()

def notes_quit():
    running = False
    import step1
    step1.Android()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg, x, y, w, h, ic, ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        if click[0] ==1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))

    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)


def take_note():
    global note
    running = True
    pygame.display.set_caption('Notes')
    pygame.display.set_icon(pygame.image.load('android_icon.png'))
    
    while running:
        for event in pygame.event.get():
##            print event
            if event.type == pygame.QUIT:
                notes_quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if len(note) > 0:
                        note = note.rstrip(note[len(note)-1])
                if event.key in (pygame.K_KP_ENTER, pygame.K_RETURN):
                    note += '\n'
            if event.type == pygame.KEYUP:
                if event.key in range(32,123) :
                    note+=chr(event.key)
        gameDisplay.fill(white)

        note_list = note.split('\n')
        for i in range(len(note_list)):
            TextSurf, TextRect = text_objects(note_list[i], smallText)
            TextRect.midleft = (10,20*(i+1))
            gameDisplay.blit(TextSurf, TextRect)

        button('save', display_width-65, display_height-35, 60, 30, green, bright_green, save_note)

        pygame.display.update()
        clock.tick(120)

def save_note():
    time.sleep(0.5)
    global name
    running = True
    while running:
        for event in pygame.event.get():
##            print event
            if event.type == pygame.QUIT:
                running = False
                notes_quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if len(name) > 0:
                        name = name.rstrip(name[len(name)-1])
                if event.key in (pygame.K_KP_ENTER, pygame.K_RETURN):
                    save_note_file()
            if event.type == pygame.KEYUP:
                if event.key in range(32,123) :
                    name+=chr(event.key)
        gameDisplay.fill(white)

        TextSurf, TextRect = text_objects("Enter name of file", mediumText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects(name, mediumText)
        TextRect.center = ((display_width/2),(display_height/2)+50)
        gameDisplay.blit(TextSurf, TextRect)
        
        button('save', display_width-65, display_height-35, 60, 30, green, bright_green, save_note_file)
        pygame.display.update()
        clock.tick(120)
        
def save_note_file():
    global name, note
    fw = open(name+'.txt','w')
    fw.write(note)
    fw.close()
    name, note = '', ''
    running = True
    while running:

        gameDisplay.fill(white)
    

        TextSurf, TextRect = text_objects("file saved", mediumText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(120)
        time.sleep(1.0)
        notes_quit()

def view_note():
    time.sleep(0.5)
    global name
    running = True
    pygame.display.set_caption('Notes')
    pygame.display.set_icon(pygame.image.load('android_icon.png'))
    
    while running:
        for event in pygame.event.get():
##            print event
            if event.type == pygame.QUIT:
                notes_quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if len(name) > 0:
                        name = name.rstrip(name[len(name)-1])
                if event.key in (pygame.K_KP_ENTER, pygame.K_RETURN):
                    view_note_file()
            if event.type == pygame.KEYUP:
                if event.key in range(32,123) :
                    name+=chr(event.key)
        gameDisplay.fill(white)

        TextSurf, TextRect = text_objects("Enter name of file", mediumText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects(name, mediumText)
        TextRect.center = ((display_width/2),(display_height/2)+50)
        gameDisplay.blit(TextSurf, TextRect)
        
        button('open', display_width-65, display_height-35, 60, 30, green, bright_green, view_note_file)
        pygame.display.update()
        clock.tick(120)
def view_note_file():
    global name
    try:
        fr = open(name+'.txt','r')
        name = ''
        running = True
        note_text = fr.read()
        note_list = note_text.split('\n')
        while running:
            for event in pygame.event.get():
##                print event
                if event.type == pygame.QUIT:
                    notes_quit()
            gameDisplay.fill(white)
            for i in range(len(note_list)):
                TextSurf, TextRect = text_objects(note_list[i], smallText)
                TextRect.midleft = (10,20*(i+1))
                gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            clock.tick(120)
            
    except IOError:
        running = True
        name = ''
        while running:
            gameDisplay.fill(white)
            TextSurf, TextRect = text_objects("file not found", mediumText)
            TextRect.center = ((display_width/2),(display_height/2))
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            clock.tick(120)
            time.sleep(1.0)
            notes_quit()

    

def notes_intro():
    time.sleep(0.5)
    intro = True
    while intro:
        for event in pygame.event.get():
##            print event
            if event.type == pygame.QUIT:
                notes_quit()
        gameDisplay.fill(white)
        
        button('Take Note', display_width*0.38, display_height*0.2, 150, 100, green, bright_green, take_note)
        button('View Note', display_width*0.38, display_height*0.6, 150, 100, red, bright_red, view_note)
  
        pygame.display.update()
        clock.tick(120)

