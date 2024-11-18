import pygame
import random

#make a comment
#random.randrange(low, high)
#move the mole in increments of 32

def main():
   try:
       pygame.init()
       # You can draw the mole with this snippet:
       # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
       mole_image = pygame.image.load("mole.png")
       screen = pygame.display.set_mode((640, 512))
       clock = pygame.time.Clock()
       running = True
       while running:
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   running = False
               elif event.type == pygame.MOUSEBUTTONDOWN:
                   print(event.pos)


                   #take event position and check if it matches with the mole
                   #take account if the mole is in that range


           screen.fill((213, 247, 242))
           pygame.draw.line(screen, "dark blue", (32, 0), (32, 512))


           #create a loop to draw the rest of the line


           screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
           pygame.display.flip()
           clock.tick(60)
   finally:
       pygame.quit()




if __name__ == "__main__":
   main()

