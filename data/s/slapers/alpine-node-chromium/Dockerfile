FROM mhart/alpine-node:8  
  
MAINTAINER stefan@lapers.be  
  
ADD xvfb-chromium /usr/bin/xvfb-chromium  
  
RUN set -e \  
&& echo " ------ INSTALLING PACKAGES ------" \  
&& apk -U --no-cache add udev chromium xvfb dbus ttf-freefont bash git \  
\  
&& echo " ------ SETTING UP CHROMIUM ------" \  
&& rm -f /usr/bin/chromium-browser \  
&& ln -s /usr/bin/xvfb-chromium /usr/bin/google-chrome \  
&& ln -s /usr/bin/xvfb-chromium /usr/bin/chromium-browser \  
&& chmod 755 /usr/bin/xvfb-chromium \  
\  
&& echo " ------ CLEANING UP ------" \  
&& rm -rf /var/cache/apk/*  

