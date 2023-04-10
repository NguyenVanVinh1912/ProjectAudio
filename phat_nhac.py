import pygame
import sys
# import pyautogui
pygame.init()

clock = pygame.time.Clock()
fps = 60

# Load file nhac.mp3
pygame.mixer.music.load("kk.mp3")

# Phat nhac
pygame.mixer.music.play()

# Khoi tao font va hien thi chuoi thoi gian bai hat
font = pygame.font.SysFont("Arial", 30)
time_elapsed = 0

while True:
    clock.tick(fps)
    
    # Tinh thoi gian da troi qua
    time_elapsed += clock.get_time() / 1000
    
    # Lay thoi gian cua bai hat
    song_time = pygame.mixer.music.get_pos() / 1000
    
    # Tinh thoi gian con lai cua bai hat
    remaining_time = song_time - time_elapsed
    
    # Format thoi gian con lai theo phut:giay
    minutes = int(remaining_time // 60)
    seconds = int(remaining_time % 60)
    time_str = '{:02d}:{:02d}'.format(minutes, seconds)
    
    # Hien thi thoi gian len man hinh
    time_surface = font.render(time_str, True, (255, 255, 255))
    screen.blit(time_surface, (0, 0))
    
    # Kiem tra su kien dong cua so
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()