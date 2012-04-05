import sys, pygame, random
pygame.init() 

#create the screen
winw = 1000
winh = 500
window = pygame.display.set_mode((winw, winh)) 

xcoord = random.randint(0,winw)
ycoord = random.randint(0,winh)
width = 1
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

#draw a line
#for ycoord in xrange(winh):
#   for xcoord in xrange(winw):
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

#pygame.draw.arc(window, color, pygame.Rect(0,0,winw,winh), 0, width)
pygame.display.flip() 

while 1:
   for event in pygame.event.get(): 
      if event.type == pygame.QUIT: 
         sys.exit(0)
   #xcoord = random.randint(0,winw)
   #ycoord = random.randint(0,winh)
   #color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
   newcolor = []
   for component in color:
      toadd = component + random.randint(-10, 10)
      if toadd > 255:
         toadd = 255
      if toadd < 0:
         toadd = 0
      newcolor.append(toadd)
   color = tuple(newcolor)
   xdiff = random.randint(-300, 300)
   ydiff = random.randint(-300, 300)
   width = random.randint(1,10)
   if xcoord+xdiff > winw:
      xdiff = winw - xcoord
   if ycoord+ydiff > winh:
      ydiff = winh - ycoord
   if ycoord+ydiff < 0:
      ydiff = 0 - ycoord
   if xcoord+xdiff < 0:
      xdiff = 0 - xcoord
   pygame.draw.line(window, color, (xcoord+xdiff, ycoord), (xcoord+xdiff, ycoord+ydiff), width)
   xcoord += xdiff
   ycoord += ydiff
   pygame.display.flip()
   pygame.gfxdraw.bezier(window, ((40,40),(400,400)), ((120,120)), color)
   pygame.display.flip()
