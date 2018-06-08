# DESCRIPTION: GIMP on Alpine Linux  
# AUTHOR: rookiepeng (https://zpeng.me)  
FROM alpine  
MAINTAINER rookiepeng  
  
RUN apk add --no-cache --update \  
sudo \  
gimp \  
ghostscript-fonts \  
dbus-x11  
  
RUN adduser -D -h /home/alpine -s /bin/sh alpine  
RUN echo "alpine:alpine" | chpasswd  
RUN echo '%alpine ALL=(ALL) ALL' >> /etc/sudoers  
  
USER alpine  
  
#ENV HOME /home/alpine  
ENTRYPOINT [ "gimp" ]

