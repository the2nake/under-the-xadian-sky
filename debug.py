"""
This is the entry point for the game "Under the Xadian Sky", based on the
Netflix series "The Dragon Prince".

Dependencies:
os
pygame 2.0.0.dev8
logzero
datetime
pydraw.py
tilemap.py

Thank you kenney, for making this possible.
"""


"""
Current debug version progress:
 * Intro screen progress: 50%
 * Main game progress: 0%
"""

import os
import pygame
import tilemap
import logzero
import datetime
from pydraw import *
from logzero import logger

# Input box class

now = datetime.datetime.now()
date = now.strftime("%d-%m-%Y")
time = now.strftime("%H:%M:%S")


def checksave(savefile: str):
    savedata = {}
    try:
        file = open(savefile)
    except FileNotFoundError:
        return False, {}
    savelist = file.readlines()
    
    # tilenames is a tuple of names. tilenames[0] returns all of the names, while tilenames[1] returns the avatar names.
    tilesheet, tilenames = tilemap.init()

    try:
        for each in savelist:
            each = each[:len(each) - 1]

        if savelist[0].split("=")[0] == "name" and len(savelist[0].split("=")[1]) > 2 and savelist != [] and savelist[1].split("=")[0] == "avatar" and len(savelist[1].split("=")[1]) > 2 and tilenames[0].__contains__(savelist[1].split("=")[1][:-1]):
            savedata["valid"] = True
            savedata["name"] = savelist[0].split("=")[1][:-1]
            savedata["avatar"] = savelist[1].split("=")[1][:-1]
        else:
            savedata["valid"] = False
            # clear all empty save files

    except IndexError:
        savedata["valid"] = False

    if savedata["valid"]:
        return True, savedata
    else:
        return False, {}


