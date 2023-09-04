# pygameFPS

A python package to the show client fps in a pygame project

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
pygame.display.set_caption('Example')
clock = pygame.time.Clock()
maxFPS = 144
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    fps.tick()
    # default rendering
    fps.render(screen)
    # custom args(surface, x, y, size, color)
    fps.render(screen, 50, 50, 24, (255, 255, 255))
    
    screen.fill("black")
    
    pygame.display.flip()

    clock.tick(maxFPS)

pygame.quit()
```
