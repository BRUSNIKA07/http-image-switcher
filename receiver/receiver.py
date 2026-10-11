import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
import pygame

folder = os.path.join(os.path.dirname(__file__), "..", "images")
images = [f for f in sorted(os.listdir(folder)) if f.lower().endswith((".png", ".jpg"))]
current = 0


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        global current
        if self.path == "/next":
            if images:
                current = (current + 1) % len(images)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"ok")
        else:
            self.send_response(404)
            self.end_headers()


server = HTTPServer(("0.0.0.0", 8000), Handler)
threading.Thread(target=server.serve_forever, daemon=True).start()

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("receiver")
font = pygame.font.SysFont(None, 48)
pictures = [pygame.image.load(os.path.join(folder, f)) for f in images]
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    if pictures:
        screen.blit(pygame.transform.scale(pictures[current], (800, 600)), (0, 0))
    else:
        text = font.render("no images", True, (255, 255, 255))
        screen.blit(text, text.get_rect(center=(400, 300)))
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
