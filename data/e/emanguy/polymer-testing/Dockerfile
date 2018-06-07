FROM node:carbon  
  
LABEL maintainer "Evan Rittenhouse <emanguy1@gmail.com>"  
  
# You can change this environment variable to change the virtual screen size
defined by start-xvfb-server.sh  
ENV SCREEN_SIZE="1920x1080"  
WORKDIR /srv/  
  
# Add temporary CI installer scripts  
ADD ./ci/ ./ci/  
  
# Install necessary software  
RUN ./ci/install-chrome.sh && \  
./ci/install-firefox.sh && \  
./ci/install-java.sh && \  
rm -rf ci/ && \  
npm install -g --unsafe-perm bower polymer-cli  
  
# Add XVFB start script  
ADD ./start-xvfb-server.sh .

