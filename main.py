import time
import pygame

timeElapsed = 0

def SpawnWindow():
    pygame.init()
    pygame.font.init()
    displayInfo = pygame.display.Info()
    screen = pygame.display.set_mode((750, 450), pygame.NOFRAME)
    waitTime = 30
    tick = 0
    
    image = pygame.image.load("assets/screen.png").convert()
    image = pygame.transform.smoothscale(image,(750, 450))
    
    font = pygame.font.SysFont('Arial Rounded MT Bold', 60)
    text = font.render(str(round(waitTime-tick,1)), False, (255, 255, 255))
    for i in range(0,waitTime*(10)):
        pygame.event.get() 
        screen.blit(image, (0,0))
        screen.blit(text, ((750/2)-40,(450/2)+110))
        pygame.display.flip()
        time.sleep(0.1)
        tick+=0.1
    pygame.quit()

while True:
    if timeElapsed % 1200 == 0 and timeElapsed != 0:
        SpawnWindow()
    time.sleep(1)
    timeElapsed+=1
    


