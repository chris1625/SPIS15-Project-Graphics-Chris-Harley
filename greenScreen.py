from PIL import Image,ImageDraw

chris=Image.open('greenscreen_chris.jpg')
(chrisWidth,chrisHeight)=chris.size

harley=Image.open('greenscreen_harley.jpg')
(harleyWidth,harleyHeight)=harley.size

def removeGreen():
    (Gred,Ggreen,Gblue)=chris.getpixel((1,1))
    newHarley=Image.new('RGB',(harleyWidth,harleyHeight))
    for x in range(harleyWidth):
        for y in range (harleyHeight):
            (red,green,blue)=harley.getpixel((x,y))
            total=float(red+green+blue)
#            if 200<=red<= and 0.39<=float(green/total)<=0.44 and 0.18<=float(blue/total)<=0.22:
            if 200<=red<=255 and 215<=green<=255 and 110<=blue<=167:
                red,green,blue=255,255,255
            newHarley.putpixel((x,y),(red,green,blue))
    newHarley.show()

def showPixel(startx,starty,endx,endy):
    minRed=255
    maxRed=0
    minGreen=255
    maxGreen=0
    minBlue=255
    maxBlue=0
    for x in range(startx,endx):
        for y in range(starty, endy):
            (red,green,blue)=harley.getpixel((x,y))
            minRed=min(minRed,red)
            maxRed=max(maxRed,red)
            minGreen=min(minGreen,green)
            maxGreen=max(maxGreen,green)
            minBlue=min(minBlue,blue)
            maxBlue=max(maxBlue,blue)
    print minRed,maxRed,minGreen,maxGreen,minBlue,maxBlue
            
