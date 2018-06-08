FROM alpine:latest  
  
MAINTAINER Pavel Evstigneev <pavel.evst@gmail.com>  
  
RUN \  
# Install firefox and xvfb  
apk update && apk upgrade && \  
apk add xvfb bash firefox-esr dbus ttf-freefont fontconfig python curl && \  
rm -rf /var/cache/apk/*  
  
RUN \  
# Create firefox + xvfb runner  
mv /usr/bin/firefox /usr/bin/firefox-origin && \  
echo $'#!/usr/bin/env sh\n\  
Xvfb :0 -screen 0 1344x750x24 -ac +extension GLX +render -noreset & \n\  
DISPLAY=:0.0 firefox-origin $@ \n\  
killall Xvfb' > /usr/bin/firefox && \  
chmod +x /usr/bin/firefox  
# Install slimerjs  
#COPY slimerjs /usr/local/slimerjs  
RUN curl -L -o /tmp/slimerjs.zip
https://github.com/laurentj/slimerjs/releases/download/0.10.3/slimerjs-0.10.3.zip
&& \  
mkdir /opt && \  
unzip /tmp/slimerjs.zip -d /opt && \  
mv /opt/slimerjs-0.10.3 /opt/slimerjs && \  
ln -s /opt/slimerjs/slimerjs /usr/local/bin/slimerjs && \  
rm -f /tmp/slimerjs.zip  
# Install casperjs  
RUN curl -L -o /tmp/casperjs.zip
https://github.com/n1k0/casperjs/archive/master.zip && \  
unzip /tmp/casperjs.zip -d /opt && \  
mv /opt/casperjs-master /opt/casperjs && \  
ln -s /opt/casperjs/bin/casperjs /usr/local/bin/casperjs && \  
rm -f /tmp/casperjs.zip

