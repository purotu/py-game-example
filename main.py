import pygame
from spaceship import Spaceship
pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

GREY = (50, 50, 50)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Python Space Invaders")

clock = pygame.time.Clock()

spaceship = Spaceship(SCREEN_WIDTH, SCREEN_HEIGHT)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

game = True

while game:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game = False

  # Updating
  spaceship_group.update()

  # Drawing 
  screen.fill(GREY)
  spaceship_group.draw(screen)
  spaceship_group.sprite.lasers_group.draw(screen)
    
  pygame.display.update()
  clock.tick(60)



