# pygameFPS

A simple python package to show your fps in pygame

# Install
```pip install pygameFPS```

# Example
```
import pygame
import pygameFPS as fps
pygame.init()
screen = pygame.display.set_mode([500, 500])
running = True
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Graphing calculator')
clock = pygame.time.Clock()
maxFPS = 144
running = True

while running:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    fps.tick()
    # default rendering
    fps.render(screen)
    # custom args(surface, x, y, size, color)
    fps.render(screen, 50, 50, 24, (255, 255, 255))
    
    screen.fill("black")
    width = 1280
    height = 720
    colour = (255, 255, 255)
    font = pygame.font.SysFont(None, 24)
    img = font.render(f'FPS: {getFPS()}', True, colour)
    screen.blit(img, (20, 20))
    pygame.draw.line(screen, colour, (width / 2, 0), (width / 2, height), 3)
    pygame.draw.line(screen, colour, (0, height / 2), (width, height / 2), 3)

    for line in lines:
        if not line.getCalculated():
            line.calculate()
        x = line.x
        y = line.y
        x2 = line.x2
        y2 = line.y2
        half_width = width / 2
        half_height = height / 2
        pygame.draw.line(screen, colour, (half_width + x, half_height + y), (half_width + x2, half_height + y2), 3)

    pygame.display.flip()

    clock.tick(maxFPS)

pygame.quit()
```
