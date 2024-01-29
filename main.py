import pygame

# class waz:
#     dlugosc = 1
    # def __init__(self, x, y):

pygame.init()
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
running = True

deltaTime = 0
playerPos = pygame.Vector2(screen.get_width() / 2 - 20, screen.get_height() / 2 -20)
rectPoczatek = pygame.Rect(playerPos.x, playerPos.y, 40, 40)
playerSpeed = 15

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("dark green")

    # RENDER YOUR GAME HERE
    pygame.draw.rect(screen, "blue", rectPoczatek)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        playerPos.y -= playerSpeed
    if keys[pygame.K_s]:
        playerPos.y += playerSpeed
    if keys[pygame.K_a]:
        playerPos.x -= playerSpeed
    if keys[pygame.K_d]:
        playerPos.x += playerSpeed

    rectPoczatek.center = (playerPos.x,playerPos.y)
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(5)  # limits FPS to 60

pygame.quit()