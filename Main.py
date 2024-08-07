import pygame

# Initialize Pygame
pygame.init()

# Define colors (RGB)
BLACK = (0, 0, 0)
PURPLE = (153, 153, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (51, 51, 255)
GREEN = (0, 102, 102)
GREEN1 = (153, 255, 153)

# Screen dimensions
SCREEN_W = 1250
SCREEN_H = 720
window_size = (SCREEN_W, SCREEN_H)

# Set up display
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Help me")

# Fill screen with color
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
screen.fill(GREEN1)

# Set fonts
sys_font = pygame.font.SysFont("calibri", 50)
sys_font1 = pygame.font.SysFont("papyrus", 70)
custom_font = pygame.font.Font("Font/4AnnAroiUltraThin-Regular.ttf", 20)

# Button setup
def create_button(rect, color, hover_color, text, font, text_color):
    button = {
        'rect': pygame.Rect(rect),
        'color': color,
        'hover_color': hover_color,
        'text': font.render(text, True, text_color),
        'text_rect': font.render(text, True, text_color).get_rect(center=(rect[0] + rect[2] // 2, rect[1] + rect[3] // 2))
    }
    return button

buttons = [
    create_button((50, 200, 200, 50), PURPLE, WHITE, "start", pygame.font.SysFont("calibri", 50), BLUE),
    create_button((50, 350, 200, 50), PURPLE, WHITE, "advice", pygame.font.SysFont("calibri", 50), BLUE),
    create_button((50, 500, 200, 50), PURPLE, WHITE, "out", pygame.font.SysFont("calibri", 50), BLUE)
]

# Display text setup
section_text = sys_font1.render("Game to exercise weak wrist muscles", False, GREEN)
title_text = custom_font.render("คะแนนหนูตกอ่ะพี่ปันนน ฮือออ", True, BLACK)

# Load and transform image
CAT = pygame.image.load("Image/cat.jpg")
CAT = pygame.transform.scale(CAT, (27, 30))

# Pygame clock initialization
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    clock.tick(60)
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for idx, button in enumerate(buttons):
                if button['rect'].collidepoint(mouse_pos):
                    print(f"Button {idx + 1} clicked!")
    
    for button in buttons:
        if button['rect'].collidepoint(mouse_pos):
            button['color'] = button['hover_color']
        else:
            button['color'] = PURPLE

    window.fill(GREEN1)
    for button in buttons:
        pygame.draw.rect(window, button['color'], button['rect'])
        window.blit(button['text'], button['text_rect'])

    current_time = pygame.time.get_ticks()
    clock_text = sys_font.render(f"Time: {current_time / 1000:.2f} s", True, WHITE)
    clock_text_rect = clock_text.get_rect(topright=(780, 10))
    window.blit(clock_text, clock_text_rect)

    screen.blit(section_text, (40, 50))
    screen.blit(title_text, (20, 655))
    screen.blit(CAT, (289, 655))

    pygame.display.flip()

pygame.quit()
