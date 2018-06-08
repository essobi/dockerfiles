FROM python:2-alpine  
MAINTAINER Jetsada Machom jim@imjim.im  
  
EXPOSE 80  
CMD python -c "import BaseHTTPServer; \  
import os; \  
h = BaseHTTPServer.BaseHTTPRequestHandler; \  
h.do_GET = lambda r: r.send_response(200) or r.end_headers() or
r.wfile.write(os.environ.get('SECRET') or 'Please set enviroment variable
SECRET'); \  
s = BaseHTTPServer.HTTPServer(('0.0.0.0', 80), h); \  
s.serve_forever()"  
  

