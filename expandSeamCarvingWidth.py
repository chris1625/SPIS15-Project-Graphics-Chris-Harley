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

def expandEnergyLevelWidth(image,widthchange):
    image2 = Image.open(image)
    image=greyscale(image)
    endLocation = 0
    (width,height)=image.size
    endY = height - 1
    print 'Now cutting seams by width'
    print width
    print height
    finalimage = Image.new('RGB',(width + widthchange,height),0)
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
    print 'wubbalubba'
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
    print 'wubbadubba'
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
            
        endY = height - 1

    for r in range (height - 1):
        e2 = 0 
        for e in range (width - 1):
            
                
            if image.getpixel((e,r)) != (255,0,0):
                red,blue,green = image2.getpixel((e,r))
                finalimage.putpixel((e2,r),(red,blue,green))
                if e2 < width + widthchange -1:
                    e2+=1
            else:
                red,blue,green = image2.getpixel((e,r))
                if e2 < width + widthchange - 1:
                    red2,blue2,green2 = image2.getpixel((e+1,r))
                if e2 > 0: 
                    red3,blue3,green3 = image2.getpixel((e-1,r))
                finalimage.putpixel((e2,r),(red,blue,green))
                if 0 <e2 < width + widthchange-1:
                    red,blue,green = (red2+red3)/2,(blue2+blue3)/2,(green2+green3)/2
                elif e2 == 0:
                    red,blue,green = red2,blue2,green2
                else:
                    red,blue,green = red3,blue3,green3
                finalimage.putpixel((e2,r),(red,blue,green))
                e2+=2
    image.save('seamsW.jpg')
    finalimage.save('output.bmp')
