FROM ubuntu:14.04  
MAINTAINER guodong <gd@tongjo.com>  
RUN apt-get update  
RUN apt-get install -y libwebp-dev libx11-dev libxdamage-dev libxtst-dev
libpng12-0  
COPY build/pulsar /usr/local/bin/pulsar  
COPY libwebsockets.so.11 /usr/lib/  
COPY pulsar.desktop /root/.config/autostart/  
ENV DISPLAY :0  
ENV PULSAR_PORT 5678  
CMD pulsar  
EXPOSE 5678

