import pygame

# init pygame instance
pygame.init()
# build the surface
surface = pygame.display.set_mode((800, 400))
# set the game window title
pygame.display.set_caption('Helicopter')
# init the game clock
clock = pygame.time.Clock()

# game over flag
game_over = False

# loop until game is not over
while not game_over:
    # get the pygame event if its not QUIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    pygame.display.update()
    # cap the fps
    clock.tick(60)

# close the instance of pygame
pygame.quit()
quit()