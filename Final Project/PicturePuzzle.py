from Tkinter import *
from time import sleep      #import delay
import numpy as np # for arrays
import random  # To support random moves when you click the hexagon
import collections          #import empty dictionary
from PIL import Image, ImageDraw, ImageTk

def run_picture_puzzle(picture):

    root = Toplevel()
    root.title("3 RING HEXAGON Picture Puzzle")

    winningCondition = (
    {38: [39, 42, 43], 39: [38, 40, 43, 44], 40: [39, 41, 44, 45], 41: [40, 45, 46], 42: [38, 43, 47, 48],
     43: [38, 39, 42, 44, 48, 49], 44: [39, 40, 43, 45, 49, 50], 45: [40, 41, 44, 46, 50, 51], 46: [41, 45, 51, 52],
     47: [42, 48, 53, 54], 48: [42, 43, 47, 49, 54, 55], 49: [43, 44, 48, 50, 55, 56], 50: [44, 45, 49, 51, 56, 57],
     51: [45, 46, 50, 52, 57, 58], 52: [46, 51, 58, 59], 53: [47, 54, 60], 54: [47, 48, 53, 55, 60, 61],
     55: [48, 49, 54, 56, 61, 62], 56: [49, 50, 55, 57, 62, 63], 57: [50, 51, 56, 58, 63, 64],
     58: [51, 52, 57, 59, 64, 65], 59: [52, 58, 65], 60: [53, 54, 61, 66], 61: [54, 55, 60, 62, 66, 67],
     62: [55, 56, 61, 63, 67, 68], 63: [56, 57, 62, 64, 68, 69], 64: [57, 58, 63, 65, 69, 70], 65: [58, 59, 64, 70],
     66: [60, 61, 67, 71], 67: [61, 62, 66, 68, 71, 72], 68: [62, 63, 67, 69, 72, 73], 69: [63, 64, 68, 70, 73, 74],
     70: [64, 65, 69, 74], 71: [66, 67, 72], 72: [67, 68, 71, 73], 73: [68, 69, 72, 74], 74: [69, 70, 73]})

    WIDTH = 650.0 # Canvas dimensions
    HEIGHT = 650.0
    print "Images/%s.gif" %picture
    image = Image.open("Images/%s.gif" %picture) # opening the image from photo booth
    [imageSizeWidth, imageSizeHeight] = image.size

    newImageSizeWidth = int(WIDTH-25)
    newImageSizeHeight = int(HEIGHT-25)

    image = image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS) # resizing the image to fit the canvas
    resizeFile = "ResizedHexagonImage.gif"
    resizedImage = image.save(resizeFile)
    global canvas1
    canvas1 = Canvas(root, width=WIDTH, height=HEIGHT, bg="beige", highlightthickness=0, bd=0)
    canvas1.grid(row=0, column=0, padx=5, pady=5, sticky='NSWE')

    r = 40  # Radius of the hexagon's circumcircle in pixels.
    # Get the center of the canvas.
    global xc, yc
    xc = WIDTH / 2
    yc = HEIGHT / 2

    # Setting up the hexagon image to be broken depcomposed
    puzzleImage = PhotoImage(file="ResizedHexagonImage.gif")  # opening the photo
    im = Image.open("ResizedHexagonImage.gif").convert("RGBA")
    global imageArray
    imageArray = np.asarray(im)  # converting image into a numpy array
    global hexagonImages
    hexagonImages = []  # dictionary to store the hexagon images

    def drawHexagonImage(polygon, x, y):
        global imageArray, canvas1, hexagonImages

        maskImage = Image.new('L', (imageArray.shape[1], imageArray.shape[0]), 0)  # create a mask array
        ImageDraw.Draw(maskImage).polygon(polygon, outline=1, fill=1)
        mask = np.array(maskImage)  # assemble new image (uint8: 0-255)
        newImageArray = np.empty(imageArray.shape, dtype='uint8')  # colors (three first columns, RGB)
        newImageArray[:, :, :3] = imageArray[:, :, :3]  # transparency (4th column)
        newImageArray[:, :, 3] = mask * 255  # back to Image from numpy
        newIm = Image.fromarray(newImageArray, "RGBA")

        hexObj = {}  # storing the hexagon images
        hexObj["tk"] = ImageTk.PhotoImage(newIm)
        hexObj["img"] = canvas1.create_image((xc - 13, yc - 13), image=hexObj["tk"])  # putting the image into tk

        hexagonImages.append(hexObj)  # adding the hexagons as its created

    def hexagon(m, n):
        xc = WIDTH / 2;
        yc = HEIGHT / 2
        cc = np.array([xc, yc])  # Center of the canvas.
        global r  # The scale of the hexagons. Radius for the circumcircle of each hexagon.
        # the magic translation vectors for a hexagonal tesselation.
        # With numpy, vectors (and matrices for that matter) are just Python arrays
        v1 = r * np.array([1 + np.cos(np.pi / 3), np.sin(np.pi / 3)])
        v2 = r * np.array([1 + np.cos(np.pi / 3), -np.sin(np.pi / 3)])  # Only a sign difference.
        z = m * v1 + n * v2 + cc  # Be sure to add the canvas center.
        return z

    polygon1 = [150.0, 195.0961894323342, 125.0, 238.39745962155612, 75.000000000000014, 238.39745962155615, 50.0,
                195.0961894323342, 74.999999999999972, 151.79491924311228, 125.0, 151.79491924311228]
    polygon2 = [225.0, 151.79491924311228, 200.0, 195.0961894323342, 150.0, 195.0961894323342, 125.0,
                151.79491924311228, 149.99999999999997, 108.49364905389035, 200.0, 108.49364905389035]
    polygon3 = [300.0, 108.49364905389035, 275.0, 151.79491924311228, 225.0, 151.7949192431123, 200.0,
                108.49364905389035, 224.99999999999997, 65.192378864668427, 275.0, 65.192378864668427]
    polygon4 = [375.0, 65.192378864668399, 350.0, 108.49364905389032, 300.0, 108.49364905389034, 275.0,
                65.192378864668399, 300.0, 21.891108675446482, 350.0, 21.891108675446468]
    polygon5 = [150.0, 281.69872981077805, 125.0, 325.0, 75.000000000000014, 325.0, 50.0, 281.69872981077805,
                74.999999999999972, 238.39745962155612, 125.0, 238.39745962155612]
    polygon6 = [225.0, 238.39745962155615, 200.0, 281.6987298107781, 150.0, 281.6987298107781, 125.0,
                238.39745962155615, 149.99999999999997, 195.09618943233423, 200.0, 195.09618943233423]
    polygon7 = [300.0, 195.0961894323342, 275.0, 238.39745962155612, 225.0, 238.39745962155615, 200.0,
                195.0961894323342, 224.99999999999997, 151.79491924311228, 275.0, 151.79491924311228]
    polygon8 = [375.0, 151.79491924311228, 350.0, 195.0961894323342, 300.0, 195.0961894323342, 275.0,
                151.79491924311228, 300.0, 108.49364905389035, 350.0, 108.49364905389035]
    polygon9 = [450.0, 108.49364905389035, 425.0, 151.79491924311228, 375.0, 151.7949192431123, 350.0,
                108.49364905389035, 375.0, 65.192378864668427, 425.0, 65.192378864668427]
    polygon10 = [150.0, 368.30127018922195, 125.0, 411.6025403784439, 75.000000000000014, 411.6025403784439, 50.0,
                 368.30127018922195, 74.999999999999972, 325.00000000000006, 125.0, 325.0]
    polygon11 = [225.0, 325.0, 200.0, 368.30127018922195, 150.0, 368.30127018922195, 125.0, 325.0, 149.99999999999997,
                 281.6987298107781, 200.0, 281.69872981077805]
    polygon12 = [300.0, 281.69872981077805, 275.0, 325.0, 225.0, 325.0, 200.0, 281.69872981077805, 224.99999999999997,
                 238.39745962155612, 275.0, 238.39745962155612]
    polygon13 = [375.0, 238.39745962155615, 350.0, 281.6987298107781, 300.0, 281.6987298107781, 275.0,
                 238.39745962155615, 300.0, 195.09618943233423, 350.0, 195.09618943233423]
    polygon14 = [450.0, 195.0961894323342, 425.0, 238.39745962155612, 375.0, 238.39745962155615, 350.0,
                 195.0961894323342, 375.0, 151.79491924311228, 425.0, 151.79491924311228]
    polygon15 = [525.0, 151.79491924311228, 500.0, 195.0961894323342, 450.0, 195.0961894323342, 425.0,
                 151.79491924311228, 450.0, 108.49364905389035, 500.0, 108.49364905389035]
    polygon16 = [150.0, 454.9038105676658, 125.0, 498.20508075688775, 75.000000000000014, 498.20508075688775, 50.0,
                 454.9038105676658, 74.999999999999972, 411.6025403784439, 125.0, 411.60254037844385]
    polygon17 = [225.0, 411.60254037844385, 200.0, 454.9038105676658, 150.0, 454.9038105676658, 125.0,
                 411.60254037844385, 149.99999999999997, 368.30127018922195, 200.0, 368.3012701892219]
    polygon18 = [300.0, 368.30127018922195, 275.0, 411.6025403784439, 225.0, 411.6025403784439, 200.0,
                 368.30127018922195, 224.99999999999997, 325.00000000000006, 275.0, 325.0]
    polygon19 = [375.0, 325.0, 350.0, 368.30127018922195, 300.0, 368.30127018922195, 275.0, 325.0, 300.0,
                 281.6987298107781, 350.0, 281.69872981077805]
    polygon20 = [450.0, 281.69872981077805, 425.0, 325.0, 375.0, 325.0, 350.0, 281.69872981077805, 375.0,
                 238.39745962155612, 425.0, 238.39745962155612]
    polygon21 = [525.0, 238.39745962155615, 500.0, 281.6987298107781, 450.0, 281.6987298107781, 425.0,
                 238.39745962155615, 450.0, 195.09618943233423, 500.0, 195.09618943233423]
    polygon22 = [600.0, 195.0961894323342, 575.0, 238.39745962155612, 525.0, 238.39745962155615, 500.0,
                 195.0961894323342, 525.0, 151.79491924311228, 575.0, 151.79491924311228]
    polygon23 = [225.0, 498.2050807568877, 200.0, 541.50635094610959, 150.0, 541.50635094610959, 125.0,
                 498.2050807568877, 149.99999999999997, 454.9038105676658, 200.0, 454.90381056766574]
    polygon24 = [300.0, 454.9038105676658, 275.0, 498.20508075688775, 225.0, 498.20508075688775, 200.0,
                 454.9038105676658, 224.99999999999997, 411.6025403784439, 275.0, 411.60254037844385]
    polygon25 = [375.0, 411.60254037844385, 350.0, 454.9038105676658, 300.0, 454.9038105676658, 275.0,
                 411.60254037844385, 300.0, 368.30127018922195, 350.0, 368.3012701892219]
    polygon26 = [450.0, 368.30127018922195, 425.0, 411.6025403784439, 375.0, 411.6025403784439, 350.0,
                 368.30127018922195, 375.0, 325.00000000000006, 425.0, 325.0]
    polygon27 = [525.0, 325.0, 500.0, 368.30127018922195, 450.0, 368.30127018922195, 425.0, 325.0, 450.0,
                 281.6987298107781, 500.0, 281.69872981077805]
    polygon28 = [600.0, 281.69872981077805, 575.0, 325.0, 525.0, 325.0, 500.0, 281.69872981077805, 525.0,
                 238.39745962155612, 575.0, 238.39745962155612]
    polygon29 = [300.0, 541.50635094610971, 275.0, 584.8076211353316, 225.0, 584.8076211353316, 200.0,
                 541.50635094610971, 224.99999999999997, 498.20508075688781, 275.0, 498.20508075688775]
    polygon30 = [375.0, 498.2050807568877, 350.0, 541.50635094610959, 300.0, 541.50635094610959, 275.0,
                 498.2050807568877, 300.0, 454.9038105676658, 350.0, 454.90381056766574]
    polygon31 = [450.0, 454.9038105676658, 425.0, 498.20508075688775, 375.0, 498.20508075688775, 350.0,
                 454.9038105676658, 375.0, 411.6025403784439, 425.0, 411.60254037844385]
    polygon32 = [525.0, 411.60254037844385, 500.0, 454.9038105676658, 450.0, 454.9038105676658, 425.0,
                 411.60254037844385, 450.0, 368.30127018922195, 500.0, 368.3012701892219]
    polygon33 = [600.0, 368.30127018922195, 575.0, 411.6025403784439, 525.0, 411.6025403784439, 500.0,
                 368.30127018922195, 525.0, 325.00000000000006, 575.0, 325.0]
    polygon34 = [375.0, 584.8076211353316, 350.0, 628.1088913245535, 300.0, 628.1088913245535, 275.0, 584.8076211353316,
                 300.0, 541.50635094610971, 350.0, 541.50635094610971]
    polygon35 = [450.0, 541.50635094610971, 425.0, 584.8076211353316, 375.0, 584.8076211353316, 350.0,
                 541.50635094610971, 375.0, 498.20508075688781, 425.0, 498.20508075688775]
    polygon36 = [525.0, 498.2050807568877, 500.0, 541.50635094610959, 450.0, 541.50635094610959, 425.0,
                 498.2050807568877, 450.0, 454.9038105676658, 500.0, 454.90381056766574]
    polygon37 = [600.0, 454.9038105676658, 575.0, 498.20508075688775, 525.0, 498.20508075688775, 500.0,
                 454.9038105676658, 525.0, 411.6025403784439, 575.0, 411.60254037844385]

    polygon = [polygon1, polygon2, polygon3, polygon4, polygon5, polygon6, polygon7, polygon8, polygon9, polygon10,
               polygon11, polygon12, polygon13, polygon14, polygon15, polygon16, polygon17, polygon18, polygon19,
               polygon20,
               polygon21, polygon22, polygon23, polygon24, polygon25, polygon26, polygon27, polygon28, polygon29,
               polygon30,
               polygon31, polygon32, polygon33, polygon34, polygon35, polygon36, polygon37]

    for i in range(len(polygon)):
        drawHexagonImage(polygon[i], polygon[i][0], polygon[i][1])
    for i in range(len(polygon)):
        hexagonImages[i]['poly'] = canvas1.create_polygon(polygon[i], fill='', activefill="green", outline="red",
                                                          width=4)

    rings = []  # A list of rings
    hexIDs = []  # A list of IDs for all your hexagons
    global get_center_of_hexagon
    get_center_of_hexagon = {}
    def get_center_of_hexagon(hexID):
        points = canvas1.coords(hexID)
        xc, yc = points[0] - r, points[1]
        return xc, yc

    def check_if_win():
        global valid_moves
        if startChecking == True:
            #print "I am in the checking loop"
            if winningCondition == valid_moves:
                sleep(1)
                print "You solved the puzzle! YOU WIN!!!"
                winningScreen()
                winCaption = Label(canvas1, text='YOU SOLVED THE PUZZLE!', font=('fixedsys', 26), fg='red',
                                      bg='black')
                winCaption.place(x=WIDTH/2, y=HEIGHT/2 , relwidth=1.0, anchor=CENTER)

    def winningScreen():
        canvas1.delete("all")
        canvas1.create_image(325, 325, image=puzzleImage, anchor=CENTER)

    # print 'The center of the canvas has coordinates [%d, %d]' % (xc, yc)
    points = []
    for k in range(6):
        x, y = xc + r * np.cos(k * np.pi / 3), yc + r * np.sin(k * np.pi / 3)
        points.extend([x, y])  # Use extend to add more than one item to a list at a time.
    global hexID
    hexID = 74  # The selected transparent tilec
    canvas1.itemconfig(hexID, fill="", activefill="", outline="blue", state="hidden")  # making it transparent
    canvas1.itemconfig(37, state="hidden")
    # print "The first hexagon has the coordinates: ", canvas1.coords(hexID)
    # print "The first hexagon is centered on: ", get_center_of_hexagon(hexID)

    number_of_moves = 0
    # Recursive method to move the specified tile with a simple animation
    total_moves = 0
    global click

    def click(event):  # selecting the tile
        if canvas1.find_withtag(CURRENT):
            selected_tile = canvas1.find_withtag(CURRENT)[0]  # getting the selected tile ID
            move(selected_tile)  # call the move command

    global move_stack, validMoves
    move_stack = []

    def validMoves():
        global valid_moves
        del valid_moves
        valid_moves = collections.defaultdict(list)
        for i in hexIDs:  # dictionary of all tiles and the value moves within each tile
            for j in hexIDs:
                x = get_center_of_hexagon(i)
                y = get_center_of_hexagon(j)
                distance = np.sqrt(((x[0] - y[0]) ** 2) + ((x[1] - y[1]) ** 2))
                if distance < 87 and distance > 1:
                    valid_moves[i].append(j)
        #print "valid_moves: ", valid_moves
    global move
    def move(tile):
        global number_of_moves, move_stack, get_center_of_hexagon, hexID, click

        x = get_center_of_hexagon(tile)  # Coordinate of Clicked Tile
        y = get_center_of_hexagon(hexID)  # Coordinate of the Current Transparent Tile
        distance = np.sqrt(((x[0] - y[0]) ** 2) + ((x[1] - y[1]) ** 2))  # Find the distance between the two tile
        if distance < 87 and distance > 1:  # only move if the clicked tile is next to the transparent tile
            canvas1.unbind("<Button-1>")  # disable clicking while animation is going on
            movex_to_dest = get_center_of_hexagon(tile)[0] - get_center_of_hexagon(hexID)[
                0]  # distance from clicked tile x direction
            movey_to_dest = get_center_of_hexagon(tile)[1] - get_center_of_hexagon(hexID)[
                1]  # distance from clicked tile y direction
            movex_to_origin = get_center_of_hexagon(hexID)[0] - get_center_of_hexagon(tile)[
                0]  # distance from transparent tile x direction
            movey_to_origin = get_center_of_hexagon(hexID)[1] - get_center_of_hexagon(tile)[
                1]  # distance from transparent tile y direction
            for i in range(20):
                deltax = movex_to_dest / 20.0
                deltay = movey_to_dest / 20.0  # Break up the move into 20 small steps for the animation.
                canvas1.move(hexID, deltax, deltay)  # basically swap tiles with the transparent
                sleep(0.015)
                canvas1.update()
            for i in range(20):
                deltax = movex_to_origin / 20.0
                deltay = movey_to_origin / 20.0  # Break up the move into 20 small steps for the animation.
                canvas1.move(tile, deltax, deltay)  # basically swap tiles with the clicked tile
                sleep(0.015)
                canvas1.update()
            for i in range(20):
                deltax = movex_to_origin / 20.0
                deltay = movey_to_origin / 20.0  # Break up the move into 20 small steps for the animation.
                canvas1.move(tile - 37, deltax, deltay)  # basically swap tiles with the clicked tile
                # sleep(0.015)
                canvas1.update()
            # number_of_moves += 1
            move_stack.append(tile)
            # print "Move number %d" % number_of_moves
            #print "Tile ID %d has been swapped with tile ID %d" % (tile, hexID)
            canvas1.bind("<Button-1>", click)  # Re-enable clicking
            validMoves()
            check_if_win()
            return 1  # return 1 if the tile has been successfully moved
        else:
            print "Invalid tile movement"  # return error if the clicked tile is not next to the transparent tile
            return 0  # also return 0 if the tile hasn't moved

    ## when moving, it is swapping the transparent tile with the clicked tile, even though the transparent tile can't be seen
    ## it still has the value of hexID
    global valid_moves
    valid_moves = collections.defaultdict(list)  # empty dictionary

    hexIDs = range(38, 75)
    global startChecking
    startChecking = False
    def scramble():
        global valid_moves, startChecking
        for i in hexIDs:  # dictionary of all tiles and the value moves within each tile
            for j in hexIDs:
                x = get_center_of_hexagon(i)
                y = get_center_of_hexagon(j)
                distance = np.sqrt(((x[0] - y[0]) ** 2) + ((x[1] - y[1]) ** 2))
                if distance < 87 and distance > 1:
                    valid_moves[i].append(j)
        #print valid_moves
        ran_tile = random.choice(valid_moves[hexID])
        check_if_move_is_good = move(ran_tile)
        if check_if_move_is_good == 0:  # if scramble made a invalid move then it will choose another move
            ran_tile = random.choice(valid_moves[hexID])  # no effect to the stack
            move(ran_tile)

        startChecking = True
        #print startChecking

    canvas1.bind("<Button-1>", click)  # tile Click

    def solve():
        global solve
        move_stackCount = len(move_stack)
        prevMoves = move_stack
        #print prevMoves
        for i in range(1, move_stackCount + 1):
            tile = prevMoves[move_stackCount - i]  # manual .pop()
            del prevMoves[move_stackCount - i]  # manual .pop()
            move(tile)

    solve_button = Button(root, text="Solve",font=('fixedsys', 20),bg='green',fg='white', command=lambda: solve())  # Call web cam file here
    solve_button.grid(row=1, column=0)

    for i in range(1,15):
        root.after(i, scramble())  # starting scramble


    root.mainloop()
    #print hexagonImages
    #print len(hexagonImages)