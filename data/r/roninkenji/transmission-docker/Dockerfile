FROM alpine:latest  
MAINTAINER roninkenji  
  
RUN mkdir -p /config /downloads /watchdir  
  
RUN apk update && apk upgrade && apk add transmission-daemon transmission-cli  
  
COPY docker_init.sh /usr/local/bin/  
  
ENTRYPOINT ["/bin/sh", "-c", "/usr/local/bin/docker_init.sh"]  
EXPOSE 9091 64000  

