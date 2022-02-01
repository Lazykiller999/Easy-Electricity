import pygame  # imports the required libraries in the program
import random
import sys
import time
from pygame.locals import *  # from a certain module, imports everything

pygame.init()  # initialise pygame
WIDTH, HEIGHT = 1024, 576  # sets the width and height of the program
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # creates the window/display
pygame.display.set_caption("Easy Electricity")  # names the program
logo = pygame.image.load("electric-current.png")  # loads the game logo
pygame.display.set_icon(logo)  # Sets the game logo
BLACK = (0, 0, 0)  # RGB values for black
WHITE = (255, 255, 255)  # RGB value for white
FPS = 60  # set frames per second
autocomplete = True
clicking = False  # Boolean for clicking
base_font = pygame.font.Font(None, 48)  # Sets the base font
GREEN = (0, 255, 0)  # RGB value for green


def draw_window():  # Function for loading the main menu and drawing to the screen
    mm = pygame.image.load("main menu.png")  # loads the image to pygame
    WIN.blit(mm, (0, 0))  # Blits to the screen


def help_window():
    run = True
    clock = pygame.time.Clock()
    help_img = pygame.image.load("help.png")
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
                    settings()
        WIN.blit(help_img, (0, 0))
        pygame.display.update()


def register():
    register_img = pygame.image.load("Register.png")
    WIN.blit(register_img, (0, 0))
    color_active = (255, 0, 0)  # RGB colour for active
    color_passive = WHITE  # RGB colour for passive
    color_u = color_passive  # Sets colour to passive
    color_p = color_passive
    color_c = color_passive
    active_u = False  # Boolean for if the text box is active
    active_p = False
    active_c = False
    Username = ""
    Password = ""
    Code = ""
    cc = "L4ZY"
    accept = False
    run = True
    clock = pygame.time.Clock()
    while run:
        mx, my = pygame.mouse.get_pos()
        user_surface = base_font.render(Username, True, color_u)
        pass_surface = base_font.render(Password, True, color_p)
        code_surface = base_font.render(Code, True, color_c)
        user_rect = pygame.Rect(401.94, 139.34, 218.11, 79.12)
        pass_rect = pygame.Rect(402.94, 283.34, 218.11, 79.12)
        code_rect = pygame.Rect(401.94, 427.34, 218.11, 79.12)
        submit_rect = pygame.Rect(805.94, 497.34, 218.11, 79.12)
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if user_rect.collidepoint((mx, my)):
                    Username = ""
                    active_u = True
                    active_p = False
                    active_c = False
                elif pass_rect.collidepoint((mx, my)):
                    Password = ""
                    active_p = True
                    active_u = False
                    active_c = False
                elif code_rect.collidepoint((mx, my)):
                    Code = ""
                    active_c = True
                    active_u = False
                    active_p = False
                else:
                    active_u = False
                    active_p = False
                    active_c = False
                if submit_rect.collidepoint((mx, my)):
                    if accept:
                        if Username != "" and Password != "" and Username != "Error!" and Password != "Error!":
                            with open("AS.txt", "a+") as f:
                                f.write(f"{Username}:{Password}\n")
                                f.close()
                            sys.exit()

            if event.type == KEYDOWN:  # checks if user is using the keyboard
                if event.key == K_ESCAPE:  # checks if user is pressing the escape button
                    run = False  # setting run to false
                    admin()  # calls the main function
                if active_u:  # condition to check if active is equal to true
                    if event.key == K_BACKSPACE:  # if backspace is pressed
                        Username = Username[:-1]  # delete one character from the string
                    else:
                        Username += event.unicode  # enters the users input into the string
                    if event.key == K_SLASH:  # uses slash to initiate the check
                        Username = Username[:-1]  # deletes the slash from the string
                        active_u = False  # active will be false

                if active_p:  # condition to check if active is equal to true
                    if event.key == K_BACKSPACE:  # if backspace is pressed
                        Password = Password[:-1]  # delete one character from the string
                    else:
                        Password += event.unicode  # enters the users input into the string
                    if event.key == K_SLASH:  # uses slash to initiate the check
                        Password = Password[:-1]  # deletes the slash from the string
                        active_p = False  # active will be false

                if active_c:  # condition to check if active is equal to true
                    if event.key == K_BACKSPACE:  # if backspace is pressed
                        Code = Code[:-1]  # delete one character from the string
                    else:
                        Code += event.unicode  # enters the users input into the string
                    if event.key == K_SLASH:  # uses slash to initiate the check
                        Code = Code[:-1]  # deletes the slash from the string
                        active_c = False  # active will be false
        if not active_u:
            user_length = len(Username)
            if user_length > 10:
                Username = "Error!"

        if not active_p:
            pass_length = len(Password)
            if pass_length > 10:
                Password = "Error!"

        if not active_c:
            if Code == "":
                pass
                accept = False
            else:
                if Code == cc:
                    accept = True
                else:
                    accept = False
                    Code = "Error!"

        if active_u:
            color_u = color_active
        else:
            color_u = color_passive
        if active_p:
            color_p = color_active
        else:
            color_p = color_passive
        if active_c:
            color_c = color_active
        else:
            color_c = color_passive

        WIN.blit(register_img, (0, 0))
        if Username == "Error!":
            WIN.blit(user_surface, (user_rect.x + 65, user_rect.y + 20))
        else:
            WIN.blit(user_surface, (user_rect.x + 10, user_rect.y + 20))
        if Password == "Error!":
            WIN.blit(pass_surface, (pass_rect.x + 65, pass_rect.y + 20))
        else:
            WIN.blit(pass_surface, (pass_rect.x + 10, pass_rect.y + 20))
        if Code == "Error!":
            WIN.blit(code_surface, (code_rect.x + 65, code_rect.y + 20))
        else:
            WIN.blit(code_surface, (code_rect.x + 10, code_rect.y + 20))

        pygame.display.update()


