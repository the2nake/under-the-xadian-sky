''' 
Pydraw by Vo Thuong
-------------------
A collection of modules that help with drawing in pygame

Dependecies:
pygame 2.0.0.dev8
tilemap.py
'''

import pygame
import tilemap
from pygame import freetype


class Button:
    '''
    A simple button class for pygame

    Arguments:
    text (str): The text to display on the button

    pos, size, colour (tuple): The position, size, and colours of the button, drawn from the top left corner of the button. The pos and size support using sw, sh, bw, bh to stand for the screen and button's height and width. Default colours are (255, 0, 0) when not clicked and (128, 0, 0) when clicked.

    icon (tuple): Formatted like so: (tilesheetname (str), iconname (str, in tilesheet), pos (bool)). pos is left(f) or right(t). If iconname = None or invalid, no icon.
    disabled (bool): If the button is "fake" or not
    borderradius (int): The radius of the border. Default is 0

    Note: the colour tuple is a tuple of 3 tuples, both representing colours. The first is non-clicked, the second is clicked, the  third is text colour.
    '''

    def __init__(self, screen: pygame.Surface, text: str, pos: tuple, size: tuple, colours: tuple = ((255, 0, 0), (128, 0, 0), (0, 0, 0)), font: tuple = (None, 24), icon: tuple = ("assets/tilesheet.png", None, False), disabled=False, borderradius: int = 0):
        sw = screen.get_width()
        sh = screen.get_height()
        bw = size[0]
        bh = size[1]
        if type(pos[0]) == str or type(size[0]) == str:
            self.x = eval(pos[0])
            self.y = eval(pos[1])
        else:
            self.x = pos[0]
            self.y = pos[1]

        if type(size[0]) == str:
            self.w = eval(size[0])
            self.h = eval(size[1])
        else:
            self.w = size[0]
            self.h = size[1]
            
        self.rect = pygame.rect.Rect(
            int(self.x), int(self.y), int(self.w), int(self.h))
        self.screen = screen
        self.font = font
        self.text = text
        self.icon = icon
        self.colours = colours
        if disabled:
            self.drawcolour = colours[1]
        else:
            self.drawcolour = colours[0]
        self.borderradius = borderradius
        self.disabled = disabled

    def handle_event(self, event):
        '''
        Handles the clicking
        '''
        if self.disabled:
            self.drawcolour = self.colours[1]
            return 0
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user click on the button
                if self.rect.collidepoint(event.pos):
                    self.drawcolour = self.colours[1]
                    return 1
            elif event.type == pygame.MOUSEBUTTONUP:
                self.drawcolour = self.colours[0]
                return 0

            return None

    def draw(self):
        '''
        Draws the button
        '''
        #pygame.draw.rect(self.screen, self.drawcolour, self.rect, 0, self.borderradius)
        pygame.draw.rect(self.screen, self.drawcolour, self.rect, 0, self.borderradius)
        if self.icon[1] != None and tilemap.names.__contains__(self.icon[1]):
            padding = self.h/2 - 8
            if self.icon[2]: # right
                draw_tile(self.screen, str(self.icon[0]), (self.x + self.w - 16 - padding, self.y + padding), tilemap.init()[0][self.icon[1]], 0, (False, False))
                text(self.screen, self.text, ("%s + (%s - tw - 16 - 2 * %s)/2" % (str(self.x), str(self.w), str(padding)),
                                              "%s + (%s - th)/2" % (str(self.y), str(self.h))), self.colours[2], self.drawcolour, self.font)
            else: # left
                draw_tile(self.screen, str(self.icon[0]), (self.x + padding, self.y + padding), tilemap.init()[0][self.icon[1]], 0, (False, False))
                text(self.screen, self.text, ("%s + 24 + (%s - tw - 16 - 2 * %s)/2" % (str(self.x), str(self.w), str(padding)),
                                                "%s + (%s - th)/2" % (str(self.y), str(self.h))), self.colours[2], self.drawcolour, self.font)
        else:
            text(self.screen, self.text, ("%s + (%s - tw)/2" % (str(self.x), str(self.w)),
                                          "%s + (%s - th)/2" % (str(self.y), str(self.h))), self.colours[2], self.drawcolour, self.font)


class InputBox:
    '''
    A simple input box class for pygame

    Arguments:

    x, y, w, h (int): pos, size of input box

    colours (tuple): tuple of tuple of colours. ((active), (inactive), (bgcolour))
    '''

    def __init__(self, x: int, y: int, w: int, h: int = 24, colours: tuple = ((168, 70, 70), (150, 50, 50), (0, 0, 0)), deftext=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.keymap = {}
        self.colour = pygame.Color(colours[1][0], colours[1][1], colours[1][2])
        self.colours = colours
        self.text = deftext
        self.deftext = deftext
        self.font = h
        self.txt_surface = pygame.font.Font(
            None, self.font).render(self.text, True, self.colour)
        self.active = False

    def handle_event(self, event):
        '''
        Handles the events related to this input box
        '''
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.colour = pygame.Color(self.colours[0][0], self.colours[0][1], self.colours[0][2]) if self.active else pygame.Color(
                self.colours[1][0], self.colours[0][1], self.colours[1][2])
        if event.type == pygame.KEYDOWN:
            self.keymap[event.key] = True
            if self.active:
                if self.keymap.get(pygame.K_RETURN):
                    if self.text == "":
                        self.deftext = "Input may not be empty"
                        self.text = self.deftext
                        self.active = False
                    else:
                        return self.text
                elif self.keymap.get(pygame.K_BACKSPACE):
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = pygame.font.Font(
                    None, self.font).render(self.text, True, self.colour)
        if event.type == pygame.KEYUP:
            self.keymap[event.key] = False

        return 0

    def update(self):
        '''
        Updates the input box
        '''
        # Resize the box if the text is too long.
        width = max(self.rect.w, self.txt_surface.get_width()+10)
        self.rect.w = width

        if self.active and self.text == self.deftext:
            self.text = ''
            self.txt_surface = pygame.font.Font(
                None, self.font).render(self.text, True, self.colour)
        elif (not self.active) and self.text == '':
            self.text = self.deftext
            self.txt_surface = pygame.font.Font(
                None, self.font).render(self.text, True, self.colour)

        return 0

    def draw(self, screen: pygame.Surface):
        '''
        Draws the input box
        '''
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.colour, self.rect, 2)

        return 0


