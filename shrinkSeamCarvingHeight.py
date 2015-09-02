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
    return image 

def shrinkEnergyLevelHeight(image,heightchange):
    image2 = Image.open(image)
    image=greyscale(image)
    endLocation = 0
    (width,height)=image.size
    endX = width - 1
    print 'Now cutting seams by height'
    print width
    print height
    finalimage = Image.new('RGB',(width,height-heightchange),0)
    #Important to be used later to determine coordinates of final position
    minimum = 9999999 # Also important for later 
    '''Makes a table of the energy levels'''
    table = [[0 for y in range(height)] for x in range(width)]
    pathwaytable = [[0 for y in range(height)] for x in range(width)]
    for y in range (height-1):
        for x in range (width-1):
            energy = 0
            color = image.getpixel((x,y))[1] 
            #if x > 0: 
                #energy = energy + abs(color - image.getpixel((x-1,y))[1])
                
            if x < height:
                energy = energy + abs(color - image.getpixel((x,y+1))[1])

            #if y > 0:
                #energy = energy + abs(color - image.getpixel((x,y-1))[1])

            if y < height:
                 energy = energy + abs(color - image.getpixel((x+1,y))[1])
            table[x][y] = energy
    print 'wubbalubba'
    for a in range (height):
        for b in range (width-1):
            john = table [b+1][a]
            if b != width - 1:
                if a != 0 and a!= height - 1:
                    table[b+1][a] = table[b+1][a] + min(table[b][a-1],table[b][a],table[b][a+1])
                    
                    if table[b+1][a] - john == table[b][a-1]:
                         pathwaytable[b+1][a] = [b, a-1]
                    elif table[b+1][a] - john == table[b][a+1]:
                         pathwaytable[b+1][a] = [b, a+1]
                    else:
                        pathwaytable[b+1][a] = [b , a]
                        
                elif a == 0:
                    table[b+1][a] = table[b+1][a] + min(table[b][a],table[b][a+1])
                    if table[b+1][a] - john == table[b][a]:
                         pathwaytable[b+1][a] = [b, a]
                    else: 
                         pathwaytable[b+1][a] = [b, a+1]
                else:
                    table[b+1][a] = table[b+1][a] + min(table[b][a-1],table[b][a])
                    if table[b+1][a] - john == table[b][a-1]:
                         pathwaytable[b+1][a] = [b, a-1]
                    else:
                         pathwaytable[b+1][a] = [b, a]
    print 'wubbadubba'
   # for c in range (width - 2):
       # minimum = min(table[c][height - 1],table[c+1][height - 1])
       # if min(table[c][height-1],table[c+1][height - 1]) == minimum:
           #  endLocation = c
    for u in range (heightchange+1):
        for c in range (height - 1):
            minimum = min(minimum,table[width - 1][c],table[width - 1][c+1])
            if table[width-1][c] == minimum:
                 endLocation = c
            elif table[width-1][c+1] == minimum:
                endLocation = c+1 
        table[width-1][endLocation] = 999999999
        minimum = 99999999
        while endX != 0:
            image.putpixel((endX,endLocation),(255,0,0))
            if endLocation == 0:
                if image.getpixel((endX-1,endLocation)) == (255,0,0) and image.getpixel((endX-1,endLocation+1)) == (255,0,0):
                    for foo in range (1,height-1):
                         if endLocation + foo > height - 1:
                             pass
                         elif endLocation + foo == height - 1:
                             if image.getpixel((endX-1,endLocation+foo)) != (255,0,0) or image.getpixel((endX-1,endLocation-1+foo)) != (255,0,0):
                                endLocation = endLocation + foo
                                break
                         elif image.getpixel((endX-1,endLocation+foo)) != (255,0,0) or image.getpixel((endX-1,endLocation-1+foo)) != (255,0,0) or image.getpixel((endX-1,endLocation+1+foo)) != (255,0,0):
                            endLocation = endLocation + foo
                            break
                         if endLocation - foo < 0:
                            pass
                         elif endLocation - foo == 0:
                            if image.getpixel((endX-1,endLocation-foo)) != (255,0,0) or image.getpixel((endX-1,endLocation+1-foo)) != (255,0,0):
                                endLocation = endLocation - foo
                                break
                         elif image.getpixel((endX-1,endLocation-foo)) != (255,0,0) or image.getpixel((endX-1,endLocation-1-foo)) != (255,0,0) or image.getpixel((endX-1,endLocation+1-foo)) != (255,0,0):
                            endLocation = endLocation - foo
                            break
                        
            elif endLocation == height-1:
                if image.getpixel((endX-1,endLocation)) == (255,0,0) and image.getpixel((endX-1,endLocation-1)) == (255,0,0):
                    for foo in range (1,height-1):
                         
                         if endLocation + foo > height - 1:
                             pass
                         elif endLocation + foo == height - 1:
                             if image.getpixel((endX-1,endLocation+foo)) != (255,0,0) or image.getpixel((endX-1,endLocation-1+foo)) != (255,0,0):
                                endLocation = endLocation + foo
                                break
                         elif image.getpixel((endX-1,endLocation+foo)) != (255,0,0) or image.getpixel((endX-1,endLocation-1+foo)) != (255,0,0) or image.getpixel((endX-1,endLocation+1+foo)) != (255,0,0):
                            endLocation = endLocation + foo
                            break
                         if endLocation - foo < 0:
                            pass
                         elif endLocation - foo == 0:
                            if image.getpixel((endX-1,endLocation-foo)) != (255,0,0) or image.getpixel((endX-1,endLocation+1-foo)) != (255,0,0):
                                endLocation = endLocation - foo
                                break
                         elif image.getpixel((endX-1,endLocation-foo)) != (255,0,0) or image.getpixel((endX-1,endLocation-1-foo)) != (255,0,0) or image.getpixel((endX-1,endLocation+1-foo)) != (255,0,0):
                            endLocation = endLocation - foo
                            break
            else:
                if image.getpixel((endX-1,endLocation)) == (255,0,0) and image.getpixel((endX-1,endLocation-1)) == (255,0,0) and image.getpixel((endX-1,endLocation+1)) == (255,0,0):
                    for foo in range (1,height-1):
                         if endLocation + foo > height - 1:
                             pass
                         elif endLocation + foo == height - 1:
                             if image.getpixel((endX-1,endLocation+foo)) != (255,0,0) or image.getpixel((endX-1,endLocation-1+foo)) != (255,0,0) :
                                endLocation = endLocation + foo
                                break
                         elif image.getpixel((endX-1,endLocation+foo)) != (255,0,0) or image.getpixel((endX-1,endLocation-1+foo)) != (255,0,0) or image.getpixel((endX-1,endLocation+1+foo)) != (255,0,0):
                            endLocation = endLocation + foo
                            break
                         if endLocation - foo < 0:
                            pass
                         elif endLocation - foo == 0:
                            if image.getpixel((endX-1,endLocation-foo)) != (255,0,0) or image.getpixel((endX-1,endLocation+1-foo)) != (255,0,0):
                                endLocation = endLocation - foo
                                break
                         elif image.getpixel((endX-1,endLocation-foo)) != (255,0,0) or image.getpixel((endX-1,endLocation-1-foo)) != (255,0,0) or image.getpixel((endX-1,endLocation+1-foo)) != (255,0,0):
                            endLocation = endLocation - foo
                            break
                        
                
            if image.getpixel((endX-1,pathwaytable[endX][endLocation][1])) == (255,0,0):
                if endLocation - (pathwaytable[endX][endLocation][1]) == 0:
                    if endLocation == 0:
                        endLocation,endX = endLocation+1,endX-1
                    elif endLocation == height - 1:
                         endLocation,endX = endLocation-1,endX-1
                    else:
                        if min(table[endX-1][endLocation-1],table[endX-1][endLocation+1]) == table[endX-1][endLocation-1] and image.getpixel((endX-1,endLocation-1)) != (255,0,0):
                             endLocation,endX = (endLocation - 1,endX-1)
                        elif image.getpixel((endX-1,endLocation+1)) != (255,0,0):
                            endLocation,endX = (endLocation+1,endX-1)
                        else:
                            endLocation,endX = (endLocation-1,endX-1)
                elif endLocation - (pathwaytable[endX][endLocation][1]) == 1:
                    if endLocation == height - 1:
                        endLocation,endX = endLocation,endX-1
                    else:
                        if min(table[endX-1][endLocation],table[endX-1][endLocation+1]) == table[endX-1][endLocation] and image.getpixel((endX-1,endLocation)) != (255,0,0):
                            endLocation,endX = endLocation,endX-1
                        elif image.getpixel((endX-1,endLocation+1)) != (255,0,0):
                            endLocation,endX = endLocation + 1,endX-1
                        else:
                            endLocation,endX = endLocation,endX-1
                else:
                    if endLocation == 0:
                         endLocation,endX = endLocation,endX-1
                    else:
                        if min(table[endX-1][endLocation],table[endX-1][endLocation-1]) == table[endX-1][endLocation] and image.getpixel((endX-1,endLocation)) != (255,0,0):
                            endLocation,endX = (endLocation,endX-1)
                        else:
                            endLocation,endX = (endLocation-1,endX-1)
            else:
                endX,endLocation = (endX-1,pathwaytable[endX][endLocation][1])
                
        image.putpixel((endX,endLocation),(255,0,0))
            
        endX = width - 1

    for e in range (width - 1):
        r2 = 0 
        for r in range (height - 1):
            if image.getpixel((e,r)) != (255,0,0):
                red,blue,green = image2.getpixel((e,r))
                finalimage.putpixel((e,r2),(red,blue,green))
                if r2 < height- heightchange - 1:
                    r2+=1
    image.save('seamsH.jpg')
    finalimage.save('output.bmp')
    finalimage.show() 