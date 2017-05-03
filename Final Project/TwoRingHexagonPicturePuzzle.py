from Tkinter import *
from time import sleep      #import delay
import numpy as np # for arrays
import random  # To support random moves when you click the hexagon
import collections          #import empty dictionary
from PIL import Image, ImageDraw, ImageTk

def run_picture_puzzle2(picture):

    root = Toplevel()
    root.title("3 RING HEXAGON Picture Puzzle")

    winningCondition = ({32: [27, 28, 33, 36], 33: [28, 29, 32, 34, 36, 37], 34: [29, 30, 33, 35, 37, 38], 35: [30, 31, 34, 38], 36: [32, 33, 37], 37: [33, 34, 36, 38], 38: [34, 35, 37], 20: [21, 23, 24], 21: [20, 22, 24, 25], 22: [21, 25, 26], 23: [20, 24, 27, 28], 24: [20, 21, 23, 25, 28, 29], 25: [21, 22, 24, 26, 29, 30], 26: [22, 25, 30, 31], 27: [23, 28, 32], 28: [23, 24, 27, 29, 32, 33], 29: [24, 25, 28, 30, 33, 34], 30: [25, 26, 29, 31, 34, 35], 31: [26, 30, 35]})

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

    polygon1 = [225.0, 238.39745962155615, 200.0, 281.6987298107781, 150.0, 281.6987298107781, 125.0,
                238.39745962155615, 149.99999999999997, 195.09618943233423, 200.0, 195.09618943233423]
    polygon2 = [300.0, 195.0961894323342, 275.0, 238.39745962155612, 225.0, 238.39745962155615, 200.0,
                195.0961894323342, 224.99999999999997, 151.79491924311228, 275.0, 151.79491924311228]
    polygon3 = [375.0, 151.79491924311228, 350.0, 195.0961894323342, 300.0, 195.0961894323342, 275.0,
                151.79491924311228, 300.0, 108.49364905389035, 350.0, 108.49364905389035]
    polygon4 = [225.0, 325.0, 200.0, 368.30127018922195, 150.0, 368.30127018922195, 125.0, 325.0, 149.99999999999997,
                281.6987298107781, 200.0, 281.69872981077805]
    polygon5 = [300.0, 281.69872981077805, 275.0, 325.0, 225.0, 325.0, 200.0, 281.69872981077805, 224.99999999999997,
                238.39745962155612, 275.0, 238.39745962155612]
    polygon6 = [375.0, 238.39745962155615, 350.0, 281.6987298107781, 300.0, 281.6987298107781, 275.0,
                238.39745962155615, 300.0, 195.09618943233423, 350.0, 195.09618943233423]
    polygon7 = [450.0, 195.0961894323342, 425.0, 238.39745962155612, 375.0, 238.39745962155615, 350.0,
                195.0961894323342, 375.0, 151.79491924311228, 425.0, 151.79491924311228]
    polygon8 = [225.0, 411.60254037844385, 200.0, 454.9038105676658, 150.0, 454.9038105676658, 125.0,
                411.60254037844385, 149.99999999999997, 368.30127018922195, 200.0, 368.3012701892219]
    polygon9 = [300.0, 368.30127018922195, 275.0, 411.6025403784439, 225.0, 411.6025403784439, 200.0,
                368.30127018922195, 224.99999999999997, 325.00000000000006, 275.0, 325.0]
    polygon10 = [375.0, 325.0, 350.0, 368.30127018922195, 300.0, 368.30127018922195, 275.0, 325.0, 300.0,
                 281.6987298107781, 350.0, 281.69872981077805]
    polygon11 = [450.0, 281.69872981077805, 425.0, 325.0, 375.0, 325.0, 350.0, 281.69872981077805, 375.0,
                 238.39745962155612, 425.0, 238.39745962155612]
    polygon12 = [525.0, 238.39745962155615, 500.0, 281.6987298107781, 450.0, 281.6987298107781, 425.0,
                 238.39745962155615, 450.0, 195.09618943233423, 500.0, 195.09618943233423]
    polygon13 = [300.0, 454.9038105676658, 275.0, 498.20508075688775, 225.0, 498.20508075688775, 200.0,
                 454.9038105676658, 224.99999999999997, 411.6025403784439, 275.0, 411.60254037844385]
    polygon14 = [375.0, 411.60254037844385, 350.0, 454.9038105676658, 300.0, 454.9038105676658, 275.0,
                 411.60254037844385, 300.0, 368.30127018922195, 350.0, 368.3012701892219]
    polygon15 = [450.0, 368.30127018922195, 425.0, 411.6025403784439, 375.0, 411.6025403784439, 350.0,
                 368.30127018922195, 375.0, 325.00000000000006, 425.0, 325.0]
    polygon16 = [525.0, 325.0, 500.0, 368.30127018922195, 450.0, 368.30127018922195, 425.0, 325.0, 450.0,
                 281.6987298107781, 500.0, 281.69872981077805]
    polygon17 = [375.0, 498.2050807568877, 350.0, 541.50635094610959, 300.0, 541.50635094610959, 275.0,
                 498.2050807568877, 300.0, 454.9038105676658, 350.0, 454.90381056766574]
    polygon18 = [450.0, 454.9038105676658, 425.0, 498.20508075688775, 375.0, 498.20508075688775, 350.0,
                 454.9038105676658, 375.0, 411.6025403784439, 425.0, 411.60254037844385]
    polygon19 = [525.0, 411.60254037844385, 500.0, 454.9038105676658, 450.0, 454.9038105676658, 425.0,
                 411.60254037844385, 450.0, 368.30127018922195, 500.0, 368.3012701892219]

    polygon = [polygon1, polygon2, polygon3, polygon4, polygon5, polygon6, polygon7,
               polygon8, polygon9, polygon10, polygon11, polygon12, polygon13, polygon14,
               polygon15, polygon16, polygon17, polygon18, polygon19]

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
    hexID=38  # The selected transparent tilec
    canvas1.itemconfig(hexID, fill="", activefill="", outline="blue", state="hidden")  # making it transparent
    canvas1.itemconfig(19, state="hidden")
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
                canvas1.move(tile - 19, deltax, deltay)  # basically swap tiles with the clicked tile
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

    hexIDs = range(20, 39)
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

    solve_button = Button(root, text="Solve",font=('fixedsys', 20),bg='green',fg='white',command=lambda: solve())  # Call web cam file here
    solve_button.grid(row=1, column=0)

    for i in range(1,15):
        root.after(i, scramble())  # starting scramble


    root.mainloop()
    #print hexagonImages
    #print len(hexagonImages)