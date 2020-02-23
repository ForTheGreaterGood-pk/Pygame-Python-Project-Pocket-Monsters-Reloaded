import pygame


def start():
    pygame.init()
    win = pygame.display.set_mode((1162, 559), pygame.SRCALPHA)  # sets the display with setting of per pixel alpha
    pygame.display.set_caption("Pocket Monsters Reloaded")
    bg = pygame.image.load("media/backstart.jpg")
    win.blit(bg, (0, 0))
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(27)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            run = False
