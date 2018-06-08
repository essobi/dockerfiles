  
FROM haproxy  
  
COPY ./errors/ /usr/local/etc/haproxy/errors/  
COPY ./*.lua /usr/local/etc/haproxy/.  
  
RUN mkdir /jail  
  
EXPOSE 80 443 54321  

