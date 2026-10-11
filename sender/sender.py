import sys
import pygame
import requests

ip = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"

pygame.init()
screen = pygame.display.set_mode((300, 200))
pygame.display.set_caption("sender")
font = pygame.font.SysFont(None, 40)
button = pygame.Rect(75, 70, 150, 60)
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and button.collidepoint(event.pos):
            try:
                requests.get(f"http://{ip}:8000/next", timeout=2)
            except requests.RequestException:
                print("receiver not available")
    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (70, 130, 200), button)
    text = font.render("Next", True, (255, 255, 255))
    screen.blit(text, text.get_rect(center=button.center))
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
