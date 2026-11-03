"""Static, synthetic-only demonstration. No credentials, database, or upstream calls."""
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent / 'public'
ASSETS = {('/' + p.name): p for p in ROOT.iterdir() if p.suffix in {'.html', '.css', '.js'}}
ASSETS.update({'/': ROOT / 'index.html', '/sandbox': ROOT / 'sandbox.html', '/api/sandbox': ROOT / 'fixture.json'})
TYPES = {'.html': 'text/html', '.css': 'text/css', '.js': 'application/javascript', '.json': 'application/json'}

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = urlsplit(self.path).path
        if path == '/health':
            self.reply(200, b'{"status":"ok","mode":"synthetic-only"}', 'application/json')
        elif path in ASSETS:
            p = ASSETS[path]
            self.reply(200, p.read_bytes(), TYPES[p.suffix])
        else:
            self.reply(404, b'Not found', 'text/plain')

    def do_POST(self):
        self.reply(405, b'Live operations are disabled.', 'text/plain')

    def reply(self, status, content, mime):
        self.send_response(status)
        self.send_header('Content-Type', mime + '; charset=utf-8')
        self.send_header('Content-Length', str(len(content)))
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Referrer-Policy', 'no-referrer')
        self.send_header('Cache-Control', 'no-store')
        self.send_header('Content-Security-Policy', "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'")
        self.end_headers()
        self.wfile.write(content)

if __name__ == '__main__':
    host = '0.0.0.0' if os.environ.get('RAILWAY_ENVIRONMENT_ID') else '127.0.0.1'
    ThreadingHTTPServer((host, int(os.environ.get('PORT', '8795'))), Handler).serve_forever()
