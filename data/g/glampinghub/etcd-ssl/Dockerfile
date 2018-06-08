FROM alpine:latest  
  
LABEL maintainer="José Luis Salvador Rufo <salvador.joseluis@gmail.com>"  
  
RUN touch /etc/ssl/index.txt /etc/ssl/index.txt.attr && \  
echo 01 > /etc/ssl/serial && \  
apk add --no-cache openssl  
  
COPY ./openssl.cnf /etc/ssl/  
COPY ./generate-ssl /usr/local/bin/  
  
CMD ["/usr/local/bin/generate-ssl"]  

