#!/usr/bin/env python3
import pygame, sys, math

# Here's our constants, constants (i.e. things that shouldn't change) are typically written in caps 
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 480, 480
SCREEN_CENTER = SCREEN_WIDTH_CENTER, SCREEN_HEIGHT_CENTER = SCREEN_WIDTH/2, SCREEN_HEIGHT/2
BLACK = (0,0,0) # These are colours defined in RGB codes
WHITE = (255,255,255) 
ORBIT_RADIUS = 100

def compute_planet_center(current_time):

    # We want one rotation every second
    #current_time_milliseconds = current_time % 1000 # This gets us the number of milliseconds after every second, note that the unit of current time is milliseconds
    current_time_milliseconds_as_fraction = current_time/1000.0 # Gotta use a float to get a float
    
    PLANET_X = SCREEN_WIDTH_CENTER + (math.sin(current_time_milliseconds_as_fraction) * ORBIT_RADIUS)
    PLANET_Y = SCREEN_HEIGHT_CENTER + (math.cos(current_time_milliseconds_as_fraction) * ORBIT_RADIUS)

    return PLANET_X, PLANET_Y

def main():
    """
    This is the main function for our game

    """
    pygame.init() # Initialise pygame, always required
    screen = pygame.display.set_mode(SCREEN_SIZE) # Screen is the 'canvas' we will paint our game onto 

    running = True # Variable we use to track if the game is running
    Clock = pygame.time.Clock()

    while running:

        # Get the amount of time that has passed since last loop
        Clock.tick(60)
        current_time = pygame.time.get_ticks()

        # Stop the game if the user clicks the quit button in the corner
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 sys.exit()

        screen.fill(BLACK) # Paint the entire screen black
        pygame.draw.circle(screen, WHITE, SCREEN_CENTER, 15) # Paint a white circle in the middle of the screen.

        planet_center = compute_planet_center(current_time)
        print(current_time)

        pygame.draw.circle(screen, WHITE, planet_center,15)

        pygame.display.flip() # Flip the screen to show it to the user!

""" This functions means that if we execute this file using ./main.py, run the main function"""
if __name__ == "__main__":
    main()