def main():
    '''
    The main function.
    '''

    logzero.logfile("logs/logfile-" + date)

    logger.info("Game started on %s at %s" % (date, time))
    logger.info("--------------------------------------")

    # init
    pygame.init()

    # create tilesheet for the assets/tilesheet.png file
    tilesheet, tilenames = tilemap.init()

    # create window and setup
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Under the Xadian Sky")
    icon = pygame.image.load("icon.png")
    pygame.display.set_icon(icon)
    #backgroundcolour = (128, 255, 128)
    backgroundcolour = (0, 0, 0)
    # speed optimizations
    pygame.event.set_allowed(
        [pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP, pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP])
    # pygame.mouse.set_cursor(*pygame.cursors.tri_left)

    pygame.mouse.set_visible(False)
    cursorimg = pygame.image.load("cursor.png")

    # create keymap
    keymap = {}

    clock = pygame.time.Clock()
    input_boxes = []
    buttons = []

    # save-file

    savelists = [[], [], []]
    savedata = [{}, {}, {}]
    savechosen = -1
    savevalidnums = []

    if checksave("save1.txt")[0]:
        savevalidnums.append(1)
        savedata[0] = checksave("save1.txt")[1]
    else:
        savedata[0] = {"valid": False}

    if checksave("save2.txt")[0]:
        savevalidnums.append(2)
        savedata[1] = checksave("save2.txt")[2]
    else:
        savedata[1] = {"valid": False}

    if checksave("save3.txt")[0]:
        savevalidnums.append(3)
        savedata[2] = checksave("save3.txt")[2]
    else:
        savedata[2] = {"valid": False}

    # save: check validity
    logger.debug("Save file info: %s" % savedata)

    # if not (savedata[0]["valid"] or savedata[1]["valid"] or savedata[2]["valid"]):
    #    input_boxes.append(
    #        InputBox(100, 288, 600, 24, ((168, 61, 61), (150, 50, 50), backgroundcolour), "What is your name? (type here)"))

    # intro init

    introrunning = True
    # there are 2 intro phases: select save, if save is there, open save. If not, ask for name and start a new game
    introphase = "selectsave"
    ticks = 0

    for num in [1, 2, 3]:
        # not savedata[num - 1]["valid"] instead of False for ony loading valid saves
        buttons.append(Button(screen, "Save " + str(num), ("(sw - bw)/2", "(sh - bh)/2 + 48 * %s - 48" % str(num)), (200, 32),
                              ((255, 128, 128), (220, 90, 90), (255, 255, 255)), (None, 24), ("assets/tilesheet.png", savedata[num - 1]["avatar"], False) if savedata[num - 1]["valid"] else ("assets/tilesheet.png", "person-empty", False), False, 4))

        # ("assets/tilesheet.png", savedata[num - 1]["avatar"], False) if savedata[num - 1]["valid"] else ("person-empty", False)

    # mainloop
    while introrunning:
        # poll for events
        for event in pygame.event.get():
            # if the event is quit --> stop
            if event.type == pygame.QUIT:
                introrunning = False

            for i, box in enumerate(input_boxes):  # handle inbut boxes
                temp = box.handle_event(event)
                if temp != 0 and introphase == "inputname":
                    # name = temp
                    # add the name to savedata, write to save file
                    savedata[savechosen - 1]["name"] = temp
                    # write to save file
                    file = open("save%s.txt" % (savechosen), "a+")
                    file.write("name=%s\n" % temp)
                    logger.info("Name is %s" % temp)
                    del input_boxes[i]
                    introrunning = False

            for buttonnum, button in enumerate(buttons):
                out = button.handle_event(event)
                if out == 1:
                    savechosen = buttonnum + 1
                    logger.info("Save chosen: save " + str(savechosen))
                    if introphase == "selectsave":
                        if savedata[savechosen - 1]["valid"]:
                            introphase = "loadsave"
                        else:
                            introphase = "inputname"

                    for i, button in enumerate(buttons):
                        if buttons.__contains__(button):
                            buttons.remove(button)
                        else:
                            del buttons[i]

            if event.type == pygame.KEYDOWN:
                keymap[event.key] = True

            if event.type == pygame.KEYUP:
                keymap[event.key] = False

        for box in input_boxes:
            if ticks > 71:
                box.update()
        # set background (grass green)
        screen.fill(backgroundcolour)
        # screen.fill((0, 0, 0))  # rgb

        # Title, credits, author info, etc
        # if savedata[0]["valid"] or savedata[1]["valid"] or savedata[2]["valid"]:  # savefiles not found
        #    text(screen, "Welcome back", ("(sw - tw)/2", "(sh - th)/3 + 50"),
        #         (231, 169, 132, ticks * 5 - 100), backgroundcolour, (None, 32))
        # else:
        #    text(screen, "Save file not found found", ("(sw - tw)/2", "(sh - th)/3 + 50"),
        #         (255, 89, 89, ticks * 5 - 100), backgroundcolour, (None, 32))

        text(screen, "Under the Xadian Sky", ("(sw - tw)/2", "(sh - th)/3"),
             (231, 169, 132, ticks * 5), backgroundcolour, (None, 56))

        if introphase == "selectsave":
            for button in buttons:
                button.draw()
        elif introphase == "inputname":
            if len(input_boxes) == 0:
                input_boxes.append(InputBox(100, 288, 600, 24, ((
                    168, 61, 61), (150, 50, 50), backgroundcolour), "What is your name? (type here)"))
        elif introphase == "loadsave":
            # this is when you load the save. Process tree below:
            #              If save is valid    /----------------------\
            # wait until button is pressed =\/                         \--> load save, start game, introtrunning = False
            #          If save is not valid  \-- Input name, avatar ---/
            pass

        # draw an icon
        # draw_tile(screen, 'assets/tilesheet.png', (304, 164), tilesheet.get("grass1"))

        # Note: slows down window considerably
        # for _ in range(len(tilesheet.keys())):
        #    draw_tile(screen, 'assets/tilesheet.png', (16 * (_ % 32), 16 *
        #                                               (_ // 32)), tilesheet.get(list(tilesheet.keys())[_]), 0, (False, False))
        # draw_tile(screen, 'assets/tilesheet.png', (0, 0),
        #          tilesheet.get(list(tilesheet.keys())[2]), 1)
        # screen.blit(pygame.image.load("assets/tilesheet.png"), (0, 0))

        # check keys
        # if keymap.get(pygame.K_SPACE):
        #    draw_img(screen, 'solicon.png', 304, 164)

        # draw input boxes
        for box in input_boxes:
            if ticks > 71:
                box.draw(screen)

        # draw cursor
        screen.blit(cursorimg, (pygame.mouse.get_pos()))

        if not introrunning:
            introrunning = False
            fade = pygame.Surface((screen.get_width(), screen.get_height()))
            fade.fill((0, 0, 0))
            for alpha in range(0, 40):
                fade.set_alpha(alpha)
                screen.blit(fade, (0, 0))
                pygame.display.update()
                clock.tick(30)
            # pygame.quit()
        else:
            # Update screen
            pygame.display.update()
            ticks += 1
            clock.tick(30)


main()
