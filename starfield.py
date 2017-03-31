#!/usr/bin/python3
import pygame, sys
from Stars import *
from pygame.locals import *

def initialise_game():
    """Initialise game state"""
    pygame.init()
    width, height = 2000, 2000
    centre = (width / 2, height / 2)
    display = pygame.display.set_mode((width, height))
    return width, height, centre, display

def run(display, FPS, BLACK, width, height, centre):
    """Game loop"""
    num_stars = 500
    stars = [Stars(width, height) for i in range(num_stars)]
    while True:
        display.fill(BLACK)

        for star in stars:
            if star.x > width or star.x < 0:
                stars.remove(star)
                stars.append(Stars(width, height))
            elif star.y > height or star.y < 0:
                stars.remove(star)
                stars.append(Stars(width, height))
            star.draw(display, centre)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

        pygame.display.update()
        pygame.time.Clock().tick(FPS)

def main():
    width, height, centre, display = initialise_game()
    BLACK, FPS = (0, 0, 0), 60
    dimensions = {"width": width, "height": height, "centre": centre}
    run(display, FPS, BLACK, **dimensions)

if __name__ == "__main__":
    main()
