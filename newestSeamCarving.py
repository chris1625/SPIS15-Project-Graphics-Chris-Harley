from PIL import Image,ImageDraw


def greyscale(image):
    '''Convert image to greyscale'''
    image=Image.open(image)
    (width,height)=image.size
    for x in range( 0, width ):
        for y in range( 0, height ):
            (red, green, blue) = image.getpixel((x, y))
            # The following code standardizes RGB values according to luminence
            # Note that the same value is written to each variable
            newRed = int(.21*red+.72*green+.07*blue)
            newGreen = int(.21*red+.72*green+.07*blue)
            newBlue = int(.21*red+.72*green+.07*blue)
            image.putpixel((x, y), (newRed, newGreen, newBlue))
    image.save('greyscale1.jpg')

def energyLevel(image,widthchange):
    image=Image.open(image)
    (width,height)=image.size
    endLocation = 0
    endY = height - 1
    #Important to be used later to determine coordinates of final position
    minimum = 9999999 # Also important for later 
    '''Makes a table of the energy levels'''
    table = [[0 for y in range(height)] for x in range(width)]
    pathwaytable = [[0 for y in range(height)] for x in range(width)]
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
            john = table [b][a+1]
            if a != height - 1:
                if b != 0 and b!= width - 2:
                    table[b][a+1] = table[b][a+1] + min(table[b-1][a],table[b][a],table[b+1][a])
                    
                    if table[b][a+1] - john == table[b-1][a]:
                         pathwaytable[b][a+1] = [b - 1, a]
                    elif table[b][a+1] - john == table[b+1][a]:
                         pathwaytable[b][a+1] = [b + 1, a]
                    else:
                        pathwaytable[b][a+1] = [b , a]
                        
                elif b == 0:
                    table[b][a+1] = table[b][a+1] + min(table[b][a],table[b+1][a])
                    if table[b][a+1] - john == table[b][a]:
                         pathwaytable[b][a+1] = [b, a]
                    else: 
                         pathwaytable[b][a+1] = [b + 1, a]
                else:
                    table[b][a+1] = table[b][a+1] + min(table[b-1][a],table[b][a])
                    if table[b][a+1] - john == table[b-1][a]:
                         pathwaytable[b][a+1] = [b - 1, a]
                    else:
                         pathwaytable[b][a+1] = [b, a]
                
   # for c in range (width - 2):
       # minimum = min(table[c][height - 1],table[c+1][height - 1])
       # if min(table[c][height-1],table[c+1][height - 1]) == minimum:
           #  endLocation = c
    for u in range (widthchange):
        for c in range (width - 2):
            minimum = min(minimum,table[c][height - 1],table[c+1][height - 1])
            if table[c][height-1] == minimum:
                 endLocation = c
            elif table[c+1][height-1] == minimum:
                endLocation = c+1 
        table[endLocation][height-1] = 999999999
        minimum = 99999999
        while endY != 0: 
            image.putpixel((endLocation,endY),(255,0,0))
            endLocation,endY = (pathwaytable[endLocation][endY][0],pathwaytable[endLocation][endY][1]) 
        endY = height - 1
    image.show()
    return minimum 
    print minimum 
