FROM ubuntu:16.04  
  
USER root  
  
  
RUN apt-get update \  
&& apt-get install -y curl \  
&& curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& apt-get install -y nodejs \  
&& mkdir ~/automation \  
&& cd ~/automation \  
&& npm init -f \  
&& npm install nightmare --save \  
&& cd node_modules/nightmare \  
&& npm link  
  
  
  
RUN apt-get install -y xvfb \  
x11-xkb-utils \  
xfonts-100dpi \  
xfonts-75dpi \  
xfonts-scalable \  
xfonts-cyrillic \  
x11-apps \  
clang \  
libdbus-1-dev \  
libgtk2.0-dev \  
libnotify-dev \  
libgnome-keyring-dev \  
libgconf2-dev \  
libasound2-dev \  
libcap-dev \  
libcups2-dev \  
libxtst-dev \  
libxss1 \  
libnss3-dev \  
gcc-multilib \  
g++-multilib \  
&& apt-get autoclean \  
&& apt-get autoremove  
  
  

