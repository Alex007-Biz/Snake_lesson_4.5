import pygame
pygame.init()

import time

window_size = (1250, 900)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Олеся, я тебя люблю!!!")
image1 = pygame.image.load("pic.png")
image_rect1 = image1.get_rect()

image2 = pygame.image.load("pic2.png")
image_rect2 = image2.get_rect()


speed = 1


run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()
            image_rect1.x = mouseX - 130
            image_rect1.y = mouseY - 110

    if image_rect1.colliderect(image_rect2):
        print("Произошло!!! Столкновение!!!")
        time.sleep(1)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        image_rect2.x -= speed
    if keys[pygame.K_RIGHT]:
        image_rect2.x += speed
    if keys[pygame.K_UP]:
        image_rect2.y -= speed
    if keys[pygame.K_DOWN]:
        image_rect2.y += speed


    screen.fill((70, 200, 50))
    screen.blit(image1, image_rect1)
    screen.blit(image2, image_rect2)

    pygame.display.flip()



pygame.quit()