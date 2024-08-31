import pygame

# เรียกใช้ pygame
pygame.init()

def check_collision(rect, pos):
    return rect.collidepoint(pos)

# ตั้งค่าสี (RGB)
BLACK = (0, 0, 0)
PURPLE = (153, 153, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (51, 51, 255)
GREEN = (0, 102, 102)
GREEN1 = (153, 255, 153)

# ขนาดหน้าจอ
SCREEN_W = 1250
SCREEN_H = 720
window_size = (SCREEN_W, SCREEN_H)

# หัวข้อเกม
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Help me")

# ตั้งค่าฟอนต์    
sys_font = pygame.font.SysFont("calibri", 50)
sys_font1 = pygame.font.SysFont("papyrus", 70)
custom_font = pygame.font.Font("Font/4AnnAroiUltraThin-Regular.ttf", 20)

# วาดปุ่ม
button_color = PURPLE
button_hover_color = WHITE
button_rect = pygame.Rect(50, 200, 200, 50)
button_font = pygame.font.SysFont("calibri", 50)
button_text = button_font.render("start", True, BLUE)
button_text_rect = button_text.get_rect(center=button_rect.center)

button_color1 = PURPLE
button_hover_color1 = WHITE
button_rect1 = pygame.Rect(50, 350, 200, 50)
button_font1 = pygame.font.SysFont("calibri", 50)
button_text1 = button_font1.render("advice", True, BLUE)
button_text_rect1 = button_text1.get_rect(center=button_rect1.center)

button_color2 = PURPLE
button_hover_color2 = WHITE
button_rect2 = pygame.Rect(50, 500, 200, 50)
button_font2 = pygame.font.SysFont("calibri", 50)
button_text2 = button_font2.render("out", True, BLUE)
button_text_rect2 = button_text2.get_rect(center=button_rect2.center)

# ตั้งค่าข้อความ
section_text = sys_font1.render("Game to exercise weak wrist muscles", False, GREEN)       
title_text = custom_font.render("31/8/67", True, BLACK)    

# โหลดภาพ
CAT = pygame.image.load("Image/cat.jpg")
CAT = pygame.transform.scale(CAT, (27, 30))

# ฟังก์ชันสำหรับหน้าจอเกม
def game_screen():
    running = True

    GAME_IMAGE = pygame.image.load('Image/Game.jpg')
    GAME_IMAGE = pygame.transform.scale(GAME_IMAGE, (1250,720))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.blit(GAME_IMAGE, (0, 0))  # ตำแหน่ง (x, y) สำหรับวาดภาพบนหน้าจอ
        
        pygame.display.flip()#ไม่ใช้ pygame.display.flip() หรือ pygame.display.update() เพื่ออัพเดตหน้าจอ การเปลี่ยนแปลงนั้นจะไม่ถูกแสดงผลบนหน้าจอ

# ฟังก์ชันสำหรับหน้าจอคำแนะนำ
def advice_screen():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # เติมสีพื้นหลังหน้าจอคำแนะนำ
        screen.fill(WHITE)

        # เพิ่มข้อความในหน้าจอคำแนะนำ
        advice_text = custom_font.render("How to play", True, BLACK)
        advice1_text = custom_font.render("Use arrow keys to move.left hand.", True, BLACK)
        advice2_text = custom_font.render("left hand.", True, BLACK)
        advice3_text = custom_font.render("1. move your wrist to the left. thech aracter will walk to the left.", True, BLACK)
        advice4_text = custom_font.render("2. move your wri st to the right.the character will walk to the right.", True, BLACK)
        advice5_text = custom_font.render("3. move yonr wrist upward s.the character moves forward.", True, BLACK)
        advice6_text = custom_font.render("4.move your wrist to the sile.the character will waik behind.", True, BLACK)
        advice7_text = custom_font.render("right hand", True, BLACK)
        advice8_text = custom_font.render("1. move your wrist to the side.control the use fo weapons.", True, BLACK)
        advice9_text = custom_font.render("2. move your wrist to the right to control the release of the skin.", True, BLACK)
        advice10_text = custom_font.render("3. move your wrist to the left. controlling weapon changes.", True, BLACK)
        advice11_text = custom_font.render("4.move your wrist to the left.controlling weapon changes.", True, BLACK)

        screen.blit(advice_text, (100, 100))  
        screen.blit(advice1_text, (100, 150))  # ปรับตำแหน่งข้อความตามต้องการ
        screen.blit(advice2_text, (100, 200))
        screen.blit(advice3_text, (100, 250))
        screen.blit(advice4_text, (100, 300))
        screen.blit(advice5_text, (100, 350))
        screen.blit(advice6_text, (100, 400))
        screen.blit(advice7_text, (100, 450))
        screen.blit(advice8_text, (100, 500))
        screen.blit(advice9_text, (100, 550))
        screen.blit(advice10_text, (100, 600))
        screen.blit(advice11_text, (100, 650))

        pygame.display.flip()

# Initialize Pygame clock
clock = pygame.time.Clock()

# ถ้าเป็น True = วนลูป
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_pos = pygame.mouse.get_pos()

    # ตรวจสอบการเคลื่อนที่ของเมาส์และเปลี่ยนสีปุ่ม
    if event.type == pygame.MOUSEMOTION: # MOUSEMOTION เพียงแค่เลื่อนเมาส์ไปบนปุ่ม สีปุ่มก็จะเปลี่ยน
        if button_rect.collidepoint(mouse_pos):
            button_color = button_hover_color
        else:
            button_color = PURPLE

        if button_rect1.collidepoint(mouse_pos):
            button_color1 = button_hover_color1
        else:
            button_color1 = PURPLE

        if button_rect2.collidepoint(mouse_pos):
            button_color2 = button_hover_color2
        else:
            button_color2 = PURPLE

    # ตรวจจับการคลิกปุ่มและการเปลี่ยนหน้าจอ
    if event.type == pygame.MOUSEBUTTONDOWN: # MOUSEBUTTONDOWN ผู้ใช้ต้องคลิก เมื่อเมาส์อยู่บนปุ่ม ข้อความถึงจะถูกแสดง (กรณีคลิกจะได้ทั้งปุ่มซ้ายและขวา)
        if button_rect.collidepoint(mouse_pos):
            print("Button 1 clicked!")
            game_screen()  # เปลี่ยนเป็นหน้าจอเกม

        if button_rect1.collidepoint(mouse_pos):
            print("Button 2 clicked!")
            advice_screen()  # เปลี่ยนเป็นหน้าจอคำแนะนำ

        if button_rect2.collidepoint(mouse_pos):
            print("Button 3 clicked!")
            running = False  # ออกจากเกม

    # วาดปุ่มและองค์ประกอบอื่นๆ บนหน้าจอ
    screen.fill(GREEN1)
    pygame.draw.rect(screen, button_color, button_rect)
    pygame.draw.rect(screen, button_color1, button_rect1)
    pygame.draw.rect(screen, button_color2, button_rect2)
    screen.blit(button_text, button_text_rect)
    screen.blit(button_text1, button_text_rect1)
    screen.blit(button_text2, button_text_rect2)
    screen.blit(section_text, (40, 50))
    screen.blit(title_text, (20, 655))
    screen.blit(CAT, (110, 655))

    pygame.display.flip()

pygame.quit()

