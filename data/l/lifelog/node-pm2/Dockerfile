FROM node:0.12  
MAINTAINER Anders Janmyr "anders.janmyr@sonymobile.com"  
# Updated 2015-08-31  
ENV Version 1.5.0  
  
RUN apt-get update && \  
apt-get install zlib1g-dev && \  
npm install -g pm2 && \  
mkdir -p /srv/app  
  
WORKDIR /srv/app  
ONBUILD COPY . /srv/app  
  
ENV NODE_ENV production  
ENV SCRIPT server.js  
ENV PORT 80  
  
EXPOSE 80  
  
CMD pm2 start $SCRIPT -i 0 && pm2 logs  

