# Flashaim NPM Front-end tools  
FROM node:4.4  
MAINTAINER paowang@flashaim.com  
ENV DEBIAN_FRONTEND noninteractive  
  
## Front-end tools  
RUN npm install -g \  
bower \  
browser-sync \  
nodemon \  
node-gyp \  
gulp  
RUN adduser --disabled-password --gecos "" flashaim  
  
VOLUME ["/var/www/etc"]  
WORKDIR /var/www/etc  
ENTRYPOINT []  
USER 1000  