def login():
    run = True
    login_img = pygame.image.load("Login.png")
    WIN.blit(login_img, (0, 0))
    clock = pygame.time.Clock()
    color_active = (255, 0, 0)  # RGB colour for active
    color_passive = WHITE  # RGB colour for passive
    color_u = color_passive  # Sets colour to passive
    color_p = color_passive
    active_u = False  # Boolean for if the text box is active
    active_p = False
    User = ""
    Pass = ""
    while run:
        mx, my = pygame.mouse.get_pos()
        user_surface = base_font.render(User, True, color_u)
        pass_surface = base_font.render(Pass, True, color_p)
        user_rect = pygame.Rect(401.94, 139.34, 218.11, 79.12)
        pass_rect = pygame.Rect(402.94, 283.34, 218.11, 79.12)
        submit_rect = pygame.Rect(401.94, 427.34, 218.11, 79.12)
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if user_rect.collidepoint((mx, my)):
                    User = ""
                    active_u = True
                    active_p = False
                elif pass_rect.collidepoint((mx, my)):
                    Pass = ""
                    active_u = False
                    active_p = True
                else:
                    active_u = False
                    active_p = False
                if submit_rect.collidepoint((mx, my)):
                    line = 0
                    if User != "" and Pass != "":
                        with open("AS.txt", "r") as check:
                            read = check.readlines()
                            max_number = len(read)
                            while True:
                                if line == max_number:
                                    print("Username or password not found")
                                    break
                                else:
                                    usernames = read[line]
                                    split = usernames.split(":")
                                    username = split[0]
                                    temp = split[1]
                                    password = temp.replace("\n", "")
                                    if User == username and Pass == password:
                                        print("Authorised")
                                        break
                                    else:
                                        line = line + 1

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
                    admin()
                if active_u:  # condition to check if active is equal to true
                    if event.key == K_BACKSPACE:  # if backspace is pressed
                        User = User[:-1]  # delete one character from the string
                    else:
                        User += event.unicode  # enters the users input into the string
                    if event.key == K_SLASH:  # uses slash to initiate the check
                        User = User[:-1]  # deletes the slash from the string
                        active_u = False  # active will be false

                if active_p:  # condition to check if active is equal to true
                    if event.key == K_BACKSPACE:  # if backspace is pressed
                        Pass = Pass[:-1]  # delete one character from the string
                    else:
                        Pass += event.unicode  # enters the users input into the string
                    if event.key == K_SLASH:  # uses slash to initiate the check
                        Pass = Pass[:-1]  # deletes the slash from the string
                        active_p = False  # active will be false

        if active_u:
            color_u = color_active
        else:
            color_u = color_passive
        if active_p:
            color_p = color_active
        else:
            color_p = color_passive
        WIN.blit(login_img, (0, 0))
        WIN.blit(user_surface, (user_rect.x + 10, user_rect.y + 20))
        WIN.blit(pass_surface, (pass_rect.x + 10, pass_rect.y + 20))
        pygame.display.update()


