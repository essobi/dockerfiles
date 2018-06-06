FROM aexea/aexea-base:node9  
LABEL maintainer "Aexea Carpentry"  
  
RUN apt-get update && apt-get install -y \  
libgtk2.0-0 \  
libnotify-dev \  
libgconf-2-4 \  
libnss3 \  
libxss1 \  
libasound2 \  
xvfb \  
zip  
  
# install Chromebrowser  
RUN \  
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key
add - && \  
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >
/etc/apt/sources.list.d/google.list && \  
apt-get update && \  
apt-get install -y dbus-x11 google-chrome-stable  
  
RUN mkdir -p /opt/code  
RUN chown node:node /opt/code  
WORKDIR /opt/code  
  
ENV TERM xterm  
ENV npm_config_loglevel warn  
RUN google-chrome --version  
  
ONBUILD RUN chown -R node:node /opt/code  
ONBUILD USER node  
ONBUILD COPY package*.json /opt/code/  
ONBUILD RUN npm install  
  
ONBUILD COPY . /opt/code  
ONBUILD USER root  
ONBUILD RUN find . -path ./node_modules -prune -o -exec chown node:node '{}'
\;  
ONBUILD USER node  

