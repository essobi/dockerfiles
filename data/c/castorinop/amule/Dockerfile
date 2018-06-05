FROM multiarch/alpine:x86_64-edge  
  
RUN cat /etc/apk/repositories| sed 's@main@testing@g' > /testing && cat
testing >> /etc/apk/repositories  
  
RUN apk add amule --update  
  
# volumes and ports  
VOLUME /config /downloads  
EXPOSE 4711/tcp 4712/tcp 4672/udp 4665/udp 4662/tcp 4661/tcp  
  
ENTRYPOINT /usr/bin/amuled  
CMD -c /config  
  

