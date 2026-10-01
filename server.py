import http.server
import socketserver
import socket
import ssl
import os
import sys
import threading

HTTP_PORT = 8080
HTTPS_PORT = 8443

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        try:
            return socket.gethostbyname(socket.gethostname())
        except Exception:
            return '127.0.0.1'

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

socketserver.TCPServer.allow_reuse_address = True

def run_http():
    with socketserver.TCPServer(("", HTTP_PORT), CustomHandler) as httpd:
        httpd.serve_forever()

def run_https(certfile, keyfile):
    with socketserver.TCPServer(("", HTTPS_PORT), CustomHandler) as httpsd:
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(certfile=certfile, keyfile=keyfile)
        httpsd.socket = context.wrap_socket(httpsd.socket, server_side=True)
        httpsd.serve_forever()

if __name__ == '__main__':
    web_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(web_dir)

    if sys.stdout.encoding != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    local_ip = get_local_ip()
    cert_path = os.path.join(web_dir, 'server.crt')
    key_path = os.path.join(web_dir, 'server.key')
    has_ssl = os.path.exists(cert_path) and os.path.exists(key_path)

    print("=" * 65)
    print("TET PREPARATION & STRICT AI VOICE EXAMINER PLATFORM")
    print("=" * 65)
    print(f"💻 Laptop (HTTP)  : http://localhost:{HTTP_PORT}")
    if has_ssl:
        print(f"💻 Laptop (HTTPS) : https://localhost:{HTTPS_PORT}")
        print(f"📱 Phone (HTTPS)  : https://{local_ip}:{HTTPS_PORT}  [RECOMMENDED FOR PHONE MIC]")
    print(f"📱 Phone (HTTP)   : http://{local_ip}:{HTTP_PORT}")
    print("=" * 65)
    print("NOTE FOR PHONE: Mobile browsers require HTTPS for Microphone voice input.")
    print("On your phone, open https://" + f"{local_ip}:{HTTPS_PORT} and accept the certificate.")
    print("=" * 65)

    # Start HTTP in thread
    t_http = threading.Thread(target=run_http, daemon=True)
    t_http.start()

    # Start HTTPS in main thread or vice versa
    if has_ssl:
        try:
            run_https(cert_path, key_path)
        except KeyboardInterrupt:
            print("\nShutting down server.")
            sys.exit(0)
    else:
        try:
            t_http.join()
        except KeyboardInterrupt:
            print("\nShutting down server.")
            sys.exit(0)
