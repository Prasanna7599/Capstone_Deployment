from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import socket
from datetime import datetime, timezone
class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            response = {
                "status": "healthy",
                "service": "sre-practice-app",
                "hostname": socket.gethostname(),
                "timestamp": datetime.now(timezone.utc).isoformat()
            }
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            html = """<!doctype html>
<html>
<head><title>SRE Practice App</title></head>
<body>
  <h1>SRE Practice App</h1>
  <p>Application deployed successfully!</p>
  <p>Try the <a href="/health">health endpoint</a>.</p>
</body>
</html>"""
            self.wfile.write(html.encode())
    def log_message(self, format, *args):
        print(f"{self.address_string()} - {format % args}", flush=True)
server = HTTPServer(("0.0.0.0", 8000), AppHandler)
print("SRE Practice App listening on port 8000", flush=True)
server.serve_forever()
