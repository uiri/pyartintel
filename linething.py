import sys, pygame, random
pygame.init() 

#create the screen
window = pygame.display.set_mode((640, 640)) 

xcoord = random.randint(0,639)
ycoord = random.randint(0,479)

#draw a line
pygame.draw.line(window, (255, 255, 255), (xcoord, ycoord), (xcoord, ycoord), 1)
#pygame.draw.arc(window, (255, 255, 255), pygame.Rect(0,0,640,480), 0, 5)

#draw it to the screen
pygame.display.flip() 

#input handling (somewhat boilerplate code):
while True: 
   for event in pygame.event.get(): 
      if event.type == pygame.QUIT: 
         sys.exit(0)
   #xcoord = random.randint(0,640)
   #ycoord = random.randint(0,480)
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
   pygame.draw.line(window, (255,255,255), (xcoord, ycoord), (xcoord+xdiff, ycoord+ydiff), 1)
   xcoord += xdiff
   ycoord += ydiff
   pygame.display.flip()
