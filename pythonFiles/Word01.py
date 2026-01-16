# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((640, 360))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    #######################################################################
    # This is where we started!
    pygame.display.set_caption("Vocab Machine!")
    
    # 1. Font instance
    font = pygame.font.Font(None, 48)  # None = default font 48 = size
    # 2. text rendering
    text_surface = font.render("Hello Pygame!", True, (255, 255, 255))

    # put the text_surface on the screen
    center_x = (screen.get_width() / 2)-(text_surface.get_width() / 2)
    center_y = (screen.get_height() / 2)-(text_surface.get_height() / 2)
    screen.blit(text_surface, (center_x, center_y))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
