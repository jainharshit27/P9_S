import pygame

pygame.init()

screen = pygame.display.set_mode((200, 200))

invisible_man = pygame.Rect(0,10,500,500)

change = 10
for i in range(100):
    screen.fill((255,255,255))
    
    if i >= 20:
        pygame.time.delay(1000)
        pygame.quit()
        sys.exit()
    
    pygame.draw.rect(screen, (0,0,0), invisible_man)        
    
    invisible_man.x += change
    invisible_man.y += change
    
    pygame.display.update()
    pygame.time.delay(100)