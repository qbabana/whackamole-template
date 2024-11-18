import pygame
import random

#setting up my grid
vertical_lines = 20
horizontal_lines = 16
square_size = 32

#function to draw my grid
#create a loop to draw the rest of the line
def draw_grid(screen):
    for x in range(0, vertical_lines * square_size, square_size):
        pygame.draw.line(screen, "dark blue", (x, 0), (x, 512))
    for y in range (0, horizontal_lines * square_size, square_size):
        pygame.draw.line(screen, "dark blue", (0, y), (640, y))

def main():
   try:
       pygame.init()
       # You can draw the mole with this snippet:
       # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
       mole_image = pygame.image.load("mole.png")
       screen = pygame.display.set_mode((640, 512))
       clock = pygame.time.Clock()
       running = True

       #starts the mole position off in the top left corner
       mole_x = 0
       mole_y = 0

       while running:
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   running = False
               #mouse click position
               elif event.type == pygame.MOUSEBUTTONDOWN:
                   click_x, click_y = event.pos
                   print(event.pos)

                   #if the mouse click is within the square of the mole, move the mole to a new random position
                   #checks if the click of the x and y coordinate is within the square the mole is in
                   #Incremented the range by 32 to check if the mole is within that square
                   if mole_x <= click_x < mole_x + square_size and mole_y <= click_y < mole_y + square_size:
                       print(event.pos)
                       mole_x = random.randrange(0, vertical_lines) * square_size
                       mole_y = random.randrange(0, horizontal_lines) * square_size
               #take event position and check if it matches with the mole
               #take account if the mole is in that range


           screen.fill((213, 247, 242))
           draw_grid(screen)
           screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))
           pygame.display.flip()
           clock.tick(60)
   finally:
       pygame.quit()




if __name__ == "__main__":
   main()
