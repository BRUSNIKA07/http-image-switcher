import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

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
