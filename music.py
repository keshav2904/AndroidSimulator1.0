import pygame, os, time
from mutagen.mp3 import MP3

pygame.init()

song_list, song_n, song_length, a, song_pos = [], 0, 0, 0, 0
music_control = pygame.image.load('music_control.png')

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

pause = True

gameDisplay = pygame.display.set_mode( (display_width, display_height) )
clock = pygame.time.Clock()
    
def music_quit():
    global pause
    pause = True
    pygame.mixer.music.stop()
    import step1
    step1.Android()

def button(x, y, w, h, action=None, msg=''):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        if click[0] ==1 and action != None:
            action()
    if msg != '':
        TextSurf, TextRect = text_objects(msg, medsmallText)
        TextRect.center = ((x+w/2),y+h/2)
        gameDisplay.blit(TextSurf, TextRect)

def button2(x, y, action=None, msg=''):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if msg != '':
        TextSurf, TextRect = text_objects(msg, medsmallText)
        TextRect.center = (x,y)
        gameDisplay.blit(TextSurf, TextRect)
        w = TextRect.midright[0] - TextRect.midleft[0]
        h = TextRect.midbottom[1] - TextRect.midtop[1]
    if x+(w/2) > mouse[0] > x-(w/2) and y+(h/2) > mouse[1] > y-(h/2):
        if click[0] ==1 and action != None:
            action()
def button3(x, y, action=None, msg=''):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if msg != '':
        TextSurf, TextRect = text_objects(msg, medsmallText)
        TextRect.center = (x,y)
        gameDisplay.blit(TextSurf, TextRect)
        w = TextRect.midright[0] - TextRect.midleft[0]
        h = TextRect.midbottom[1] - TextRect.midtop[1]
    if x+(w/2) > mouse[0] > x-(w/2) and y+(h/2) > mouse[1] > y-(h/2):
        if click[0] ==1 and action != None:
            action(mouse)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def previous():
    time.sleep(0.5)
    global song_n, song_list, song_length, a
    a = 0
    pygame.mixer.music.stop()
    if song_n > 0:
        song_n -= 1
    else:
        song_n = len(song_list)-1
    pygame.mixer.music.load('music\\'+song_list[song_n])
    pygame.mixer.music.play(1)
    song = MP3('music\\'+song_list[song_n])
    song_length = song.info.length


def pause_play():
    time.sleep(0.5)
    global pause
    pause = not pause
    if pause == True:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

def nextt():
    time.sleep(0.5)
    global song_n, song_list, song_length, a
    pygame.mixer.music.stop()
    a = 0
    if song_n < len(song_list)-1:
        song_n += 1
    else:
        song_n = 0
    pygame.mixer.music.load('music\\'+song_list[song_n])
    pygame.mixer.music.play(1)
    song = MP3('music\\'+song_list[song_n])
    song_length = song.info.length

    
def play_in_background():
    pygame.mixer.music.unpause()
    global pause
    pause = True
    import step1
    step1.Android()

def jump(mouse):
    global song_length, a, song_pos
    a = int(mouse[0]*song_length*1000/display_width)
    pygame.mixer.music.stop()
    pygame.mixer.music.play(1)
    song_pos = pygame.mixer.music.get_pos()
    pygame.mixer.music.set_pos(mouse[0]*song_length/display_width)

    
def music_intro():
    global song_n, song_list, song_length, a, song_pos
    time.sleep(0.5)
    song_list = os.listdir('music')                                   #list containing names of musicfiles
    a = 0
    if song_list != []:
        pygame.mixer.music.load('music\\'+song_list[song_n])
        pygame.mixer.music.play(1)
        pygame.mixer.music.pause()
        song = MP3('music\\'+song_list[song_n])
        song_length = song.info.length
    textchange = 0
    intro = True
    while intro:
        for event in pygame.event.get():
##            print event
            if event.type == pygame.QUIT:
                music_quit()
        gameDisplay.fill(white)
        if song_list != []:
            song_playing = pygame.mixer.music.get_busy()
            if song_playing == False:
                nextt()

            text_speed = 1
            TextSurf, TextRect = text_objects(song_list[song_n], mediumText)
            TextRect.midleft = ((display_width/2-textchange),(display_height/2)-150)
            gameDisplay.blit(TextSurf, TextRect)
            textchange += text_speed
            if TextRect.midright[0] < -20:
                textchange = -display_width/2
            gameDisplay.blit(music_control, (48.5,500))
            song_pos = pygame.mixer.music.get_pos()
            button3(display_width/2, display_height/2+100, jump, '_________________________________________')
            pygame.draw.circle(gameDisplay, black, (int((song_pos+a)*display_width/song_length/1000),int(display_height/2)+117), 6)
            button(48.5, 500, 135, 65, previous)
            button(183.5, 500, 135, 65, pause_play)
            button(318.5, 500, 135, 65, nextt)
            button2(display_width/2, display_height/2, play_in_background, 'play in background')
        else:
            TextSurf, TextRect = text_objects('No Music Files Found !', mediumText)
            TextRect.center = ((display_width/2),(display_height/2))
            gameDisplay.blit(TextSurf, TextRect)
  
        pygame.display.update()
        clock.tick(120)
