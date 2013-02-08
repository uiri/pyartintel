import sys, pygame, random, copy
pygame.init() 

#create the screen
paint = True
winw = 1000
winh = 500
window = pygame.display.set_mode((winw, winh)) 
alreadypainted = []
pallette = []
directions = ["up", "right", "down", "left"]

strokecount = 0
colourstrokecount = 0
oldcolourstrokecount = 0
oldoldcolourstrokecount = 0
oldcolourstrokecountcount = 0
xcoord = random.randint(int(winw*0.1),int(winw*0.9))
ycoord = random.randint(int(winh*0.1),int(winh*0.9))
width = 1
widthmax = 20
color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
basecolor = copy.copy(color)

pygame.display.flip() 

while 1:
   for event in pygame.event.get(): 
      if event.type == pygame.QUIT: 
         sys.exit(0)
   if paint:
      # random coords and colour each time
      #xcoord = random.randint(0,winw)
      #ycoord = random.randint(0,winh)
      #color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
      newcolor = []
      for i in xrange(3):
         toadd = basecolor[i] + random.randint(-10, 10)
         if toadd > 255:
            toadd = 255
         if toadd < 100:
            toadd = 100
         newcolor.append(toadd)
      color = tuple(newcolor)
      width = random.randint(1,widthmax)
      """xdiff = random.randint(-10, 10)
      ydiff = random.randint(-10, 10)
      if xcoord+xdiff > winw:
         xdiff = winw - xcoord
      if ycoord+ydiff > winh:
         ydiff = winh - ycoord
      if ycoord+ydiff < 0:
         ydiff = 0 - ycoord
      if xcoord+xdiff < 0:
         xdiff = 0 - xcoord"""
      #pygame.draw.line(window, color, (xcoord+xdiff, ycoord), (xcoord+xdiff, ycoord+ydiff), width)
      if xcoord == winw:
         xcoord = 0
      if ycoord == winh:
         ycoord = 0
      try:
         count = 1
         if strokecount > 3:
            strokecount = 0
            xcoord = newxcoord
            ycoord = newycoord
         newxcoord = copy.copy(xcoord)
         newycoord = copy.copy(ycoord)
         rightunchecked = False
         leftunchecked = False
         upunchecked = False
         downunchecked = False
         while window.get_at((newxcoord, newycoord)) != (0,0,0):
            direct = random.choice([(xcoord+count,ycoord), (xcoord, ycoord+count), (xcoord-count, ycoord), (xcoord, ycoord-count)])
            if window.get_at(direct) == (0,0,0):
               if direct[0] == xcoord:
                  if direct[1] < ycoord:
                     newycoord -= count
                  else:
                     newycoord += count
               else:
                  if direct[0] < xcoord:
                     newxcoord -= count
                  else:
                     newxcoord += count
            if direct == (xcoord+count, ycoord):
               rightunchecked = True
            if direct == (xcoord, ycoord+count):
               downunchecked = True
            if direct == (xcoord-count, ycoord):
               leftunchecked = True
            if direct == (xcoord, ycoord-count):
               upunchecked = True
            if upunchecked and downunchecked and leftunchecked and rightunchecked:
               count += 1
         pygame.draw.circle(window, color, (newxcoord, newycoord), width)
         strokecount += 1
         colourstrokecount += 1
         #xcoord += xdiff
         #ycoord += ydiff
         alreadypainted.append((xcoord, ycoord))
         pygame.display.flip()
         if len(alreadypainted) == winh*winw:
            paint = False
      except:
         if colourstrokecount == oldcolourstrokecount and colourstrokecount != oldoldcolourstrokecount:
            oldcolourstrokecountcount += 1
         if basecolor not in pallette:
            pallette.append(basecolor)
         if oldcolourstrokecountcount > 10:
            for i in xrange(len(pallette)):
               print i, pallette[i]
            paint = False
            #basecolorseed = random.randint(75,180)
            #basecolor = (basecolorseed, basecolorseed, basecolorseed)
            basecolor = (random.randint(75, 180), random.randint(75, 180), random.randint(75, 180))
            tempwindow = window.copy()
            tempwindow.set_colorkey((0,0,0))
            window.fill(basecolor)
            pygame.display.flip()
            window.blit(tempwindow, (0,0))
            pygame.display.flip()
         xcoord = random.randint(int(winw*0.1),int(winw*0.9))
         ycoord = random.randint(int(winh*0.1),int(winh*0.9))
         oldoldcolourstrokecount = oldcolourstrokecount
         oldcolourstrokecount = colourstrokecount
         if colourstrokecount > int(winw*winh*0.075)/(widthmax**1.5):
            #basecolorseed = random.randint(100, 255)
            #basecolor = (basecolorseed, basecolorseed, basecolorseed)
            basecolor = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
            colourstrokecount = 0
