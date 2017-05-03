from PicturePuzzle import *
from TwoRingHexagonPicturePuzzle import *
root = Toplevel()

root.title("Hexagonal Puzzle")

def clear(widget):
    widget.config(state=NORMAL)
    widget.delete(0,END)

def picture_puzzle(pic):
    global load_picture
    load_picture = pic
    if pic == "space":
        load_picture = "space"
        run_picture_puzzle(load_picture)
    elif pic == "lion":
        load_picture = "lion"
        run_picture_puzzle(load_picture)
    elif pic == "mountain":
        load_picture = "mountain"
        run_picture_puzzle(load_picture)
    elif pic == "island":
        load_picture = "island"
        run_picture_puzzle(load_picture)
    elif pic == "city":
        load_picture = "city"
        run_picture_puzzle(load_picture)

def picture_puzzle2(pic):
    global load_picture
    load_picture = pic
    if pic == "space":
        load_picture = "space"
        run_picture_puzzle2(load_picture)
    elif pic == "lion":
        load_picture = "lion"
        run_picture_puzzle2(load_picture)
    elif pic == "mountain":
        load_picture = "mountain"
        run_picture_puzzle2(load_picture)
    elif pic == "island":
        load_picture = "island"
        run_picture_puzzle2(load_picture)
    elif pic == "city":
        load_picture = "city"
        run_picture_puzzle2(load_picture)

def web_cam_puzzle():
    execfile("WebCamPuzzle.py")

def web_cam_puzzle2():
    execfile("TwoRingHexagonWebCamPuzzle.py")

root.resizable(0,0)
Welcome = Label(root, text="Welcome to Hexagon Puzzle",font=("helvetica", 16, "bold"), justify=CENTER)
Welcome.grid(row=0, column=0, columnspan= 3)

choose = Label(root, text="Please Choose Which Picture You Would Like To Use",font=("helvetica", 13, "italic"), justify=CENTER)
choose.grid(row=1, column=0, columnspan= 3)

web_cam_image = PhotoImage(file='Images/webcam.gif')
web_cam_button = Button(root, image=web_cam_image, command=lambda: web_cam_puzzle())#Call web cam file here
web_cam_button.grid(row=2, column=0)



var = StringVar(root)
var.set("space")

option = OptionMenu(root, var, "lion", "space", "mountain", "island", "city")
option.grid(row= 6, column= 2)

picture_image = PhotoImage(file='Images/dragon.gif')
picture_button = Button(root, image=picture_image, command= lambda:picture_puzzle(var.get()))#Call picture file here
picture_button.grid(row=2, column=2)


web_cam_image2 = PhotoImage(file='Images/lilwebcam.gif')
web_cam_button2 = Button(root, image=web_cam_image2, command=lambda: web_cam_puzzle2())#Call web cam file here
web_cam_button2.grid(row=4, column=0)


picture_image2 = PhotoImage(file='Images/babydragon.gif')
picture_button2 = Button(root, image=picture_image2, command= lambda:picture_puzzle2(var.get()))#Call picture file here
picture_button2.grid(row=4, column=2)


web_cam_label = Label(root, text="3 RING HEXAGON Web Cam Picture",font=("helvetica", 10, "bold"),justify=CENTER)
web_cam_label.grid(row=3, column=0)

picture_label = Label(root, text="3 RING HEXAGON Pre-loaded Pictures",font=("helvetica", 10, "bold"),justify=CENTER)
picture_label.grid(row=3, column=2)


web_cam_label = Label(root, text="2 RING HEXAGON Web Cam Picture",font=("fangsongti", 10), justify=CENTER)
web_cam_label.grid(row=5, column=0)

picture_label = Label(root, text="2 RING HEXAGON Pre-loaded Pictures",font=("fangsongti", 10), justify=CENTER)
picture_label.grid(row=5, column=2)


choose_pic_label = Label(root, text="Pick A Pre Loaded Picture In the Dropdown Menu --->",font=('mincho',10,'italic'), justify=CENTER)
choose_pic_label.grid(row=6, column=0, columnspan= 2)

root.mainloop()