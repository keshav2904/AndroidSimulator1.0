import pygame, datetime, random, cargamecopy, os, webbrowser, time, phonebook, notes, images, music, message

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

chrome_logo = pygame.image.load("chrome_logo.png")
google_bar = pygame.image.load("search_bar_copy.png")
calculator_logo = pygame.image.load("calculator_logo.png")
contacts_logo = pygame.image.load("contacts_logo.png")
notes_logo = pygame.image.load("notes_logo.png")
images_logo = pygame.image.load("images_logo.png")
music_logo = pygame.image.load("music_logo.jpg")
message_logo = pygame.image.load("message_logo.png")


def android_quit():
    pygame.quit()
    quit()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(x, y, w, h, action=None, dw=display_width, dh=display_height, caption='Android', icon=' ', msg='',img=''):
    global gameDisplay
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        if click[0] ==1 and action != None:
            gameDisplay = pygame.display.set_mode( (dw, dh) )
            pygame.display.set_caption(caption)
            pygame.display.set_icon(pygame.image.load(icon))
            action()

    if msg != '':
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ( (x+(w/4)), (y+(h)) )
        gameDisplay.blit(textSurf, textRect)
    if img != '':
        gameDisplay.blit(img,(x,y))

def button2(x, y, w, h, action=None, msg='',img=''):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        if click[0] ==1 and action != None:
            action()
    if msg != '':
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ( (x+(w/4)), (y+(h)) )
        gameDisplay.blit(textSurf, textRect)
    if img != '':
        gameDisplay.blit(img,(x,y))

def run_chrome():
    time.sleep(0.5)
    webbrowser.open("www.google.com")
def calculator():
    os.startfile("calculator")
    time.sleep(5)
                
def Android():
    time.sleep(0.5)
    running = True
    global search
    search = ''
    pygame.display.set_caption('Android')
    pygame.display.set_icon(pygame.image.load('android_icon.png'))
    
    while running:
        dt = datetime.datetime.now()
        day, month, year = dt.day, dt.month, dt.year
        hour, minute, second = dt.hour, dt.minute, dt.second
        for event in pygame.event.get():
##            print event
            if event.type == pygame.QUIT:
                android_quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if len(search) > 0:
                        search = search.rstrip(search[len(search)-1])
                if event.key in (pygame.K_KP_ENTER, pygame.K_RETURN):
                    webbrowser.open("www.google.com/search?source=hp&q="+"+".join(search.split()))
                    search = ''
            if event.type == pygame.KEYUP:
                if event.key in range(32,123) :
                    search+=chr(event.key)
        gameDisplay.fill(white)

        gameDisplay.blit(google_bar,(50,54))
##        TextSurf, TextRect = text_objects('google search: ', smallText)
##        TextRect.center = (150,80)
##        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects(str(search), smallText)
        TextRect.midleft = (150,80)
        gameDisplay.blit(TextSurf, TextRect)
        
        TextSurf, TextRect = text_objects("%02d"%day+'/'+"%02d"%month+'/'+"%04d"%year, mediumText)
        TextRect.center = ((display_width/2),(display_height/2)-150)
        gameDisplay.blit(TextSurf, TextRect)
        
        TextSurf, TextRect = text_objects("%02d"%hour+':'+"%02d"%minute+':'+"%02d"%second, mediumText)
        TextRect.center = ((display_width/2),(display_height/2)-100)
        gameDisplay.blit(TextSurf, TextRect)

        button(display_width*0.2-25, display_height*0.75, 100, 75, cargamecopy.game_intro, cargamecopy.display_width, cargamecopy.display_height, cargamecopy.gameCaption, cargamecopy.gameIcon, msg='Car game', img=cargamecopy.gameLogo)
        button2(display_width*0.4-25, display_height*0.75, 100, 75, run_chrome, msg='Chrome', img=chrome_logo)
        button2(display_width*0.6-25, display_height*0.75, 100, 75, phonebook.phonebook_intro, msg='Contacts', img=contacts_logo)
        button2(display_width*0.8-25, display_height*0.75, 100, 75, calculator, msg='Calculator', img=calculator_logo)
        button2(display_width*0.4-25, display_height*0.55, 100, 75, notes.notes_intro, msg='Notes', img=notes_logo)
        button2(display_width*0.2-25, display_height*0.55, 100, 75, images.image_intro, msg='Images', img=images_logo)
        button2(display_width*0.6-25, display_height*0.55, 100, 75, music.music_intro, msg='Music', img=music_logo)
        button2(display_width*0.8-25, display_height*0.55, 100, 75, message.message_intro, msg='Messages', img=message_logo)
        pygame.display.update()
        clock.tick(120)


Android()









        
