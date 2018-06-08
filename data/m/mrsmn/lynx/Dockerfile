FROM alpine:latest  
MAINTAINER Martin Simon <me@martinsimon.me>  
  
RUN \  
apk add --update \  
lynx && \  
rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["lynx"]