def admin():
    clock = pygame.time.Clock()
    run = True
    admin_img = pygame.image.load("Admin panel.png")
    WIN.blit(admin_img, (0, 0))
    while run:
        mx, my = pygame.mouse.get_pos()
        clock.tick(FPS)
        register_rect = pygame.Rect(336, 232, 164, 69)
        login_rect = pygame.Rect(524, 232, 163, 69)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
                    settings()
            if event.type == MOUSEBUTTONDOWN:
                if register_rect.collidepoint((mx, my)):
                    register()
                if login_rect.collidepoint((mx, my)):
                    login()
        pygame.display.update()


def settings():  # Settings function
    global clicking, FPS, autocomplete
    text = f'{FPS}'  # sets the text to FPS
    autocomplete_txt = f"{autocomplete}"  # displays the text
    setting = pygame.image.load("Settings.png")  # loads the image
    WIN.blit(setting, (0, 0))  # blits the image
    running = True  # Boolean for running
    clock = pygame.time.Clock()  # clock function in pygame
    clicking = False  # Boolean for clicking
    color_active = (255, 0, 0)  # RGB colour for active
    color_passive = WHITE  # RGB colour for passive
    color = color_passive  # Sets colour to passive
    active = False  # Boolean for if the text box is active
    while running:  # Running loop
        mx, my = pygame.mouse.get_pos()  # Gets position of the mouse cursor
        clock.tick(FPS)  # Sets the FPS
        text_surface = base_font.render(text, True, color)  # Rendering the font
        toggle_surface = base_font.render(autocomplete_txt, True, WHITE)  # renders the font
        input_rect = pygame.Rect(197.16, 180.97, 147.34, 60.08)  # Creates the rectangle for the input
        toggle_rect = pygame.Rect(436.16, 180.97, 147.34, 60.08)
        help_rect = pygame.Rect(878.38, 0.22, 146.13, 59.59)
        admin_rect = pygame.Rect(879.38, 60.22, 146.13, 59.59)
        for event in pygame.event.get():  # gets the events that occur in pygame
            if event.type == QUIT:  # Checks if exit button is pressed
                pygame.quit()  # Calls the quit function
                sys.exit()  # tells the system to exit the program
            if event.type == MOUSEBUTTONDOWN:  # Checking if user is clicking mouse
                if input_rect.collidepoint((mx, my)):  # Checks if user is on the box
                    text = ""  # clears the string
                    active = True  # sets active to true
                else:
                    active = False  # if not in use sets active to false
                if toggle_rect.collidepoint((mx, my)):
                    if autocomplete:
                        autocomplete_txt = "False"
                        autocomplete = False
                    elif not autocomplete:
                        autocomplete_txt = "True"
                        autocomplete = True
                if help_rect.collidepoint((mx, my)):
                    help_window()
                if admin_rect.collidepoint((mx, my)):
                    admin()
            if event.type == KEYDOWN:  # checks if user is using the keyboard
                if event.key == K_ESCAPE:  # checks if user is pressing the escape button
                    running = False  # setting run to false
                    main()  # calls the main function
                if active:  # condition to check if active is equal to true
                    if event.key == K_BACKSPACE:  # if backspace is pressed
                        text = text[:-1]  # delete one character from the string
                    else:
                        text += event.unicode  # enters the users input into the string
                    if event.key == K_SLASH:  # uses slash to initiate the check
                        text = text[:-1]  # deletes the slash from the string
                        active = False  # active will be false
        if not active:
            if text.isdigit():  # checks if the input is integers
                int_user_text = int(text)  # converts the string into integers
                if int_user_text > 240 or int_user_text < 15:  # makes sure the input is less than 240 and greater
                    # than 15
                    text = "Error"  # if limits are exceeding sets string to error and is shown on screen
                else:
                    FPS = int_user_text  # stores the input into the variable FPS
            else:
                text = "Error"  # if input are not integers, it shows error on the screen

        if active:  # checks if active is true
            color = color_active  # sets the colour to active which is RED
        else:
            color = color_passive  # sets the colour to white which is passive
        WIN.blit(setting, (0, 0))  # blits the settings screen with the new FPS
        WIN.blit(toggle_surface, (toggle_rect.x + 35, toggle_rect.y + 20))
        if text == "Error":
            WIN.blit(text_surface, (
                input_rect.x + 35,
                input_rect.y + 20))  # blits the error to the screen and slightly moves the error message
        else:
            WIN.blit(text_surface, (input_rect.x + 50, input_rect.y + 20))  # blits the fps into the box
        pygame.display.update()  # updates the screen


