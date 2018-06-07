FROM alpine  
  
RUN echo $'#!/bin/sh\n\  
while true; \  
do (echo -e "HTTP/1.1 200 OK\\\r\\\n"; echo -e "$(printenv)") | nc -lp 8080; \  
done' > /usr/local/bin/env-server && chmod +x /usr/local/bin/env-server  
  
EXPOSE 8080  
ENTRYPOINT ["/usr/local/bin/env-server"]  

