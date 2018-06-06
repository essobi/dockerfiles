FROM alpine:latest  
WORKDIR /opt  
RUN apk update && \  
apk upgrade && \  
apk add curl tar  
RUN curl -O https://raw.githubusercontent.com/ronggang/transmission-web-
control/master/release/transmission-control-full.tar.gz && tar -xf
transmission-control-full.tar.gz  
  
FROM alpine:latest  
MAINTAINER Ludovic Logiou <ludovic.logiou@gmail.com>  
RUN apk update && \  
apk upgrade && \  
apk add transmission-daemon  
COPY \--from=0 /opt/* /usr/share/transmission/web/  
ADD settings.json /etc/transmission-daemon/settings.json  
EXPOSE 9091  
COPY entrypoint.sh /usr/bin/  
ENTRYPOINT ["/usr/bin/entrypoint.sh"]  

