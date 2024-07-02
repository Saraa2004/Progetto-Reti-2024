# Progetto Programmazione di Reti 2024, traccia 2

import sys, signal
import http.server
import socketserver

if sys.argv[1:]:
    ip_address = sys.argv[1]    
else:
    ip_address = '127.0.0.1'
    
if sys.argv[2:]:
    port = int(sys.argv[2])
else:
    port = 8080
 
server = socketserver.ThreadingTCPServer((ip_address, port), http.server.SimpleHTTPRequestHandler)

server.daemon_threads = True

server.allow_reuse_address = True

def signal_handler(signal, frame):
    print('Exiting http server (Ctrl + C pressed)')
    try:
        if(server):
            server.server_close()
    finally:
        sys.exit(0)
        
signal.signal(signal.SIGINT, signal_handler)

try:
    while True:
        print('Server HTTP')
        print('Indirizzo IP:', ip_address)
        print('Port:', port)
        print('Per terminare premere Ctrl + C')
        server.serve_forever()
except KeyboardInterrupt:
    pass

server.server_close()