import pygame
import yodaFontEx

display = pygame.display.set_mode( ( 800, 600 ) )
clock = pygame.time.Clock()
direction = 0
loop = True
stage = 0
fonttable = pygame.image.load('examples\exfont.png')

while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    display.fill((255,255,255))
    str = "Hello, World!"
    yodaFontEx.drawText(str[0:stage], (10, 10), 1, display, fonttable)
    if stage == 0:
        direction = 0
    elif stage == 13:
        direction = 1
    if direction == 0:
        stage += 1
    elif direction == 1:
        stage -= 1
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()