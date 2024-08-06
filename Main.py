import pygame

#เรียกใช้ pygame
pygame.init()

def check_collision(rect, pos):
    return rect.collidepoint(pos)

#ตั้งค่าสี(RGB)
BLACK = (0,0,0)
PURPLE = (153,153,255)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (51,51,255)
GREEN = (0,102,102)
GREEN1 = (153,255,153)

#ขนาดหน้าจอ
SCREEN_W = 1250
SCREEN_H = 720
window_size = (1250, 720)

#หัวข้อเกม
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Help me")

#กำหนดตัวแปร
screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
screen.fill(GREEN1)#แล้วเอาตัวแปรมาเรียกใช้ในการตังค่าสี

#ตั้งค่าฟอนต์    
sys_font = pygame.font.SysFont("calibri",50)
sys_font1 = pygame.font.SysFont("papyrus",70)
custom_font = pygame.font.Font("Font/4AnnAroiUltraThin-Regular.ttf",20)

#วาดรูปทรง
W = 200
 
button_color = (PURPLE)
button_hover_color = (WHITE)
button_rect = pygame.Rect(50,200,200,50)
button_font = pygame.font.SysFont("calibri", 50)
button_text = button_font.render("start", True, BLUE)
button_text_rect = button_text.get_rect(center=button_rect.center)

button_color1 = (PURPLE)
button_hover_color1 = (WHITE)
button_rect1 = pygame.Rect(50,350,200,50)
button_font1 = pygame.font.SysFont("calibri", 50)
button_text1 = button_font1.render("advice", True, BLUE)
button_text_rect1 = button_text1.get_rect(center=button_rect1.center)

button_color2 = (PURPLE)
button_hover_color2 = (WHITE)
button_rect2 = pygame.Rect(50,500,200,50)
button_font2 = pygame.font.SysFont("calibri", 50)
button_text2 = button_font2.render("out", True, BLUE)
button_text_rect2 = button_text2.get_rect(center=button_rect2.center)

#ดึงฟอนต์
fonts = pygame.font.get_fonts()
for font in fonts:#แสดงชื่อฟอนต์ทีละตัว
    print(font)

#ตั้งค่าข้อความ
section_text = sys_font1.render("Game to exercise weak wrist muscles",False,GREEN)       
title_text = custom_font.render("คะแนนหนูตกอ่ะพี่ปันนน ฮือออ",True,BLACK)    

#โหลดภาพ
CAT = pygame.image.load("Image/cat.jpg")

#ปรับขนาดภาพ
CAT = pygame.transform.scale(CAT,(27,30))

# ฟังก์ชันสำหรับหน้าจอเกม
def game_screen():
    # โค้ดสำหรับหน้าจอเกมของคุณ
    running = True
    while running:
        # ... (โค้ดสำหรับการอัปเดตและแสดงผลหน้าจอเกม)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

# Initialize Pygame clock
clock = pygame.time.Clock()

#ถ้าเป็น Ture = วนลูป
running = True
# Limit the frame rate to 60 FPS เมื่อเริ่มใช้คำสั่งวนลูปในกิจกรรมเกม
while running:
    clock.tick(60)

    # Handle events
    for event in pygame.event.get():#ถ้ามี event ใน pygame ให้ตรวจสอบ event 
        if event.type == pygame.QUIT:#ถ้า type ของ event เป็นการปิดหน้าจอ
            running = False #ถ้าเป็น False = หยุดวนลูป

    mouse_pos = pygame.mouse.get_pos()
    mouse_pos1 = pygame.mouse.get_pos()
    
 
# Handle mouse events
    if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEMOTION:
        mouse_pos = pygame.mouse.get_pos()

    if button_rect.collidepoint(mouse_pos):
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Button 1 clicked!")
    if event.type == pygame.MOUSEMOTION:
         mouse_pos = pygame.mouse.get_pos()
         if button_rect.collidepoint(mouse_pos):
            button_color = button_hover_color
         else:
            button_color = (PURPLE)

    if button_rect1.collidepoint(mouse_pos):
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Button 2 clicked!")
    if event.type == pygame.MOUSEMOTION:
         mouse_pos = pygame.mouse.get_pos()
         if button_rect1.collidepoint(mouse_pos):
            button_color1 = button_hover_color
         else:
            button_color1 = (PURPLE)        

    if button_rect2.collidepoint(mouse_pos):
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Button 3 clicked!")
    if event.type == pygame.MOUSEMOTION:
         mouse_pos = pygame.mouse.get_pos()
         if button_rect2.collidepoint(mouse_pos):
            button_color2 = button_hover_color
         else:
            button_color2 = (PURPLE)              

    window.fill((153,255,153))      
    pygame.draw.rect(window, button_color, button_rect)
    pygame.draw.rect(window, button_color1, button_rect1)
    pygame.draw.rect(window, button_color2, button_rect2)
    window.blit(button_text, button_text_rect)
    window.blit(button_text1, button_text_rect1)
    window.blit(button_text2, button_text_rect2)
    current_time = pygame.time.get_ticks()
    clock_text = button_font.render(f"Time: {current_time/1000:.2f} s", True, (255, 255, 255))
    clock_text_rect = clock_text.get_rect(topright=(780, 10))
    window.blit(clock_text, clock_text_rect)
    
    

    screen.blit(section_text,(40,50))#เอาข้อความเข้าไปแปะใน screen        
    screen.blit(title_text,(20,655))#เอาข้อความเข้าไปแปะใน screen      
    screen.blit(CAT,(289,655))#เอาข้อความเข้าไปแปะใน screen      
    
    pygame.display.flip()
pygame.quit()#ปิดหน้าจอเกม
