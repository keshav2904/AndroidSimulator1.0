"""
required files. Install using pip

* Requests

 ```
 pip install requests
 ```

 * BeautifulSoup
 
 ```
 pip install beautifulsoup4
 ```


"""
import pygame, time

pygame.init()

message, number, message_list = '', '', []
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

def message_quit():
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
    
def message_intro():
    time.sleep(0.5)
    global message, number
    intro = True
    pygame.display.set_caption('Messages')
    while intro:
        for event in pygame.event.get():
##            print event
            if event.type == pygame.QUIT:
                message_quit()
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_KP_ENTER, pygame.K_RETURN):
                    take_message()
                if event.key == pygame.K_BACKSPACE:
                    if len(number) > 0:
                        number = number.rstrip(number[len(number)-1])
            if event.type == pygame.KEYUP:
                if event.key in range(48,58) :
                    number+=chr(event.key)
                if event.key in range(256,266) :
                    number+=chr(event.key-208)
        gameDisplay.fill(white)
        TextSurf, TextRect = text_objects("Enter contact number", mediumText)
        TextRect.center = ((display_width/2),(display_height/2-75))
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("you wish to send sms to", mediumText)
        TextRect.center = ((display_width/2),(display_height/2-25))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects(number, mediumText)
        TextRect.center = ((display_width/2),(display_height/2)+50)
        gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(120)

def take_message():
    global message, number, message_list
    intro = True
    pygame.display.set_caption('Messages')
    while intro:
        for event in pygame.event.get():
##            print event
            if event.type == pygame.QUIT:
                message_quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if len(message) > 0:
                        message = message.rstrip(message[len(message)-1])
                if event.key in (pygame.K_KP_ENTER, pygame.K_RETURN):
                    message += '\n'
            if event.type == pygame.KEYUP:
                if event.key in range(32,123) :
                    message+=chr(event.key)
                if event.key in range(256,266) :
                    message+=chr(event.key-208)
        gameDisplay.fill(white)

        message_list = message.split('\n')
        for i in range(len(message_list)):
            TextSurf, TextRect = text_objects(message_list[i], medsmallText)
            TextRect.midleft = (10,35*(i+4))
            gameDisplay.blit(TextSurf, TextRect)


        TextSurf, TextRect = text_objects("Enter your message", mediumText)
        TextRect.center = ((display_width/2),(display_height/2-250))
        gameDisplay.blit(TextSurf, TextRect)

        button('send', display_width-65, display_height-35, 60, 30, green, bright_green, send)

        pygame.display.update()
        clock.tick(120)

def send():
    global number, message, message_list
    message = ''
    for i in range(len(message_list)):
        message += message_list[i]+' '
    status = sendSMS(number, message)
    if status == True:
        message, number, message_list = '', '', []
        while True:

            gameDisplay.fill(white)
        

            TextSurf, TextRect = text_objects("message send", mediumText)
            TextRect.center = ((display_width/2),(display_height/2))
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            clock.tick(120)
            time.sleep(1.0)
            message_quit()
    elif status == 'connection error':
        message, number, message_list = '', '', []
        while True:

            gameDisplay.fill(white)
        

            TextSurf, TextRect = text_objects("connection error occured", mediumText)
            TextRect.center = ((display_width/2),(display_height/2-25))
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            clock.tick(120)
            time.sleep(2.0)
            message_quit()
    elif status == 'number incorrect':
        message, number, message_list = '', '', []
        while True:

            gameDisplay.fill(white)
        

            TextSurf, TextRect = text_objects("number is incorrect", mediumText)
            TextRect.center = ((display_width/2),(display_height/2-25))
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            clock.tick(120)
            time.sleep(2.0)
            message_quit()
    elif status == 'message too long':
        message, number, message_list = '', '', []
        while True:

            gameDisplay.fill(white)
        

            TextSurf, TextRect = text_objects("Message too long", mediumText)
            TextRect.center = ((display_width/2),(display_height/2-25))
            gameDisplay.blit(TextSurf, TextRect)
            TextSurf, TextRect = text_objects("cannot send..!", mediumText)
            TextRect.center = ((display_width/2),(display_height/2+25))
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            clock.tick(120)
            time.sleep(2.0)
            message_quit()
    else:
        message, number, message_list = '', '', []
        while True:

            gameDisplay.fill(white)
        

            TextSurf, TextRect = text_objects("some error occured", mediumText)
            TextRect.center = ((display_width/2),(display_height/2-25))
            gameDisplay.blit(TextSurf, TextRect)
            TextSurf, TextRect = text_objects("cannot send message..!!", mediumText)
            TextRect.center = ((display_width/2),(display_height/2+25))
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            clock.tick(120)
            time.sleep(2.0)
            message_quit()

def sendSMS(to, message):
    import way2sms #this file contains main program
    
##    q=way2sms.sms("7055455188","D9SsA7DZa5FX") # creating object with  my login details for website. Don't change this
    from requests.exceptions import ConnectionError
    try:
        q=way2sms.sms("9557722520","kb115198122")
        return(q.send( str(to), str(message))) # sends sms. Both parameters must be string
    except ConnectionError:
        return 'connection error'
    except:
        return False

##    return(q.msgSentToday()) # msgSentToday returns how many msg are send today
    
    q.logout()


