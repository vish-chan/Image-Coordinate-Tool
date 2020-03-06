import sys, pygame, getopt

black = (0,0,0)
white = (255, 255, 255)
FPS = 60


def translateCoordinates(coordinate, size):
    x, y = coordinate
    hd_constant = 960 / (size[0] / 2), 540 / (size[1] / 2)
    x, y = x-size[0]/2, 0 - (y-size[1]/2)
    x, y = int(hd_constant[0]*x), int(hd_constant[1]*y)
    return x, y

def drawGrid(screen, size):
    pygame.draw.line(screen, white, (int(size[0] / 2), 0), (int(size[0] / 2), size[1]))
    pygame.draw.line(screen, white, (0, int(size[1] / 2)), (size[0], int(size[1] / 2)))

def usageError():
    print('coordinates.py -i <imagefile> (optional : -w <width> -l <height> -g)')
    sys.exit(2)

def main(argv):
    size = 960, 540
    image_name = ""
    w, h = 0, 0
    grid=False
    try:
        opts, args = getopt.getopt(argv, "hi:w:l:g", ["image=", "widhth=", "length="])
    except getopt.GetoptError:
        usageError()
    if(len(opts)==0):
        usageError()
    for opt, arg in opts:
        if(opt=='-h'):
            usageError()
        elif(opt in ('-i', "--image")):
            image_name = arg
        elif (opt in ('-w', "--width")):
            w = int(arg)
        elif (opt in ('-l', "--length")):
            h = int(arg)
        elif (opt == '-g'):
            grid = True
        else:
            usageError()
    if(len(image_name)==0):
        usageError()
    if(w>=size[0] and h>=size[1]):
        size = w, h
    pygame.init()
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    img = pygame.image.load(image_name)
    img = pygame.transform.scale(img, size)

    while 1:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                sys.exit()
            elif (event.type == pygame.MOUSEMOTION):
                coordinates = pygame.mouse.get_pos()
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                coordinates = pygame.mouse.get_pos()
        coordinates_translated = translateCoordinates(coordinates, size)
        textsurface = myfont.render(str(coordinates_translated[0]) + " ," + str(coordinates_translated[1]), True, white)
        screen.fill((0, 0, 0));
        screen.blit(img, (0, 0))
        if(grid):
            drawGrid(screen, size)
        screen.blit(textsurface, (0, 0))
        pygame.draw.line(screen, white, (coordinates[0], 0), (coordinates[0], size[1]))
        pygame.draw.line(screen, white, (0, coordinates[1]), (size[0], coordinates[1]))
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == '__main__':
    main(sys.argv[1:])


