import sys, pygame, random
pygame.init() 

#create the screen
window = pygame.display.set_mode((640, 640)) 

xcoord = random.randint(0,640)
ycoord = random.randint(0,640)
width = 1
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

#draw a line
#for ycoord in xrange(640):
#   for xcoord in xrange(640):
#      pygame.draw.line(window, color, (xcoord, ycoord), (xcoord, ycoord), width)
#      color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
"""      newcolor = []
      for component in color:
         toadd = component + random.randint(-100, 100)
         if toadd > 255:
            toadd = 255
         if toadd < 0:
            toadd = 0
         newcolor.append(toadd)
      color = tuple(newcolor)"""

#pygame.draw.arc(window, color, pygame.Rect(0,0,640,480), 0, width)
pygame.display.flip() 

while 1:
   for event in pygame.event.get(): 
      if event.type == pygame.QUIT: 
         sys.exit(0)
   #xcoord = random.randint(0,640)
   #ycoord = random.randint(0,640)
   #color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
   newcolor = []
   for component in color:
      toadd = component + random.randint(-100, 100)
      if toadd > 255:
         toadd = 255
      if toadd < 0:
         toadd = 0
      newcolor.append(toadd)
   color = tuple(newcolor)
   xdiff = random.randint(-200, 200)
   ydiff = random.randint(-200, 200)
   if xcoord+xdiff > 640:
      xdiff = 640 - xcoord
   if ycoord+ydiff > 640:
      ydiff = 640 - ycoord
   if ycoord+ydiff < 0:
      ydiff = 0 - ycoord
   if xcoord+xdiff < 0:
      xdiff = 0 - xcoord
   pygame.draw.line(window, color, (xcoord, ycoord), (xcoord+xdiff, ycoord+ydiff), width)
   xcoord += xdiff
   ycoord += ydiff
   pygame.display.flip()
