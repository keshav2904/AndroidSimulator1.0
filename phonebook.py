import pygame, os, time, pickle

class Contact:
    def __init__(self):
        self.name = "Contact Empty"
        self.number = ""
    def input_contact(self, name, number):
        self.name = name
        self.number = number
contact = Contact()
name = ''
number = ''

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

def phonebook_quit():
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

def add_contact():
    running = True
    global name, number, contact
    while running:
        for event in pygame.event.get():
##            print event
            if event.type == pygame.QUIT:
                phonebook_quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if len(name) > 0:
                        name = name.rstrip(name[len(name)-1])
                if event.key in (pygame.K_KP_ENTER, pygame.K_RETURN):
                    fr = open("Contacts.dat", "rb")
                    found = 0
                    try:
                        while True:
                            s = pickle.load(fr)
                            if s.name == name:
                                found += 1
                    except EOFError:
                        fr.close()
                    if found == 0:
                        add_contact2()
                    else:
                        running = True
                        while running:
                            gameDisplay.fill(white)
                            TextSurf, TextRect = text_objects("contact already exists", mediumText)
                            TextRect.center = ((display_width/2),(display_height/2))
                            gameDisplay.blit(TextSurf, TextRect)
                            pygame.display.update()
                            clock.tick(120)
                            time.sleep(1.0)
                            name, number = '', ''
                            del contact
                            contact = Contact()
                            phonebook_quit()
                            
            if event.type == pygame.KEYUP:
                if event.key in range(32,123) :
                    name+=chr(event.key)
        gameDisplay.fill(white)
        TextSurf, TextRect = text_objects("Enter contact name", mediumText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects(name, mediumText)
        TextRect.center = ((display_width/2),(display_height/2)+50)
        gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(120)
def add_contact2():
    running = True
    global name, number, contact
    while running:
        for event in pygame.event.get():
##            print event
            if event.type == pygame.QUIT:
                phonebook_quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if len(number) > 0:
                        number = number.rstrip(number[len(number)-1])
                if event.key in (pygame.K_KP_ENTER, pygame.K_RETURN):
                    contact.input_contact(name, number)
                    add_contact3()
            if event.type == pygame.KEYUP:
                if event.key in range(48,58) :
                    number+=chr(event.key)
                if event.key in range(256,266) :
                    number+=chr(event.key-208)
        gameDisplay.fill(white)
        TextSurf, TextRect = text_objects("Enter contact number", mediumText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects(number, mediumText)
        TextRect.center = ((display_width/2),(display_height/2)+50)
        gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(120)
def add_contact3():
    global name, number, contact
    fr = open("Contacts.dat", "a+b")
    pickle.dump(contact, fr)
    fr.close()
    name, number = '', ''
    del contact
    contact = Contact()
    running = True
    while running:

        gameDisplay.fill(white)
    

        TextSurf, TextRect = text_objects("contact saved", mediumText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(120)
        time.sleep(1.0)
        phonebook_quit()

def delete_contact():
    global name, number, contact
    running = True
    while running:
        for event in pygame.event.get():
##            print event
            if event.type == pygame.QUIT:
                phonebook_quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if len(name) > 0:
                        name = name.rstrip(name[len(name)-1])
                if event.key in (pygame.K_KP_ENTER, pygame.K_RETURN):
                    fr = open("Contacts.dat", "rb")
                    fw = open("Temp.dat", "wb")
                    found = 0
                    try:
                        while True:
                            s = pickle.load(fr)
                            if s.name != name:
                                pickle.dump(s,fw)
                            else:
                                found += 1
                    except EOFError:
                        fr.close()
                        fw.close()
                    os.remove("Contacts.dat")
                    os.rename("Temp.dat","Contacts.dat")
                    name, number = '', ''
                    del contact
                    contact = Contact()
                    if found == 0:
                        running = True
                        while running:

                            gameDisplay.fill(white)
                        

                            TextSurf, TextRect = text_objects("no contact found", mediumText)
                            TextRect.center = ((display_width/2),(display_height/2))
                            gameDisplay.blit(TextSurf, TextRect)
                            pygame.display.update()
                            clock.tick(120)
                            time.sleep(1.0)
                            phonebook_quit()
                    else:
                        running = True
                        while running:

                            gameDisplay.fill(white)
                        

                            TextSurf, TextRect = text_objects("contact deleted", mediumText)
                            TextRect.center = ((display_width/2),(display_height/2))
                            gameDisplay.blit(TextSurf, TextRect)
                            pygame.display.update()
                            clock.tick(120)
                            time.sleep(1.0)
                            phonebook_quit()

            if event.type == pygame.KEYUP:
                if event.key in range(32,123) :
                    name+=chr(event.key)
        gameDisplay.fill(white)
        TextSurf, TextRect = text_objects("Enter contact name", mediumText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects(name, mediumText)
        TextRect.center = ((display_width/2),(display_height/2)+50)
        gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(120)

def edit_contact():
    running = True
    global name, number, contact
    while running:
        for event in pygame.event.get():
##            print event
            if event.type == pygame.QUIT:
                phonebook_quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if len(name) > 0:
                        name = name.rstrip(name[len(name)-1])
                if event.key in (pygame.K_KP_ENTER, pygame.K_RETURN):
                    fr = open("Contacts.dat", "rb")
                    fw = open("Temp.dat", "wb")
                    found = 0
                    try:
                        while True:
                            s = pickle.load(fr)
                            if s.name == name:
                                found += 1
                                s = edit_contact2()
                                pickle.dump(s,fw)
                            else:
                                pickle.dump(s,fw)
                    except EOFError:
                        fr.close()
                        fw.close()
                    os.remove("Contacts.dat")
                    os.rename("Temp.dat","Contacts.dat")
                    name, number = '', ''
                    del contact
                    contact = Contact()
                    if found == 0:
                        running = True
                        while running:

                            gameDisplay.fill(white)
                        

                            TextSurf, TextRect = text_objects("no contact found", mediumText)
                            TextRect.center = ((display_width/2),(display_height/2))
                            gameDisplay.blit(TextSurf, TextRect)
                            pygame.display.update()
                            clock.tick(120)
                            time.sleep(1.0)
                            phonebook_quit()
                    else:
                        running = True
                        while running:

                            gameDisplay.fill(white)
                        

                            TextSurf, TextRect = text_objects("contact updated", mediumText)
                            TextRect.center = ((display_width/2),(display_height/2))
                            gameDisplay.blit(TextSurf, TextRect)
                            pygame.display.update()
                            clock.tick(120)
                            time.sleep(1.0)
                            phonebook_quit()
            if event.type == pygame.KEYUP:
                if event.key in range(32,123) :
                    name+=chr(event.key)
        gameDisplay.fill(white)
        TextSurf, TextRect = text_objects("Enter contact name", mediumText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects(name, mediumText)
        TextRect.center = ((display_width/2),(display_height/2)+50)
        gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(120)

def edit_contact2():
    running = True
    global name, number, contact
    while running:
        for event in pygame.event.get():
##            print event
            if event.type == pygame.QUIT:
                phonebook_quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if len(number) > 0:
                        number = number.rstrip(number[len(number)-1])
                if event.key in (pygame.K_KP_ENTER, pygame.K_RETURN):
                    contact.input_contact(name, number)
                    return contact
            if event.type == pygame.KEYUP:
                if event.key in range(48,58) :
                    number+=chr(event.key)
                if event.key in range(256,266) :
                    number+=chr(event.key-208)
        gameDisplay.fill(white)
        TextSurf, TextRect = text_objects("Enter contact number", mediumText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects(number, mediumText)
        TextRect.center = ((display_width/2),(display_height/2)+50)
        gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(120)

def view_contact():
    running = True
    global name, number, contact
    while running:
        for event in pygame.event.get():
##            print event
            if event.type == pygame.QUIT:
                phonebook_quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if len(name) > 0:
                        name = name.rstrip(name[len(name)-1])
                if event.key in (pygame.K_KP_ENTER, pygame.K_RETURN):
                    fr = open("Contacts.dat", "rb")
                    found = 0
                    try:
                        while True:
                            s = pickle.load(fr)
                            if s.name == name:
                                found += 1
                    except EOFError:
                        fr.close()
                    if found == 0:
                        running = True
                        while running:
                            gameDisplay.fill(white)
                            TextSurf, TextRect = text_objects("contact does not exists", mediumText)
                            TextRect.center = ((display_width/2),(display_height/2))
                            gameDisplay.blit(TextSurf, TextRect)
                            pygame.display.update()
                            clock.tick(120)
                            time.sleep(1.0)
                            name, number = '', ''
                            del contact
                            contact = Contact()
                            phonebook_quit()
                    else:
                        fr = open("Contacts.dat", "rb")
                        while True:
                            s = pickle.load(fr)
                            if s.name == name:
                                fr.close()
                                break
                        running = True
                        while running:
                            for event in pygame.event.get():
##                                print event
                                if event.type == pygame.QUIT:
                                    name, number = '', ''
                                    del contact
                                    contact = Contact()
                                    phonebook_quit()
                            gameDisplay.fill(white)
                            TextSurf, TextRect = text_objects("contact name", mediumText)
                            TextRect.center = ((display_width/2),(display_height/2)-150)
                            gameDisplay.blit(TextSurf, TextRect)

                            TextSurf, TextRect = text_objects(s.name, mediumText)
                            TextRect.center = ((display_width/2),(display_height/2)-100)
                            gameDisplay.blit(TextSurf, TextRect)

                            TextSurf, TextRect = text_objects("contact number", mediumText)
                            TextRect.center = ((display_width/2),(display_height/2)+50)
                            gameDisplay.blit(TextSurf, TextRect)

                            TextSurf, TextRect = text_objects(s.number, mediumText)
                            TextRect.center = ((display_width/2),(display_height/2)+100)
                            gameDisplay.blit(TextSurf, TextRect)

                            pygame.display.update()
                            clock.tick(120)
                            
            if event.type == pygame.KEYUP:
                if event.key in range(32,123) :
                    name+=chr(event.key)
        gameDisplay.fill(white)
        TextSurf, TextRect = text_objects("Enter contact name", mediumText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects(name, mediumText)
        TextRect.center = ((display_width/2),(display_height/2)+50)
        gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(120)


    
def phonebook_intro():
    time.sleep(0.5)
    intro = True
    pygame.display.set_caption('Contacts')
    pygame.display.set_icon(pygame.image.load('android_icon.png'))
    while intro:
        for event in pygame.event.get():
##            print event
            if event.type == pygame.QUIT:
                phonebook_quit()
        gameDisplay.fill(white)
        
        button('Add Contact', display_width*0.1, display_height*0.2, 150, 100, green, bright_green, add_contact)
        button('Delete Contact', display_width*0.6, display_height*0.2, 150, 100, red, bright_red, delete_contact)
        button('Edit Contact', display_width*0.1, display_height*0.6, 150, 100, green, bright_green, edit_contact)
        button('View contact', display_width*0.6, display_height*0.6, 150, 100, red, bright_red, view_contact)
  
        pygame.display.update()
        clock.tick(120)

