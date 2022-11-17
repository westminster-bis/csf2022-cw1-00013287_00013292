# import py modules
import pygame
import pygame_menu 
import random
import sys
from typing import Tuple, Any 
from math import isclose

# initialize pygame
pygame.init()
 
# define display size
display_width = 600
display_height = 400
 
# define colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

# define initial difficulty level
difficulty = 0
# define 
 
# Game difficulty is assigned the following values:
#     Beginner = 25
#     Easy = 50
#     Medium = 100
#     Hard = 500

# set pygame display size
win = pygame.display.set_mode((display_width,display_height))
# set pygame window caption
pygame.display.set_caption('Snake Game by 00013287 & 00013292')
# set pygame clock for controlling in-game speed
clock = pygame.time.Clock()
# define player name
player_name = '';
# set default player name to True 
default_player_name = True;

# define a function for generate snake food at random locations
def setup_snake_food():
    new_food_position = [random.randrange(1, (display_width//10))* 10, random.randrange(1, (display_height//10)) * 10]
    return new_food_position # returns new food object coordinates (x, y)

# define a function for generate collision objects
def setup_collision_obj():
    new_collision_obj = [random.randrange(1, (display_width//10))* 10, random.randrange(1, (display_height//10)) * 10]
    return new_collision_obj # returns new collision object coordinates (x, y)

# define a function for set up game difficulty
def set_game_difficulty(selected: Tuple, value: Any):
    # when called this function checks the state of the selected difficulty level and updated difficulty level accordingly
    if(value == 1):
        difficulty = 25
    elif(value == 2):
        difficulty = 50
    elif(value == 3):
        difficulty = 100
    elif(value == 4):
        difficulty = 500
    else:
        difficulty = 25

# define a function for display in-game score
def show_game_score(font, size, game_score):
    game_score_font = pygame.font.SysFont(font, size); # set a font for score
    game_score_surface = game_score_font.render((player_name + "'s Game Score: " + str(game_score)), True, white) # create pygame surface object (a container) for a score
    game_score_rect = game_score_surface.get_rect()
    game_score_rect.midtop = (display_height, 15)
    win.blit(game_score_surface, game_score_rect) # add score object to the game window

# define a function for display generated collision object
def show_collision_obj(collision_obj_position, snake_width, snake_height):
    collision_obj_rect = pygame.Rect(collision_obj_position[0], collision_obj_position[1], snake_width, snake_height) # create interactive rectangle of an collision object
    collision_obj_image = pygame.image.load("./assets/images/red-brick-wall.jpg") # loading red-brick-wall.jpg texture for collision objects from ./assets/images directory
    collision_obj_image_resize = pygame.transform.scale(collision_obj_image, (snake_width, snake_height)) # set size for collision object
    win.blit(collision_obj_image_resize, collision_obj_rect) # add collision object to the game window

# define a function for assinging a name to a player
def set_player_name(name):
    global player_name;
    global default_player_name;
    player_name = name;
    default_player_name = False; # default player name is not displayed if inputted

# define a function for set default name to user
def set_default_player_name():
    global player_name;
    global default_player_name;
    player_name = "Guest";
    default_player_name = False; # default player name is not 'Guest' if inputted

# define a function for display a start screen
def show_start_screen():
    # call a pygame_menu.Menu constructor
    start_menu = pygame_menu.Menu(width=display_width, height=display_height, title='Welcome to Snake Game!', theme=pygame_menu.themes.THEME_BLUE);
    # add text input field for user name
    start_menu.add.text_input("Your Name: ", default="Guest", onchange=set_player_name);
    # add selector field for difficulty
    start_menu.add.selector("Difficulty: ", [("Beginner", 1), ("Easy", 2), ("Medium", 3), ("Hard", 4)], onchange=set_game_difficulty);
    # add divider line
    start_menu.add.label("");
    # add play button
    start_menu.add.button("Play", game_loop);
    # add quit button
    start_menu.add.button("Quit", pygame_menu.events.EXIT);
    # use default player name if player name not set
    if default_player_name:
        set_default_player_name();
    # call a pygame.Menu method for display a menu
    start_menu.mainloop(win)

# define a function for replaying the game
def replay_game(): 
    # call game loop function when clicked on the replay button
    game_loop()

# define a function for showing game over menu
def show_end_screen(game_score):
    # call a pygame_menu.Menu constructor
    end_menu = pygame_menu.Menu(width=display_width, height=display_height, title='Game Over', theme=pygame_menu.themes.THEME_BLUE);
    # add text input field for user name
    end_menu.add.label("Your Score: " + str(game_score));
    # add selector field for difficulty
    end_menu.add.selector("Difficulty: ", [("Beginner", 1), ("Easy", 2), ("Medium", 3), ("Hard", 4)], onchange=set_game_difficulty);
    # add divider line
    end_menu.add.label("");
    # add play button
    end_menu.add.button("Play", replay_game);
    # add quit button
    end_menu.add.button("Quit Game", pygame_menu.events.EXIT);
    # use default player name if player name not set
    if default_player_name:
        set_default_player_name();
    # call a pygame.Menu method for display a menu
    end_menu.mainloop(win)

# define function for playing a music
def play_music():
    # import music from ./assets/music directory
    pygame.mixer.music.load("./assets/music/bg-music.mp3")
    # set music volume statically to 0.3 of full volume
    pygame.mixer.music.set_volume(0.3)
    # set music to play indefinitely (loop=-1), start from 1.0s of the playback (start=1.0) with no fade time (fade_ms=0)
    pygame.mixer.music.play(loops=-1, start=1.0, fade_ms=0)

# define a function for looping the game
def game_loop():
    play_music()
    # define variables for snake position
    x = display_width/2
    y = display_height/2
    snake_position = [x, y]
    # define variables for snake size
    snake_body = [[display_width/2, display_height/2], [(display_width/2)-10, display_height/2], [(display_width/2)-(2*10), display_width/2]]
    snake_width = 20
    snake_height = 20
    snake_speed = 5
    # define variable for snake direction
    snake_direction = "UP"
    new_direction = snake_direction 
    # define variable for exit state & set it to False 
    gameExit = False
    # define variable for score state & set it to 0
    game_score = 0;

    # generate snake food object
    food_position = setup_snake_food()
    # display snake food objects
    show_food = True

    # generate collision object
    collision_obj_position = setup_collision_obj()
    # displaydisplay collision objects
    show_collision = True  

    # define a loop for playing game while user does not exit the game
    while not gameExit:
        # set pygame delay for smoother gaming experience
        pygame.time.delay(10)
        # check if player clicks on exit button
        for event in pygame.event.get():
            # if player quits the game set variable run to False  
            if event.type == pygame.QUIT:
                run = False
        # check user for pressing keys
        keys = pygame.key.get_pressed()
        
        # check user for pressing Escape button
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
            break
        # set variable new_direction state when user pressing Arrow Left button
        if keys[pygame.K_LEFT]:
            new_direction = "LEFT";
        # set variable new_direction state when user pressing Arrow Right button
        if keys[pygame.K_RIGHT]:
            new_direction = "RIGHT";
        # set variable new_direction state when user pressing Arrow Up button
        if keys[pygame.K_UP]:
            new_direction = "UP";
        # set variable new_direction state when user pressing Arrow Down button
        if keys[pygame.K_DOWN]:
            new_direction = "DOWN";
            
        # check user for pressing Arrow Down button
        if snake_direction != "UP" and new_direction == "DOWN":
            snake_direction = new_direction
        # check user for pressing Arrow Up button
        if snake_direction != "DOWN" and new_direction == "UP":
            snake_direction = new_direction
        # check user for pressing Arrow Right button
        if snake_direction != "LEFT" and new_direction == "RIGHT":
            snake_direction = new_direction
        # check user for pressing Arrow Left button
        if snake_direction != "RIGHT" and new_direction == "LEFT":
            snake_direction = new_direction

        # dynamically set snake speed depending on snake direction
        if snake_direction == "UP":
            snake_position[1] -= snake_speed
        if snake_direction == "DOWN":
            snake_position[1] += snake_speed;
        if snake_direction == "LEFT":
            snake_position[0] -= snake_speed;
        if snake_direction == "RIGHT":
            snake_position[0] += snake_speed;

        # increase snake size dynamically after eating snake food
        snake_body.insert(0, list(snake_position));
        if isclose(snake_position[0], food_position[0], abs_tol=5) and isclose(snake_position[1], food_position[1], abs_tol=5):
            game_score += 1;
            show_food = False;
        else:
            snake_body.pop();
        
        # end the game when snake collides with collision objects
        if isclose(snake_position[0], collision_obj_position[0], abs_tol=(snake_width - 10)) and isclose(snake_position[1], collision_obj_position[1], abs_tol=(snake_height - 10)):
            show_end_screen(game_score);

        # set condition for generate & display snake food object after it is eaten
        if not show_food:
            food_position = setup_snake_food();
            show_food = True;
        # set condition for generate & displaydisplay collision object after it is eaten
        if not show_collision:
            collision_obj_position = setup_collision_obj();
            show_collision = True;

        # display additional snake body parts after eating snake food
        win.fill(black);
        for pos in snake_body:
            pygame.draw.rect(win, (255, 255, 255), pygame.Rect(pos[0], pos[1], snake_width/2, snake_height/2));

        # display appel.png image from ./assets/images directory for snake food
        win.blit(pygame.image.load("./assets/images/appel.png").convert(), (food_position[0], food_position[1]))
        # generate collision object
        show_collision_obj(collision_obj_position, snake_width, snake_height);
        # set condition for snake colliding with in-game borders & end game when collided
        if snake_position[0] < 0 or snake_position[0] > (display_width - snake_width/2):
            show_end_screen(game_score);
        if snake_position[1] < 0 or snake_position[1] > (display_height - snake_height/2):
            show_end_screen(game_score);     
        # set in-game font to Verdana
        show_game_score('verdana', 20, game_score)
        # dynamically update pygame display after any change
        pygame.display.update();
        # set game difficulty
        clock.tick(difficulty);
# displaydisplay start screen at the start of the game
show_start_screen()