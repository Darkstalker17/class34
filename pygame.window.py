'''Pygame Window
Outline:
Write a Python program to create an empty Pygame window.'''
import pygame
pygame.init()
'''screen = pygame.display.set_mode((1000, 1000))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip()'''

'''
Add Image to the Screen
Outline:
Write a program to create a Pygame window with an image in it. Use white colour as background RGB (255, 255, 255). You can use any image of your choice.
'''
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Adding image and background image')
background_image = pygame.transform.scale(
    pygame.image.load("backgruons.jpg").convert(),
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

penguin_image = pygame.transform.scale(
    pygame.image.load("penguin.jpg").convert_alpha(), (200, 200))
penguin_rect = penguin_image.get_rect(center=(SCREEN_WIDTH // 2,
                                              SCREEN_HEIGHT // 2 - 30))
text = pygame.font.Font(None, 36).render("Hello Dakshith", True,
                                         pygame.Color("Yellow"))
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110))
def game_loop():
  clock = pygame.time.Clock()
  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    display_surface.blit(background_image, (0, 0))
    display_surface.blit(penguin_image, penguin_rect)
    display_surface.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(30)

  pygame.quit()


if __name__ == '__main__':
  game_loop()