def level_completed():
    global clicking
    lc_screen = pygame.image.load("level_completed.png")  # loads the image
    WIN.blit(lc_screen, (0, 0))  # blits the image to the screen
    run = True  # boolean to see if loop should be running
    clock = pygame.time.Clock()  # clock function used for fps
    clicking = False  # boolean to see if clicking is active
    while run:  # while loop
        mx, my = pygame.mouse.get_pos()  # get the position of the mouse. gets the x and y coordinates
        next_level = pygame.Rect(374, 439, 306, 109)  # variable to draw a rectangle that is used as a button
        retry_button = pygame.Rect(0, 55, 170, 77)  # variabel to draw a rectangle that is used as a button
        clock.tick(FPS)  # sets the FPS to the imputed FPS
        for event in pygame.event.get():  # gets the events that are occuring
            if event.type == QUIT:  # if user presses the exit button
                pygame.quit()  # pygame quits the application
                sys.exit()  # system closes the window
            if event.type == KEYDOWN:  # checks if user is inputting into the keyboard
                if event.key == K_ESCAPE:  # if escape is pressed
                    run = False  # sets run to false
                    main()  # calls main function
            if event.type == MOUSEBUTTONDOWN:  # checks if user is pressing on their mouse
                if event.button == 1:  # checks if user is pressing the left click
                    clicking = True  # sets the clicking variable to true
            if event.type == MOUSEBUTTONUP:  # checks if user has stopped pressing the mouse
                if event.button == 1:  # checks if it is the left click button
                    clicking = False  # sets clicking to false
        if next_level.collidepoint((mx, my)):  # checks if the mouse coords are colliding with the rectangle
            if clicking:  # checks if clicking is true
                l2()  # loads level 2
        if retry_button.collidepoint((mx, my)):  # checks if the mouse coords are colliding with the rectangle
            if clicking:  # checks if clicking is true
                l1()  # loads up level one
        pygame.display.update()  # updates the screen


