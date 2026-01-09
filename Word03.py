import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((640, 360))
clock = pygame.time.Clock()
running = True

# Creat a font instance (None = default font 48 = size)
font = pygame.font.Font(None, 48)  
# Set the title of this game
pygame.display.set_caption("Vocab Machine!")

CURRENT = 0
STATE_VOCAB = 0
STATE_DEFINITION = 1
STATE_EX = 2

vocab = "incantation"
definition = "the words or sounds that are uttered, especially chanted, as part of a maginal ritual or spell, or the act of uttering such words or sounds."
ex = "Around the fire, tribal elders changed an incatation."

while running:
    # See all events in screen
    for event in pygame.event.get():
        # QUIT
        if event.type == pygame.QUIT:
            running = False
        # MOUSE CLICK
        if event.type == pygame.MOUSEBUTTONDOWN:
            if CURRENT == STATE_VOCAB:
                CURRENT = STATE_DEFINITION
            elif CURRENT == STATE_DEFINITION:
                CURRENT = STATE_EX
            else:
                CURRENT = STATE_VOCAB

    # fill the screen with black color
    screen.fill("black")
    
    if CURRENT == STATE_VOCAB:
        text_surface = font.render(vocab, True, (255, 255, 255))
    elif CURRENT == STATE_DEFINITION:
        text_surface = font.render(definition, True, (255, 255, 255))
    else:
        text_surface = font.render(ex, True, (255, 255, 255))

    # put the text_surface on the screen
    center_x = (screen.get_width() / 2)-(text_surface.get_width() / 2)
    center_y = (screen.get_height() / 2)-(text_surface.get_height() / 2)
    screen.blit(text_surface, (center_x, center_y))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
