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

def shrinkEnergyLevelWidth(image,widthchange):
    image2 = Image.open(image)
    image=greyscale(image)
    endLocation = 0
    (width,height)=image.size
    endY = height - 1
    print 'Now cutting seams by width'
    print width
    print height
    finalimage = Image.new('RGB',(width - widthchange,height),0)
    #Important to be used later to determine coordinates of final position
    minimum = 9999999999999999999 # Also important for later 
    '''Makes a table of the energy levels'''
    table = [[0 for y in range(height)] for x in range(width)]
    pathwaytable = [[0 for y in range(height)] for x in range(width)]
    for x in range (width):
        for y in range (height):
            energy = 0
            color = image.getpixel((x,y))[1] 
            #if x > 0: 
                #energy = energy + abs(color - image.getpixel((x-1,y))[1])
            if x == width - 1 and y == height - 1:
               energy = energy + (abs(color - image.getpixel((x-1,y))[1]) + abs(color - image.getpixel((x,y-1))[1]))/2 
            elif x < width-1 and y<height-1:
               energy + (abs(color - image.getpixel((x+1,y))[1]) + abs(color - image.getpixel((x,y+1))[1]))/2 
            elif x == width-1:
                energy = energy + abs(color - image.getpixel((x-1,y))[1])
            else:
                energy = energy + abs(color - image.getpixel((x,y-1))[1])
            table[x][y] = energy
    
    #print 'wubbalubba'
    for a in range (height-1):
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
    #print 'wubbadubba'
   # for c in range (width - 2):
       # minimum = min(table[c][height - 1],table[c+1][height - 1])
       # if min(table[c][height-1],table[c+1][height - 1]) == minimum:
           #  endLocation = c
    for u in range (widthchange):
        minimum = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        for c in range (width):
            mintester = table[c][height-1]
            minimum = min(minimum,mintester)
            if table[c][height-1] == minimum:
                endLocation = c
        table[endLocation][height-1] = 9999999999999999999
        patherX = endLocation
        patherY = height - 1
        print minimum, table[200][200] 
        for q in range (height-1,0,-1):
            patherX,patherY = pathwaytable[patherX][q][0],q
            table[patherX][patherY] = 9999999999999999999
        print endLocation
        while endY != 0:
            image.putpixel((endLocation,endY),(255,0,0))
            if endLocation == 0:
                if image.getpixel((endLocation,endY-1)) == (255,0,0) and image.getpixel((endLocation+1,endY-1)) == (255,0,0):
                    for foo in range (1,width-1):
                         if endLocation + foo > width - 1:
                             pass
                         elif endLocation + foo == width - 1:
                             if image.getpixel((endLocation+foo,endY-1)) != (255,0,0) or image.getpixel((endLocation-1+foo,endY-1)) != (255,0,0):
                                endLocation = endLocation + foo
                                break
                         elif image.getpixel((endLocation+foo,endY-1)) != (255,0,0) or image.getpixel((endLocation-1+foo,endY-1)) != (255,0,0) or image.getpixel((endLocation+1+foo,endY-1)) != (255,0,0):
                            endLocation = endLocation + foo
                            break
                         if endLocation - foo < 0:
                            pass
                         elif endLocation - foo == 0:
                            if image.getpixel((endLocation-foo,endY-1)) != (255,0,0) or image.getpixel((endLocation+1-foo,endY-1)) != (255,0,0):
                                endLocation = endLocation - foo
                                break
                         elif image.getpixel((endLocation-foo,endY-1)) != (255,0,0) or image.getpixel((endLocation-1-foo,endY-1)) != (255,0,0) or image.getpixel((endLocation+1-foo,endY-1)) != (255,0,0):
                            endLocation = endLocation - foo
                            break
                        
            elif endLocation == width-1:
                if image.getpixel((endLocation,endY-1)) == (255,0,0) and image.getpixel((endLocation-1,endY-1)) == (255,0,0):
                    for foo in range (1,width-1):
                         
                         if endLocation + foo > width - 1:
                             pass
                         elif endLocation + foo == width - 1:
                             if image.getpixel((endLocation+foo,endY-1)) != (255,0,0) or image.getpixel((endLocation-1+foo,endY-1)) != (255,0,0):
                                endLocation = endLocation + foo
                                break
                         elif image.getpixel((endLocation+foo,endY-1)) != (255,0,0) or image.getpixel((endLocation-1+foo,endY-1)) != (255,0,0) or image.getpixel((endLocation+1+foo,endY-1)) != (255,0,0):
                            endLocation = endLocation + foo
                            break
                         if endLocation - foo < 0:
                            pass
                         elif endLocation - foo == 0:
                            if image.getpixel((endLocation-foo,endY-1)) != (255,0,0) or image.getpixel((endLocation+1-foo,endY-1)) != (255,0,0):
                                endLocation = endLocation - foo
                                break
                         elif image.getpixel((endLocation-foo,endY-1)) != (255,0,0) or image.getpixel((endLocation-1-foo,endY-1)) != (255,0,0) or image.getpixel((endLocation+1-foo,endY-1)) != (255,0,0):
                            endLocation = endLocation - foo
                            break
            else:
                if image.getpixel((endLocation,endY-1)) == (255,0,0) and image.getpixel((endLocation-1,endY-1)) == (255,0,0) and image.getpixel((endLocation+1,endY-1)) == (255,0,0):
                    for foo in range (1,width-1):
                         if endLocation + foo > width - 1:
                             pass
                         elif endLocation + foo == width - 1:
                             if image.getpixel((endLocation+foo,endY-1)) != (255,0,0) or image.getpixel((endLocation-1+foo,endY-1)) != (255,0,0) :
                                endLocation = endLocation + foo
                                break
                         elif image.getpixel((endLocation+foo,endY-1)) != (255,0,0) or image.getpixel((endLocation-1+foo,endY-1)) != (255,0,0) or image.getpixel((endLocation+1+foo,endY-1)) != (255,0,0):
                            endLocation = endLocation + foo
                            break
                         if endLocation - foo < 0:
                            pass
                         elif endLocation - foo == 0:
                            if image.getpixel((endLocation-foo,endY-1)) != (255,0,0) or image.getpixel((endLocation+1-foo,endY-1)) != (255,0,0):
                                endLocation = endLocation - foo
                                break
                         elif image.getpixel((endLocation-foo,endY-1)) != (255,0,0) or image.getpixel((endLocation-1-foo,endY-1)) != (255,0,0) or image.getpixel((endLocation+1-foo,endY-1)) != (255,0,0):
                            endLocation = endLocation - foo
                            break
                        
            if endLocation < width - 1 and endLocation > 0:
                if image.getpixel((endLocation,endY-1)) == (255,0,0) and image.getpixel((endLocation-1,endY-1)) == (255,0,0) and image.getpixel((endLocation+1,endY-1)) == (255,0,0):
                    print endLocation,endY,'ayy1'
            elif endLocation == width - 1:
                if image.getpixel((endLocation,endY-1)) == (255,0,0) and image.getpixel((endLocation-1,endY-1)) == (255,0,0):
                    print endLocation,endY,'ayy2'
            elif endLocation == 0:
                if image.getpixel((endLocation,endY-1)) == (255,0,0) and image.getpixel((endLocation+1,endY-1)) == (255,0,0):
                    print endLocation,endY,'ayy3'
                
            if image.getpixel((pathwaytable[endLocation][endY][0],endY-1)) == (255,0,0):
                if endLocation - (pathwaytable[endLocation][endY][0]) == 0:
                    if endLocation == 0:
                        endLocation,endY = endLocation+1,endY-1
                    elif endLocation == width - 1:
                         endLocation,endY = endLocation-1,endY-1
                    else:
                        if min(table[endLocation-1][endY-1],table[endLocation+1][endY-1]) == table[endLocation-1][endY-1] and image.getpixel((endLocation-1,endY-1)) != (255,0,0):
                             endLocation,endY = (endLocation - 1,endY-1)
                        elif image.getpixel((endLocation+1,endY-1)) != (255,0,0):
                            endLocation,endY = (endLocation + 1,endY-1)
                        else:
                            endLocation,endY = (endLocation - 1,endY-1)
                elif endLocation - (pathwaytable[endLocation][endY][0]) == 1:
                    if endLocation == width - 1:
                        endLocation,endY = endLocation,endY-1
                    else:
                        if min(table[endLocation][endY-1],table[endLocation+1][endY-1]) == table[endLocation][endY-1] and image.getpixel((endLocation,endY-1)) != (255,0,0):
                            endLocation,endY = endLocation,endY-1
                        elif image.getpixel((endLocation+1,endY-1)) != (255,0,0):
                            endLocation,endY = endLocation + 1,endY-1
                        else:
                            endLocation,endY = endLocation,endY-1
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
                
        image.putpixel((endLocation,endY),(255,0,0))
        for a in range (height-1):
                for b in range (width):
                    if table[b][a] == 9999999999999999999:
                        break
                    
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
            
        endY = height - 1

    for r in range (height - 1):
        e2 = 0 
        for e in range (width - 1):
            if r > height-1 or r < 0:
                    print r, 'height issue'        
            if e2 > width - widthchange -1 or e2 < 0:
                    print e2,'width issue', width, height 
                
            if image.getpixel((e,r)) != (255,0,0):
                red,blue,green = image2.getpixel((e,r))
                finalimage.putpixel((e2,r),(red,blue,green))
                if e2 < width - widthchange -1:
                    e2+=1
    image.show()
    finalimage.show()


