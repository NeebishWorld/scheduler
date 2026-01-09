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
vocab_number = 0
font = pygame.font.Font(None, 36)  # definition 때문에 살짝 줄임

# -----------------------------
# States
# -----------------------------
STATE_VOCAB = 0
STATE_DEFINITION = 1
STATE_EX = 2
CURRENT = STATE_VOCAB

#------------------------------
# Buttons
#------------------------------
BUTTON_WIDTH = 50
BUTTON_HEIGHT = 50

left_button = pygame.Rect(
    20,
    screen.get_height() // 2 - BUTTON_HEIGHT // 2,
    BUTTON_WIDTH,
    BUTTON_HEIGHT
)

right_button = pygame.Rect(
    screen.get_width() - BUTTON_WIDTH - 20,
    screen.get_height() // 2 - BUTTON_HEIGHT // 2,
    BUTTON_WIDTH,
    BUTTON_HEIGHT
)

# -----------------------------
# Data
# -----------------------------
vocab = ["incantation", "incapacitate"]
definition = ["the words or sounds that are uttered, especially chanted, as part of a magical ritual or spell, or the act of uttering such words or sounds.", "to make someone unable to work or do things normally, or unable to do what they intended to do."]
ex = ["Around the fire, tribal elders chanted an incantation.", "The accident left Adam incapacitated for many months."]

MAX_TEXT_WIDTH = screen.get_width() - 40  # 좌우 여백

# -----------------------------
# Game loop
# -----------------------------
running = True
while running:
    for event in pygame.event.get():
        # QUIT
        if event.type == pygame.QUIT:
            running = False
        # MOUSE CLICK
        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_pos = event.pos

            # BUTTON
            if left_button.collidepoint(mouse_pos):
                # 이전 상태
                if vocab_number <= 0:
                    vocab_number == vocab_number
                else:
                    vocab_number -= 1

            elif right_button.collidepoint(mouse_pos):
                # 다음 상태
                if vocab_number >= len(vocab)-1:
                    vocab_number == vocab_number
                else:
                    vocab_number += 1
            else:
                if CURRENT == STATE_VOCAB:
                    CURRENT = STATE_DEFINITION
                elif CURRENT == STATE_DEFINITION:
                    CURRENT = STATE_EX
                else:
                    CURRENT = STATE_VOCAB

    screen.fill("black")

    pygame.draw.rect(screen, (80, 80, 80), left_button)
    pygame.draw.rect(screen, (80, 80, 80), right_button)

    # 화살표 텍스트
    left_text = font.render("<", True, (255, 255, 255))
    right_text = font.render(">", True, (255, 255, 255))

    screen.blit(left_text, left_text.get_rect(center=left_button.center))
    screen.blit(right_text, right_text.get_rect(center=right_button.center))


    # 어떤 텍스트를 보여줄지 결정
    temp_vocab = vocab[vocab_number]
    temp_def = definition[vocab_number]
    temp_ex = ex[vocab_number]

    if CURRENT == STATE_VOCAB:
        lines = [temp_vocab]
    elif CURRENT == STATE_DEFINITION:
        lines = render_multiline_text(temp_def, font, MAX_TEXT_WIDTH)
    else:
        lines = render_multiline_text(temp_ex, font, MAX_TEXT_WIDTH)

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
