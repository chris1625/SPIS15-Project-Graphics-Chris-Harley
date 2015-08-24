from PIL import Image,ImageDraw


def greyscale(image):
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

def energyLevel(image):
    image=Image.open(image)
    (width,height)=image.size

    '''Makes a table of the energy levels'''
    table = [[0 for y in range(height)] for x in range(width)] 
    for x in range (width-1):
        for y in range (height-1):
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

    for a in range (height- 1):
        for b in range (width - 1):
            if a != height - 1:
                if b != 0 and b!= width - 2:
                    table[b][a-1] = table[b][a-1] + min(table[b-1][a],table[b][a],table[b+1][a])
                elif b == 0:
                    table[b][a-1] = table[b][a-1] + min(table[b][a],table[b+1][a])
                else:
                    table[b][a-1] = table[b][a-1] + min(table[b-1][a],table[b][a])
        

    for c in range (width - 2):
        minimum = min(table[c][height - 2],table[c+1][height - 2])
        
    return minimum 
    print minimum 

    
