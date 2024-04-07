import pygame
pygame.init()
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("тестовый проект1")
image = pygame.image.load("")

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    screen.fill((255, 34, 250))
    pygame.display.flip()



pygame.quit()