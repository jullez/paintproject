#graphics.py
from pygame import *#1677725
init()
from random import *
from math import *

dekuRect=Rect(20,450,80,80)#sets all the rectangles needed for buttons
sprayRect=Rect(20,50,80,80)#screen.get_at(mx,my) will be useful for later, gets colors if the  mouse ins on top of a pallete
lineRect=Rect(20,150,80,80)
canvas=Rect(150,50,800,630)#1 and 2 is the initial x,y second one is len and width
majRect=Rect(20,250,80,80)
fdRect=Rect(20,350,80,80)
goronRect=Rect(20,550,80,80)
zoraRect=Rect(200,700,80,80)
kidRect=Rect(300,700,80,80)
linkRect=Rect(400,700,80,80)
wheelRect=Rect(20,650,85,134)
cRect=Rect(950,0,50,50)
saveRect=Rect(5,5,30,30)
undRect=Rect(45,5,30,30)
redRect=Rect(80,5,30,30)
rectRect=Rect(500,700,80,80)
unrectRect=Rect(600,700,80,80)
undC=0

title="Majora's Paint"
fnt=font.Font("Triforce.ttf",40)
titleTxt=fnt.render(title,True,(255,0,0))

dekuIcon=image.load("dekuIcon.png")#loads image for the stickers and the graphics within the rectangles (icons are the graphics, pics are the stickers)
dekuPic=image.load("dekuPic.png")
fdIcon=image.load("fdIcon.png")
fdPic=image.load("fdPic.png")
majIcn=image.load("majIcon.png")
majPic=image.load("majPic.png")
penIcn=image.load("penIcn.png")
sprayIcn=image.load("sprayIcn.png")
backg=image.load("Assets/bg.jpg")#loads the background
goronIcon=image.load("goronIcon.png")
goronPic=image.load('goronPic.png')
zoraPic=image.load("zoraPic.png")
zoraIcon=image.load("zoraIcon.png")
kidPic=image.load('kidPic.png')
kidIcon=image.load('kidIcon.png')
linkIcon=image.load("linkIcon.png")
linkPic=image.load("linkPic.png")
wheel=image.load("wheel.png")
saveIcn=image.load("saveIcn.png")
gs=image.load("grayscale.jpg")
redIcn=image.load("redoIcn.png")
undIcn=image.load("undoIcn.png")

mx,my=0,0#gets the mouse position used later for the pencil function
size=5#starts up the size of the brushes and pencils
spray=0#these are the "booleans" for each of the functions in the program. making them true and false was too much of a hassle due in part to the necessary capitalization
line=1
maj=0
fd=0
dk=0
gr=0
zr=0
kid=0
link=0
bg=(16777215)#sets the background colour
c=(0)
redoC=0
rect=0
unrect=0



screen=display.set_mode((1000,800))#sets the screen size, 800,600
screen.fill(0)#fills the screen with white
screen.blit(backg,(0,0))#adds the background image

screen.blit(titleTxt,(350,15))
draw.rect(screen,(bg),canvas)#draws the canvas

