import pygame

#เรียกใช้ pygame
pygame.init()

#หัวข้อเกม
pygame.display.set_caption("Help me")

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

#กำหนดตัวแปร
screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
screen.fill(GREEN1)#แล้วเอาตัวแปรมาเรียกใช้ในการตังค่าสี

#วาดรูปทรง
W = 200
pygame.draw.rect(screen,PURPLE,(50,200,W,50))
pygame.draw.rect(screen,PURPLE,(50,350,200,50))
pygame.draw.rect(screen,PURPLE,(50,500,200,50))

#ดึงฟอนต์
fonts = pygame.font.get_fonts()
for font in fonts:#แสดงชื่อฟอนต์ทีละตัว
    print(font)

#ตั้งค่าฟอนต์    
sys_font = pygame.font.SysFont("calibri",50)
sys_font1 = pygame.font.SysFont("papyrus",70)
custom_font = pygame.font.Font("Font/4AnnAroiUltraThin-Regular.ttf",20)


#ตั้งค่าข้อความ
section_text = sys_font1.render("Game to exercise weak wrist muscles",False,GREEN)    
message_text1 = sys_font.render("start",True,BLUE)    
message_text2 = sys_font.render("advice",True,BLUE)    
message_text3 = sys_font.render("out",True,BLUE)    
title_text = custom_font.render("คะแนนหนูตกอ่ะพี่ปันนน ฮือออ",True,BLACK)    

#โหลดภาพ
CAT = pygame.image.load("Image/cat.jpg")

#ปรับขนาดภาพ
CAT = pygame.transform.scale(CAT,(27,30))

#ถ้าเป็น Ture = วนลูป
running = True
while running:#เมื่อเริ่มใช้คำสั่งวนลูปในกิจกรรมเกม
    for event in pygame.event.get():#ถ้ามี event ใน pygame ให้ตรวจสอบ event 
        if event.type == pygame.QUIT:#ถ้า type ของ event เป็นการปิดหน้าจอ
            running = False #ถ้าเป็น False = หยุดวนลูป
    pygame.display.update()
    screen.blit(section_text,(40,50))#เอาข้อความเข้าไปแปะใน screen        
    screen.blit(message_text1,(80,200))#เอาข้อความเข้าไปแปะใน screen        
    screen.blit(message_text2,(80,350))#เอาข้อความเข้าไปแปะใน screen        
    screen.blit(message_text3,(80,500))#เอาข้อความเข้าไปแปะใน screen        
    screen.blit(title_text,(20,655))#เอาข้อความเข้าไปแปะใน screen      
    screen.blit(CAT,(289,655))#เอาข้อความเข้าไปแปะใน screen      
pygame.quit()#ปิดหน้าจอเกม


