# DESCRIPTION: Xfce4 desktop on Alpine Linux  
# AUTHOR: rookiepeng (https://zpeng.me)  
FROM alpine  
MAINTAINER rookiepeng  
  
RUN apk add --no-cache --update \  
sudo \  
xfce4 \  
gvfs \  
gnome-icon-theme  
  
RUN adduser -D -h /home/alpine -s /bin/sh alpine  
RUN echo "alpine:alpine" | chpasswd  
RUN echo '%alpine ALL=(ALL) ALL' >> /etc/sudoers  
  
USER alpine  
  
#ENV HOME /home/alpine  
ENTRYPOINT [ "startxfce4" ]

