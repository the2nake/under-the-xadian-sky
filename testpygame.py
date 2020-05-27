import pygame


pygame.init()
screen = pygame.display.set_mode((640, 360))

ticks = 0
clock = pygame.time.Clock()
introrunning = True
backgroundcolor = ((128, 255, 128))
while introrunning:
    for event in pygame.event.get():
        # if the event is quit --> stop
        if event.type == pygame.QUIT:
            introrunning = False

    ticks += 1

    screen.fill(backgroundcolor)
    # pygame.font.Font().render's alpha cannot be set
    welcomescreen = pygame.font.Font(None, 56, flags=pygame.SRCALPHA).render(
        "Under the Xadian Sky", True, pygame.Color(231, 169, 132))
    textsurface = pygame.Surface(
        (welcomescreen.get_width(), welcomescreen.get_height()))
    textsurface.fill(backgroundcolor)
    textsurface.blit(welcomescreen, (0, 0))
    if ticks < 255:
        textsurface.set_alpha(ticks)
    screen.blit(textsurface, (int((screen.get_width() - welcomescreen.get_width()
                                   ) / 2), int((screen.get_height() - welcomescreen.get_height()) / 3)))
    pygame.display.update()
    clock.tick(30)
