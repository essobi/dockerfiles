FROM alpine:3.4  
MAINTAINER Matt Graham <gadgetmg@gmail.com>  
  
ENV DOCKERIZE_VERSION v0.2.0  
RUN apk --no-cache add ca-certificates transmission-daemon wget && \  
wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz && \  
tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz &&
\  
rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz && \  
apk --no-cache del wget  
  
COPY settings.tmpl /transmission/settings.tmpl  
  
VOLUME ["/data/downloads"]  
VOLUME ["/transmission/torrents"]  
VOLUME ["/transmission/resume"]  
VOLUME ["/transmission/blocklist"]  
  
EXPOSE 9091  
ENTRYPOINT ["dockerize", \  
"-template", "/transmission/settings.tmpl:/transmission/settings.json", \  
"transmission-daemon", "-g", "/transmission", "-f"]  

