FROM alpine:3.3  
MAINTAINER Brad Pinter <brad.pinter@gmail.com>  
  
ENV GOSU_VERSION 1.7  
RUN apk update && \  
apk add --no-cache --update-cache curl bash && \  
curl -o /usr/local/bin/gosu -L
https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-amd64 && \  
chmod +x /usr/local/bin/gosu && \  
rm -rf /var/cache/apk/* /usr/local/src/*  
  
CMD []  

