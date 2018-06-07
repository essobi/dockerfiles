FROM node:4-onbuild  
EXPOSE 4200  
RUN apt-get -y update && \  
apt-get -y install graphicsmagick && \  
mkdir -p images/screenshots && \  
mkdir -p images/thumbs && \  
mkdir -p sources && \  
npm install -g bower && \  
bower --allow-root install  

