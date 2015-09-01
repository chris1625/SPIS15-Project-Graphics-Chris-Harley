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
    print height
    print width
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
        for b in range (width):
            john = table [b][a+1]
            if a != height - 1:
                if b != 0 and b!= width - 1:
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
    for u in range (widthchange+1):
        for c in range (width - 1):
            minimum = min(minimum,table[c][height - 1],table[c+1][height - 1])
            if table[c][height-1] == minimum:
                 endLocation = c
            elif table[c+1][height-1] == minimum:
                endLocation = c+1 
        table[endLocation][height-1] = 999999999
        minimum = 99999999
        while endY != 0:
            image.putpixel((endLocation,endY),(255,0,0))
            red,blue,green = image.getpixel((pathwaytable[endLocation][endY][0],endY-1))
            minLocation = endLocation
            for foo in range (width-1):
                #print foo, endLocation + foo,endLocation - foo
                if minLocation == width - 1 and endY > 0:
                    if image.getpixel((minLocation-1,endY-1)) != (255,0,0) or image.getpixel((minLocation,endY-1)) != (255,0,0):
                        break
                    if image.getpixel((minLocation-1,endY-1)) == (255,0,0) and image.getpixel((minLocation,endY-1)) == (255,0,0):
                        minLocation = endLocation - foo
                                
                    
                elif endLocation == 0 and endY > 0:
                    if image.getpixel((minLocation,endY-1)) != (255,0,0) or image.getpixel((minLocation+1,endY-1)) != (255,0,0):
                        break
                    if  image.getpixel((minLocation,endY-1)) == (255,0,0) and image.getpixel((minLocation+1,endY-1)) == (255,0,0):
                        minLocation = endLocation+foo
                                
                   
                elif endY > 0:
                      if image.getpixel((minLocation-1,endY-1)) != (255,0,0) or image.getpixel((minLocation,endY-1)) != (255,0,0) or image.getpixel((minLocation+1,endY-1)) != (255,0,0):
                        break
                      if image.getpixel((minLocation-1,endY-1)) == (255,0,0) and image.getpixel((minLocation,endY-1)) == (255,0,0) and image.getpixel((minLocation+1,endY-1)) == (255,0,0):
                            if endLocation - foo < 0:
                                minLocation = foo + endLocation
                            elif endLocation + foo > width - 1:
                                minLocation = endLocation - foo
                            elif min(table[endLocation+foo][endY-1],table[endLocation-foo][endY-1]) == table[endLocation-foo-1][endY-1]:
                                minLocation = endLocation - foo
                            else:
                                minLocation = endLocation + foo
                       
            
            endLocation = minLocation
           
            red,blue,green = image.getpixel((pathwaytable[endLocation][endY][0],endY-1))
            if red == 255 and blue == 0 and green == 0:
                if endLocation - (pathwaytable[endLocation][endY][0]) == 0:
                    if endLocation == 0:
                        endLocation,endY = endLocation+1,endY-1
                    elif endLocation == width - 1:
                         endLocation,endY = endLocation-1,endY-1
                    else:
                        if min(table[endLocation-1][endY-1],table[endLocation+1][endY-1]) == table[endLocation-1][endY-1] and image.getpixel((endLocation-1,endY-1)) != (255,0,0):
                             endLocation,endY = (endLocation - 1,endY-1)
                        else:
                            endLocation,endY = (endLocation + 1,endY-1)
                elif endLocation - (pathwaytable[endLocation][endY][0]) == 1:
                    if endLocation == width - 1:
                        endLocation,endY = endLocation,endY-1
                    else:
                        if min(table[endLocation][endY-1],table[endLocation+1][endY-1]) == table[endLocation][endY-1] and image.getpixel((endLocation-1,endY-1)) != (255,0,0):
                            endLocation,endY = endLocation,endY-1
                        else:
                            endLocation,endY = endLocation - 1,endY-1
                else:
                    if endLocation == 0:
                         endLocation,endY = endLocation,endY-1
                    else:
                        if min(table[endLocation][endY-1],table[endLocation-1][endY-1]) == table[endLocation][endY-1] and image.getpixel((endLocation,endY-1)) != (255,0,0):
                            endLocation,endY = (endLocation,endY-1)
                        else:
                            endLocation,endY = (endLocation-1,endY-1)
            else:
                endLocation,endY = (pathwaytable[endLocation][endY][0],endY-1)
            
        endY = height - 1
    image.save('pls.bmp')
    image.show() 
     