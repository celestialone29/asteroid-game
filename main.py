import pygame  # import pygame library
from constants import *  # import predefined constants

def main():
    pygame.init()  # initialize pygame

    # Create a new GUI window with the specified screen width and height
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Start the game loop
    while True:
        # Check for events, including the quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # exit the game loop and end the program

        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Refresh the display
        pygame.display.flip()

# Ensure main() runs only when this file is executed directly
if __name__ == "__main__":
    main()


