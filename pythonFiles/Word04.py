import pygame

# -----------------------------
# Helper function: multiline text
# -----------------------------
def render_multiline_text(text, font, max_width):
    words = text.split(" ")
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + word + " "
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word + " "

    lines.append(current_line)
    return lines


# -----------------------------
# pygame setup
# -----------------------------
pygame.init()
screen = pygame.display.set_mode((640, 360))
pygame.display.set_caption("Vocab Machine!")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)  # definition 때문에 살짝 줄임

# -----------------------------
# States
# -----------------------------
STATE_VOCAB = 0
STATE_DEFINITION = 1
STATE_EX = 2
CURRENT = STATE_VOCAB

# -----------------------------
# Data
# -----------------------------
vocab = "incantation"
definition = (
    "the words or sounds that are uttered, especially chanted, "
    "as part of a magical ritual or spell, or the act of uttering "
    "such words or sounds."
)
ex = "Around the fire, tribal elders chanted an incantation."

MAX_TEXT_WIDTH = screen.get_width() - 40  # 좌우 여백

# -----------------------------
# Game loop
# -----------------------------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if CURRENT == STATE_VOCAB:
                CURRENT = STATE_DEFINITION
            elif CURRENT == STATE_DEFINITION:
                CURRENT = STATE_EX
            else:
                CURRENT = STATE_VOCAB

    screen.fill("black")

    # 어떤 텍스트를 보여줄지 결정
    if CURRENT == STATE_VOCAB:
        lines = [vocab]
    elif CURRENT == STATE_DEFINITION:
        lines = render_multiline_text(definition, font, MAX_TEXT_WIDTH)
    else:
        lines = render_multiline_text(ex, font, MAX_TEXT_WIDTH)

    # -----------------------------
    # Draw multiline text (centered)
    # -----------------------------
    line_height = font.get_height()
    total_height = line_height * len(lines)
    start_y = (screen.get_height() - total_height) // 2

    for i, line in enumerate(lines):
        surface = font.render(line, True, (255, 255, 255))
        rect = surface.get_rect(
            centerx=screen.get_width() // 2,
            y=start_y + i * line_height
        )
        screen.blit(surface, rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
