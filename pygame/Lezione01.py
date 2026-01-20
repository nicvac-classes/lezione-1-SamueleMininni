import pygame

pygame.init()
        
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Test Pygame")

running = True
while running:
    screen.fill((30,30,50))
    pygame.draw.circle(screen, (255,100,100), (320, 240), 30)       
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

