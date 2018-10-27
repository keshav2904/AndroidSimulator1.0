import pygame, time, random, pickle, os, pyttsx3                            #importing some modules

class User:
    def __init__(self):
        self.name = "nobody"
        self.score = 0
try:
    fr = open("User.dat", "rb")
    fr.close()
except IOError:
    fw = open("User.dat", "wb")
    user = User()
    pickle.dump(user, fw)
    fw.close()
    
pygame.init()                                                               #initialising pygame
crash_sound = pygame.mixer.Sound('Crash.wav')
music_list = []
music_n = 0

display_width = 1300                                                        #dimentions of screen
display_height = 700

black = (0,0,0)                                                             #defining some basic colours
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
blue = (0,0,255)
bright_red = (255,0,0)
bright_green = (0,255,0)

car_width =  100                                                            #dimentions of car
car_height = 228

instructions ='''INSTRUCTIONS
1. Use left and right arrow keys to dodge
2. Car is crashed when hit by obstacle or wall'''

gameDisplay = pygame.display.set_mode( (display_width, display_height) )    #setting the game display
gameCaption = 'A bit Racey'                                                 #setting caption
gameIcon = 'caricon.png'
gameLogo = pygame.image.load('game_logo.png')
clock = pygame.time.Clock()                                                 #pygame clock to control fps (game smoothness)

carImg = pygame.image.load('car2.png')                                      #to load image of car

pause = False

largeText = pygame.font.SysFont('Segoe UI',100)
medlargeText = pygame.font.SysFont('Segoe UI',60)
mediumText = pygame.font.SysFont('Segoe UI',40)
medsmallText = pygame.font.SysFont('Segoe UI',30)
smallText = pygame.font.SysFont('Segoe UI',18)

def things_dodged(count):
    text = mediumText.render('Dodged : '+str(count), True, black)
    gameDisplay.blit(text, (0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
    
def car(x,y):
    gameDisplay.blit(carImg,(x,y))

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
##            if action == 'play':
##                game_loop()
##            elif action == 'quit':
##                pygame.quit()
##                quit()
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))

    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)


def crash():
    global user
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)

    TextSurf, TextRect = text_objects('You Crashed', largeText)
    TextRect.center = ((display_width/2),(display_height/3))
    gameDisplay.blit(TextSurf, TextRect)

    TextSurf, TextRect = text_objects('Your Score: '+str(user.score), mediumText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    fr = open("User.dat", "rb")
    fr1 = open("USer1.dat", "rb")
    u = pickle.load(fr)
    u1 = pickle.load(fr1)
    fr.close()
    fr1.close()
    if u1.score >= u.score:
        os.remove("User.dat")
        os.rename("User1.dat", "User.dat")
    else:
        os.remove("User1.dat")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit()

        button('Play Again', display_width*0.2, display_height*0.75, 100, 50, green, bright_green, game_loop)
        button('QUIT', display_width*0.7, display_height*0.75, 100, 50, red, bright_red, game_quit)
        
        pygame.display.update()
        clock.tick(120)

def start():
    global name, user
    try:
        engine = pyttsx3.init()
        engine.say("Hello  "+name)
        engine.runAndWait()    
        user = User()
        user.name = name
        game_loop()
    except:
        user = User()
        user.name = name
        game_loop()
        
def game_quit():
    pygame.mixer.music.stop()
    import step1
    display_width = step1.display_width
    display_height = step1.display_height
    gameDisplay = pygame.display.set_mode( (display_width, display_height) )
    step1.Android()

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False

def paused():

    pygame.mixer.music.pause()
    
    TextSurf, TextRect = text_objects('Paused', largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    text = smallText.render('press c to continue', True, black)
    gameDisplay.blit(text, (display_width*0.75,40))
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                        unpause()
        #gameDisplay.fill(white)

        button('Continue', display_width*0.2, display_height*0.75, 100, 50, green, bright_green, unpause)
        button('QUIT', display_width*0.7, display_height*0.75, 100, 50, red, bright_red, game_quit)
        
        pygame.display.update()
        clock.tick(120)

def game_intro():
    global name, music_list, music_n
    music_list = ['Jazz_In_Paris.wav','Piano_Store.wav','Greek_Dance.wav']      #list containing names of musicfiles
    crash_sound = pygame.mixer.Sound('Crash.wav')                               #crashing sound of car
    pygame.mixer.music.load(music_list[music_n])                                #to load the background music
    intro = True
    name = ''
    fr = open("User.dat", "rb")
    u = pickle.load(fr)
    fr.close()
    while intro:
        for event in pygame.event.get():
##            print event
            if event.type == pygame.QUIT:
                game_quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if len(name) > 0:
                        name = name.rstrip(name[len(name)-1])
                elif event.key in (pygame.K_KP_ENTER, pygame.K_RETURN):
                    start()
            if event.type == pygame.KEYUP:
                if event.key in range(48,123):
                    name+=chr(event.key)
        gameDisplay.fill(white)
        TextSurf, TextRect = text_objects('A Bit Racey', largeText)
        TextRect.center = ((display_width/2),(display_height/3))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects('Enter your name: '+str(name), mediumText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects('INSTRUCTIONS', smallText)
        TextRect.center = ((display_width/2),(display_height/2)+60)
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects('1. Use left and right arrow keys to dodge', smallText)
        TextRect.center = ((display_width/2),(display_height/2)+80)
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects('2. Car is crashed when hit by obstacle or wall', smallText)
        TextRect.center = ((display_width/2),(display_height/2)+100)
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects('High Score: '+str(u.score)+" made by "+str(u.name), mediumText)
        TextRect.center = ((display_width/2),(display_height/2)+300)
        gameDisplay.blit(TextSurf, TextRect)
        
        button('GO', display_width*0.2, display_height*0.75, 100, 50, green, bright_green, start)
        button('QUIT', display_width*0.7, display_height*0.75, 100, 50, red, bright_red, game_quit)
  
        pygame.display.update()
        clock.tick(120)
        
def game_loop():
    global pause, music_n, user
    user.score = 0
    pygame.mixer.music.play(-1)
    
    x = (display_width * 0.44)
    y = (display_height * 0.6)

    x_change = 0

    
    thing_starty = -600
    thing_speed = 3
    thing_width = 120
    thing_height = 120
    thing_startx = random.randrange(0, int(display_width - thing_width))

    dodged = 0

    gameExit = False

    while not gameExit:
        fw = open("User1.dat", "wb")
        pickle.dump(user, fw)
        fw.close()
        for event in pygame.event.get():
##            print event
            if event.type == pygame.QUIT:
                game_quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                if event.key == pygame.K_m:
                    pygame.mixer.music.stop()
                    if music_n < len(music_list)-1:
                        music_n += 1
                    else:
                        music_n = 0
                    pygame.mixer.music.load(music_list[music_n])
                    pygame.mixer.music.play(-1)
                    

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(white)

        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, blue)
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)
        text = smallText.render('press p to pause', True, black)
        gameDisplay.blit(text, (display_width*0.75,0))
        text = smallText.render('press m to change music', True, black)
        gameDisplay.blit(text, (display_width*0.75,20))

        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height*2
            thing_startx = random.randrange(0, int(display_width - thing_width))
            dodged += 1
            user.score+=1
            fw = open("User1.dat", "wb")
            pickle.dump(user, fw)
            fw.close()
            thing_speed += 0.075
            thing_width += 3
            

        if y < thing_starty+thing_height and y + car_height > thing_starty:
            if x + car_width > thing_startx and x < thing_startx + thing_width:
                crash()
            
                
        pygame.display.update()
        clock.tick(120)

##game_intro()
