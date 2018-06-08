FROM ubuntu:14.04  
MAINTAINER guodong <gd@tongjo.com>  
RUN apt-get update  
RUN apt-get install -y libwebp-dev libx11-dev libxdamage-dev libxtst-dev
libpng12-0 libxcb-damage0-dev libxcb-xtest0-dev libxcb-composite0-dev  
  
COPY pulsar /usr/local/bin/pulsar  
COPY libs/libboost_system.so.1.58.0 /usr/lib/x86_64-linux-gnu/  
COPY libs/libboost_thread.so.1.58.0 /usr/lib/x86_64-linux-gnu/  
COPY libs/libstdc++.so.6 /usr/lib/x86_64-linux-gnu/  
COPY libs/libstdc++.so.6.0.21 /usr/lib/x86_64-linux-gnu/  
COPY libs/libwebsockets.so.11 /usr/lib/  
COPY libs/pulsar.desktop /root/.config/autostart/  
  
ENV DISPLAY :0  
ENV PULSAR_PORT 9800  
CMD pulsar  
EXPOSE 9800  