running=True
while running:
    for e in event.get():
        if e.type==QUIT:
            running=False
        if e.type==MOUSEBUTTONDOWN and canvas.collidepoint(mx,my):
            und=screen.copy()
            red=screen.copy()
            cap=screen.copy()

            if e.button==1:
                rmx,rmy=e.pos



            if e.button==4:
                size+=1#if the wheel is rotated upwards the size increases
            elif e.button==5:
                size-=1#if it's rotated downwards it decreases
                if size<=0:#if it reaches 0 it is increased back to 1 to prevent crashes
                    size+=1
        if e.type==MOUSEBUTTONUP and canvas.collidepoint(mx,my):
            rmx=0
            rmy=0



    #-------------------------------------------

    omx,omy=mx,my#gets the mouse positions used for the pencil

    mx,my=mouse.get_pos()#gets the mouse position used for everything else

    mb=mouse.get_pressed()#checks the mouse buttons    mouse.set_cursor(circle(0,size,1))


    draw.rect(screen,(134,246,130),dekuRect,2)#draws the buttons

    draw.rect(screen,(0,255,0),sprayRect,2)

    draw.rect(screen,(255,0,0),lineRect,2)

    draw.rect(screen,(0),majRect,2)

    draw.rect(screen,(0,255,255),fdRect,2)

    draw.rect(screen,(255,0,0),rectRect,0)

    draw.rect(screen,(139,106,55),goronRect,2)

    draw.rect(screen,(59,195,234),zoraRect,2)

    draw.rect(screen,(103,25,153),majRect,2)

    draw.rect(screen,(68,150,82),linkRect,2)

    draw.rect(screen,(16777215),kidRect,2)

    draw.rect(screen,(255,0,0),unrectRect,1)

    draw.rect(screen,(c),cRect)#a neat little colour indicator, top right

    screen.blit(majIcn,(20,250))#adds the graphics on top of the buttons

    screen.blit(fdIcon,(20,350))

    screen.blit(penIcn,(20,150))

    screen.blit(sprayIcn,(20,50))

    screen.blit(dekuIcon,(20,450))

    screen.blit(goronIcon,(20,550))

    screen.blit(wheel,(20,650))

    screen.blit(zoraIcon,(200,700))

    screen.blit(kidIcon,(300,700))

    screen.blit(linkIcon,(400,700))

    screen.blit(saveIcn,(5,5))

    screen.blit(gs,(20,740))

    screen.blit(undIcn,(40,5))

    screen.blit(redIcn,(80,5))