def text(screen: pygame.Surface, text: str, pos: tuple, colour: tuple, bgcolour: tuple = (0, 0, 0), font: tuple = (None, 24)):
    '''
    Blit text to the screen, with varying levels of transparency.
    ---
    Note: This function supports the use of expressions to evaluate the position for the text. The variables are:
    textw, texth, scrnw, scrnh for text width and height and screen width and height

    Arguments:
    ---
    screen (pygame.Surface): The screen surface. \n
    text (string): text to render \n
    pos (tuple): A tuple describing where on the screen should the text be drawn. \n
    colour, bgcolor (tuple): Format: (r, g, b, (a)), where 0 <= r, g, b, a <= 255. \n
    font (tuple): Format: (path to the font file, fontsize). The pygame freetype module supports TTF, Type1, CFF, OpenType, SFNT, PCF, FNT, BDF, PFR and Type42 fonts. Default is (None, 32)
    '''
    if len(colour) == 4:
        mode = "rgba"
    else:
        mode = "rgb"
    rgbcolour = pygame.Color(colour[0], colour[1], colour[2])

    if font[0] == None:
        textobj = pygame.font.Font(None, font[1])
        textobj = textobj.render(text, True, rgbcolour)
        tw = textobj.get_width()
        th = textobj.get_height()
    else:
        textobj = freetype.Font(font[0], font[1])
        textobj = textobj.render(text, rgbcolour)
        tw = textobj[0].get_width()
        th = textobj[0].get_height()


    sw = screen.get_width()
    sh = screen.get_height()
    rendering_surface = pygame.Surface((tw, th))
    try:
        rendering_surface.fill(pygame.Color(
            bgcolour[0], bgcolour[1], bgcolour[2]))
    except IndexError:
        return None
    
    if font[0] == None:
        rendering_surface.blit(textobj, (0, 0))
    else:
        rendering_surface.blit(textobj[0], (0, 0))

    # pygame.font.Font().render's alpha cannot be set, use surface alpha
    if mode == "rgba":
        if 0 <= colour[3] <= 255:
            rendering_surface.set_alpha(colour[3])
        elif colour[3] > 255:
            rendering_surface.set_alpha(255)
        else:
            rendering_surface.set_alpha(0)

    if isinstance(pos[0], str) and isinstance(pos[1], str):

        # evaluate expressions
        screen.blit(rendering_surface, (int(eval(pos[0])), int(eval(pos[1]))))

    else:
        try:
            screen.blit(rendering_surface, (pos[0], pos[1]))
        except IndexError:
            return None

    return 1


def draw_img(surface: pygame.Surface, img_path: str, _x: int, _y: int):
    """
    Draws an image with source imgpath at (x, y), on the surface surface

    Arguments:
    surface (pygame.Surface): the pygame surface to draw on
    imgpath (string): the path to the image
    x (int): where to the image (x-axis)
    y (int): where to the image (y-axis)
    """
    try:
        img = pygame.image.load(img_path)
    except pygame.error:
        return 0

    try:
        surface.blit(img, (_x, _y))
    except TypeError:
        return 0

    return 1


def draw_tile(surface: pygame.Surface, img_path: str, pos: tuple, area: tuple, angle: int = 0, flip: tuple = (False, False)):
    """
    Draws an image with source imgpath at (x, y), on the surface surface

    Arguments:
    surface (pygame.Surface): the pygame surface to draw on
    imgpath (string): the path to the image
    pos (tuple): 2-item, position on screen
    area (tuple): 4-item, area to crop from image. (top, left, width, height) format
    angle (int): 0, 1, 2, or 3. Rotates in 90-degree increments
    flip (tuple): (horz, vert) flips. Applied after rotation
    """
    try:
        img = pygame.image.load(img_path)
    except pygame.error:
        return 0

    cropped = pygame.transform.chop(img, pygame.rect.Rect(
        0, 0, area[0], area[1]))  # top, left
    cropped = pygame.transform.chop(cropped, pygame.rect.Rect(
        area[2], area[3], 543 - area[0], 543 - area[1]))  # bottom, right
    rotated_image = pygame.transform.rotate(
        cropped, 90*(4-angle))  # reversed direction
    final_image = pygame.transform.flip(rotated_image, flip[0], flip[1])
    # new_rect = rotated_image.get_rect(
    #    center=cropped.get_rect(topleft=(0, 0)).center)

    #surface.blit(rotated_image, (new_rect.topleft[0] + pos[0], new_rect.topleft[1] + pos[1]), area)

    surface.blit(final_image, (pos[0], pos[1]))

    return 1
