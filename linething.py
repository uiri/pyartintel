import sys, pygame, random
pygame.init() 

#create the screen
paint = True
winw = 640
winh = 480
window = pygame.display.set_mode((winw, winh)) 
alreadypainted = []

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
   if paint:
      #xcoord = random.randint(0,winw)
      #ycoord = random.randint(0,winh)
      #color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
      newcolor = []
      for component in color:
         toadd = component + random.randint(-10, 10)
         if toadd > 255:
            toadd = 255
         if toadd < 100:
            toadd = 100
         newcolor.append(toadd)
      color = tuple(newcolor)
      xdiff = random.randint(-10, 10)
      ydiff = random.randint(-10, 10)
      width = random.randint(1,20)
      if xcoord+xdiff > winw:
         xdiff = winw - xcoord
      if ycoord+ydiff > winh:
         ydiff = winh - ycoord
      if ycoord+ydiff < 0:
         ydiff = 0 - ycoord
      if xcoord+xdiff < 0:
         xdiff = 0 - xcoord
      #pygame.draw.line(window, color, (xcoord+xdiff, ycoord), (xcoord+xdiff, ycoord+ydiff), width)
      if xcoord == winw:
         xcoord = 0
      if ycoord == winh:
         ycoord = 0
      try:
         while window.get_at((xcoord, ycoord)) != (0,0,0):
            if random.choice(["x", "y"]) == "x":
               if random.choice(["+", "-"]) == "+":
                  xcoord += 1
                  if xcoord > winw:
                     xcoord = 0
               else:
                  xcoord -= 1
                  if xcoord < 0:
                     xcoord = winw - 1
            else:
               if random.choice(["+", "-"]) == "+":
                  ycoord += 1
                  if ycoord > winh:
                     ycoord = 0
               else:
                  ycoord -= 1
                  if ycoord < 0:
                     ycoord = winh - 1
         pygame.draw.circle(window, color, (xcoord, ycoord), width)
         xcoord += xdiff
         ycoord += ydiff
         alreadypainted.append((xcoord, ycoord))
         pygame.display.flip()
         if len(alreadypainted) == winh*winw:
            paint = False
      except:
         xcoord = random.randint(0, winw)
         ycoord = random.randint(0, winh)