##    if mb[0]==1:
##        cap=screen.copy()

    if wheelRect.collidepoint(mx,my)and mb[0]==1:#if the rectangle around the color selector touches the mouse(it's invisible, didn't draw it)
        c=screen.get_at((mx,my))#it takes the color the user is currently mousing over
    elif wheelRect.collidepoint(mx,my)and mb[1]==1:
        bg=screen.get_at((mx,my))
    if saveRect.collidepoint(mx,my) and mb[0]==1:
        fileName=input('Enter Filename:')
        if "." not in fileName:
            fileName += ".png"
        image.save(screen.subsurface(canvas),fileName)

    if unrectRect.collidepoint(mx,my) and mb[0]==1:
        unrect=1
        rect=0
        zr=0
        kid=0
        gr=0
        dk=0
        maj=0
        link=0
        line=0
        spray=0
        fd=0
    if rectRect.collidepoint(mx,my) and mb[0]==1:
        rect=1
        zr=0
        kid=0
        gr=0
        dk=0
        maj=0
        link=0
        line=0
        spray=0
        fd=0
        unrect=0

    if zoraRect.collidepoint(mx,my) and mb[0]==1:#if the rectangles are clicked the appropriate function is activated, everything else is deactivated
        draw.rect(screen,(255,0,0),zoraRect,2)
        zr=1
        kid=0
        gr=0
        dk=0
        maj=0
        link=0
        line=0
        spray=0
        fd=0
        rect=0
        unrect=0
    if kidRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(0,0,0),kidRect,2)
        zr=0
        kid=1
        gr=0
        dk=0
        maj=0
        line=0
        link=0
        spray=0
        fd=0
        rect=0
        unrect=0
    if goronRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(210,49,151),goronRect,2)
        gr=1
        dk=0
        maj=0
        line=0
        spray=0
        fd=0
        zr=0
        kid=0
        link=0
        rect=0
        unrect=0

    if dekuRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(137,204,212),dekuRect,2)
        dk=1
        maj=0
        line=0
        spray=0
        fd=0
        gr=0
        zr=0
        kid=0
        link=0
        rect=0
        unrect=0

    if majRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(16777215),majRect,2)
        maj=1
        line=0
        spray=0
        fd
        dk=0
        gr=0
        zr=0
        kid=0
        link=0
        rect=0
        unrect=0

    if fdRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(128,0,255),fdRect,2)
        fd=1
        maj=0
        line=0
        spray=0
        dk=0
        gr=0
        zr=0
        kid=0
        link=0
        rect=0
        unrect=0

    if lineRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(0,0,255),lineRect,2)
        line=1
        spray=0
        maj=0
        fd=0
        dk=0
        gr=0
        zr=0
        kid=0
        link=0
        rect=0
        unrect=0

    if sprayRect.collidepoint(mx,my) and mb[0]==1:#same for all of the above
        draw.rect(screen,(255,0,0),sprayRect,2)
        spray=1
        line=0
        maj=0
        fd=0
        dk=0
        gr=0
        zr=0
        kid=0
        link=0
        rect=0
        unrect=0

    if linkRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(165,37,38),linkRect,2)
        link=1
        line=0
        maj=0
        fd=0
        dk=0
        gr=0
        zr=0
        kid=0
        spray=0
        rect=0
        unrect=0

    if mb[0]==1 and gr==1 and canvas.collidepoint(mx,my):#if the function is activated and the mouse is in contact with the canvas the appropriate function will be performed
        screen.set_clip(canvas)#makes it so that the image won't flood into the background
        screen.blit(goronPic,(mx-75,my-55))#had to shift the image around so that their centers spawn on top of the mouse, not their upper left corners
        screen.set_clip(None)#undoes the background thing

    if mb[0]==1 and line==1 and canvas.collidepoint(mx,my):#draw line
        screen.set_clip(canvas)
        draw.line(screen,(c),(omx,omy),(mx,my),size)
        screen.set_clip(None)

    if mb[0]==1 and spray==1 and canvas.collidepoint(mx,my):#spray paint
        screen.set_clip(canvas)
        sprayx=randint(mx-size,mx+size)#makes the random coordinates used for the spray paint
        sprayy=randint(my-size,my+size)
        if hypot(mx-sprayx,my-sprayy)<size:#checks if the random circles are being drawn within the circular bounds of the spray paint

            draw.circle(screen,(c),(sprayx,sprayy),1)
            time.wait(5)#makes it so that the circle isn't filled instantly
        screen.set_clip(None)

    if mb[0]==1 and maj==1 and canvas.collidepoint(mx,my):#majora's mask
        screen.set_clip(canvas)
        screen.blit(majPic,(mx-75,my-55))
        screen.set_clip(None)

    if mb[0]==1 and fd==1 and canvas.collidepoint(mx,my):#fierce deity mask
        screen.set_clip(canvas)
        screen.blit(fdPic,(mx-75,my-55))
        screen.set_clip(None)

    if mb[0]==1 and dk==1 and canvas.collidepoint(mx,my):#deku mask
        screen.set_clip(canvas)
        screen.blit(dekuPic,(mx-75,my-55))
        screen.set_clip(None)

    if mb[0]==1 and zr==1 and canvas.collidepoint(mx,my):#zora mask
        screen.set_clip(canvas)
        screen.blit(zoraPic,(mx-75,my-55))
        screen.set_clip(None)

    if mb[0]==1 and kid==1 and canvas.collidepoint(mx,my):#skull kid
        screen.set_clip(canvas)
        screen.blit(kidPic,(mx,my))
        screen.set_clip(None)

    if mb[0]==1 and link==1 and canvas.collidepoint(mx,my):#link
        screen.set_clip(canvas)
        screen.blit(linkPic,(mx,my))
        screen.set_clip(None)

    if mb[0]==1 and undRect.collidepoint(mx,my):
        screen.blit(und,(0,0))
        redC=1
    if mb[0]==1 and redRect.collidepoint(mx,my) and redoC==1:

        screen.blit(red,(0,0))
        redoC==0
    if mb[0]==1 and canvas.collidepoint(mx,my) and rect==1:
        screen.set_clip(canvas)
        screen.blit(cap,(0,0))
        draw.rect(screen,(c),(rmx,rmy,mx-rmx,my-rmy))
        screen.set_clip(None)
    if mb[0]==1 and canvas.collidepoint(mx,my) and unrect==1:
        screen.set_clip(canvas)
        screen.blit(cap,(0,0))
        draw.rect(screen,(c),(rmx,rmy,mx-rmx,my-rmy),size)
        screen.set_clip(None)

    if mb[1]==1:#fill the background
        draw.rect(screen,(bg),canvas)

    if mb[2]==1 and canvas.collidepoint(mx,my):#if the right mouse button is pressed
        screen.set_clip(canvas)#eraser
        draw.circle(screen,(bg),(mx,my),size)#draws a circle with the color of the background, working as an eraser
        screen.set_clip(None)






    ##print(mx,my)


    #-------------------------------------------

    display.flip()

quit()
