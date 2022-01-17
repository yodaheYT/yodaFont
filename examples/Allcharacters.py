#Import the module
import yodaFontEx
import pygame
display = pygame.display.set_mode((800,600))
fonttable = pygame.image.load("examples\exfont.png")
loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    display.fill((255,255,255))
    yodaFontEx.drawText('ABCDEFGHIJKLMNOPQRSTUVWXYZ', (0, 0), 1, display, fonttable)
    yodaFontEx.drawText('abcdefghijklmnopqrstuvwxyz', (0, 16), 1, display, fonttable)
    yodaFontEx.drawText('1234567890', (0, 32), 1, display, fonttable)
    yodaFontEx.drawText("SPECIALS: _-!.,:;|/'" + '"?><~`#@$%^&*()[]}{', (0, 48), 1, display, fonttable)
    pygame.display.update()
            
pygame.quit()
quit()