def l1():
    global clicking
    lvl1 = pygame.image.load("Circuit_Base.png")  # variable for loading image
    lamp = pygame.image.load("filament 2.0.png")  # variable for loading image
    completed_lamp = pygame.image.load("Circuit_base_with_filament.png")  # variable for loading image
    is_completed = False  # boolean to see if level is completed
    WIN.blit(lvl1, (0, 0))  # loads the image to the screen at coords 0,0
    WIN.blit(lamp, (71, 81))  # loads the lamp image to the coords set
    running = True  # boolean to see if program should be running
    clock = pygame.time.Clock()  # clock function for FPS
    clicking = False  # boolean to see if user is clicking
    while running:  # a loop that is constantly running
        collision_box = pygame.Rect(620.13, 354.13, 65.7, 34.74)  # variable for drawing a rectangle
        mx, my = pygame.mouse.get_pos()  # gets the x and y positions of the mouse/cursor
        clock.tick(FPS)  # sets the FPS to the set variable
        for event in pygame.event.get():  # gets the events that are occuring in the program
            if event.type == QUIT:  # checks if user is trying to quit
                pygame.quit()  # uses the pygame function to stop running
                sys.exit()  # makes the system close the window
            if event.type == KEYDOWN:  # checks if user is pressing on the keyboard
                if event.key == K_ESCAPE:  # checks if user is pressing the escape button
                    running = False  # sets running to false
                    main()  # calls main function
                if event.key == K_n and is_completed == True:  # if user presses on "N" and completed variable is true
                    level_completed()  # loads the level completed function
            if event.type == MOUSEBUTTONDOWN:  # checks if user is pressing on the mouse
                if event.button == 1:  # checks if user is pressing the left click button
                    clicking = True  # sets clicking to true
            if event.type == MOUSEBUTTONUP:  # checks if user has stopped clicking the mouse
                if event.button == 1:  # checks if user has stopped clicking the left mouse button
                    clicking = False  # sets clicking to false
        if clicking and is_completed == False:  # if clicking is false and the level has not been completed
            WIN.blit(lvl1, (0, 0))  # draws the level to the screen
            WIN.blit(lamp, ((mx - 50), (my - 25)))  # draws the component based on the mouse coords
        if collision_box.collidepoint(
                (mx, my)) and clicking == True:  # if user is clicking and mouse coords collide with rectangle
            time.sleep(0.1)  # program stops for 0.1 seconds
            WIN.blit(completed_lamp, (0, 0))  # draws the completed circuit to the screen
            is_completed = True  # sets completed to true
            time.sleep(0)  # makes sure the program doesn't stop
            pygame.display.update()  # updates the screen
            if is_completed and autocomplete:  # checks if level completed is equal to true
                time.sleep(5)  # waits for 5 seconds
                level_completed()  # loads levels completed function
                time.sleep(0)  # sets the wait to 0
        pygame.display.update()  # updates the screen


def l2():
    run = True
    clock = pygame.time.Clock()
    WIN.fill(GREEN)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
                    main()

        pygame.display.update()


def easter_egg():
    global clicking
    clock = pygame.time.Clock()  # function for FPS
    run = True  # boolean to check if function should be running
    W = WIDTH / 2  # variable that divides width by 2
    H = HEIGHT / 2  # variable that divides width by 2
    user_text = 'You found the easter egg!'  # string variable
    base_font = pygame.font.Font(None, 48)  # sets font for the string
    draw_window()
    while run:  # while loop
        R = random.randint(0, 255)  # random number from 0 to 255
        G = random.randint(0, 255)  # random number from 0 to 255
        B = random.randint(0, 255)  # random number from 0 to 255
        color = (R, G, B)  # sets the colour to the random R, G, B values
        mx, my = pygame.mouse.get_pos()  # gets the mouse position for x and y
        clock.tick(FPS)  # sets the FPS
        time.sleep(0.32)  # makes the program stop for 0.32 seconds
        text_surface3 = base_font.render(user_text, True, color)  # sets the text to the colour set by the RGB values
        time.sleep(0)  # stops the program from pausing
        ee_rect = pygame.Rect(H, W, 200, 200)  # variable that defines the rectangle
        for event in pygame.event.get():  # gets the events in pygame
            if event.type == QUIT:  # if user presses the exit button
                pygame.quit()  # calls pygame and tells it to stop
                sys.exit()  # tells system to close application
            if event.type == KEYDOWN:  # checks if user is typing on keyboard
                if event.key == K_ESCAPE:  # checks if user is pressing escape
                    run = False  # sets run to false
                    main()  # calls the main function
        WIN.blit(text_surface3, (ee_rect.x + 15, ee_rect.y + 25))  # blits the text to the surface
        pygame.display.update()  # updates the screen


