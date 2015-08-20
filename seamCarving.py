from PIL import Image,ImageDraw

image=Image.open('greyscale.jpg')
(width,height)=image.size

def greyscale():
    '''Convert image to greyscale'''
    for x in range( 0, width ):
        for y in range( 0, height ):
            (red, green, blue) = image.getpixel((x, y))
            # The following code standardizes RGB values according to luminence
            # Note that the same value is written to each variable
            newRed = int(.21*red+.72*green+.07*blue)
            newGreen = int(.21*red+.72*green+.07*blue)
            newBlue = int(.21*red+.72*green+.07*blue)
            image.putpixel((x, y), (newRed, newGreen, newBlue))
    image.save('greyscale.jpg')

def energyLevel():
    '''Makes a table of the energy levels'''
    table = [[0 for y in range(height-1)] for x in range(width-1)] 
    for x in range (100):
        for y in range (100):
            energy = 0
            color = image.getpixel((x,y))[1] 
            #if x > 0: 
                #energy = energy + abs(color - image.getpixel((x-1,y))[1])
                
            if x < width:
                energy = energy + abs(color - image.getpixel((x+1,y))[1])

            #if y > 0:
                #energy = energy + abs(color - image.getpixel((x,y-1))[1])

            if y < width:
                 energy = energy + abs(color - image.getpixel((x,y+1))[1])
            table[x][y] = energy 
    print table 
