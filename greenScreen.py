from PIL import Image,ImageDraw

chris=Image.open('greenscreen_chris.jpg')
(chrisWidth,chrisHeight)=chris.size

harley=Image.open('greenscreen_harley.jpg')
(harleyWidth,harleyHeight)=harley.size

def removeGreen():
    newChris=Image.new('RGB',(chrisWidth,chrisHeight))
    for x in range(chrisWidth):
        for y in range (chrisHeight):
            (red,green,blue)=chris.getpixel((x,y))
            if 130<red<200 and 140<green<220 and 60<blue<120:
                red,green,blue=255,255,255
            newChris.putpixel((x,y),(red,green,blue))
    newChris.show()

def showPixel(startx,starty,endx,endy):
    for x in range(startx,endx):
        for y in range(starty, endy):
            print chris.getpixel((x,y))
            
            