def main():
    global user_text, clicking
    clock = pygame.time.Clock()  # calls the clock function within pygame
    run = True  # boolean to see if program should be running
    draw_window()  # calls draw_window function which blits the main menu
    clicking = False  # boolean to see if user is clicking
    eeposx = random.randint(10, (HEIGHT - 10))  # gets a random number from 10 to height - 10
    eeposy = random.randint(10, (WIDTH - 10))  # gets a random number from 10 to width - 10
    HIDE_BOX = False  # boolean to see if the box should be hidden
    while run:  # while loop
        mx, my = pygame.mouse.get_pos()  # gets the x and y positions of the mouse
        clock.tick(FPS)  # sets the refresh rate/ FPS
        ee_button = pygame.Rect(eeposx, eeposy, 50, 50)  # creates the square based on the random coords
        lvl1_button = pygame.Rect(385, 409, 254, 122)  # creates a button to start the levels
        setting_button = pygame.Rect(0, 62, 159, 69)  # creates a button to go to the settings menu
        if lvl1_button.collidepoint((mx, my)):  # checks if the mouse is on the rectangle
            if clicking:  # checks if the user is clicking while on the button
                l1()  # loads up level 1
                clicking = False  # sets clicking to false
        if setting_button.collidepoint((mx, my)):  # checks if mouse is on the settings button
            if clicking == True:  # checks if user is also clicking
                settings()  # calls the settings function
                clicking = False  # sets clicking to false
        if ee_button.collidepoint((mx, my)):  # checks if mouse is on the button
            if clicking == True:  # checks if user is also clicking
                easter_egg()  # calls the function
        for event in pygame.event.get():  # gets the events that pygame is outputting
            if event.type == pygame.QUIT:  # checks if user is trying to quit
                pygame.quit()  # tells pygame to stop running
                sys.exit()  # tells system to close the application
            if event.type == KEYDOWN:  # checks if user is typing/pressing on the keyboard
                if event.key == K_ESCAPE:  # checks if the user has pressed escape
                    pygame.quit()  # tells pygame to stop running
                    sys.exit()  # tells system to close the application
                if event.key == K_BACKSLASH and HIDE_BOX == False:  # check if \ is pressed and hide_box is false
                    pygame.draw.rect(WIN, GREEN, ee_button)  # draws the rectangle on the screen with set color
                if event.key == K_z:  # if z is pressed
                    draw_window()  # re-draws the main menu on the window
            if event.type == MOUSEBUTTONDOWN:  # check if user is clicking on the mouse
                if event.button == 1:  # check if user is clicking the left mouse button
                    clicking = True  # sets clicking to true
            elif event.type == MOUSEBUTTONUP:  # check to see if user has stopped clicking
                if event.button == 1:  # checks if user has stopped clicking left mouse button
                    clicking = False  # sets clicking to false
        pygame.display.update()  # updates the display
    pygame.quit()  # tells pygame to stop running


if __name__ == "__main__":  # check to see if the name of file matches the string
    main()  # calls main function if above condition is met
