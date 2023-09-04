import time
import pygame
fps = []

class Frame():
    frameTime: int = 0
    
    def __init__(self, frameTime: int):
        self.frameTime = frameTime
        
    def getFrameTime(self) -> float:
        return self.frameTime
    
    def getDeltaFramteime(self):
        return time.time() - self.getFrameTime()
    
    def canRemove(self) -> bool:
        return self.getDeltaFramteime() >= 1
    
    def tick(self):
        if self.canRemove():
            fps.remove(self)
                
def getFPS() -> int:
    return len(fps)
                
def tick():
    for frame in fps:
        frame.tick()
    fps.append(Frame(time.time()))
    
def render(surface: pygame.surface, x = 20, y = 20, size = 24, colour = (255, 255, 255)):
    font = pygame.font.SysFont(None, size)
    img = font.render(f'FPS: {getFPS()}', True, colour)
    surface.blit(img, (x, y))