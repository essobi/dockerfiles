FROM node:latest  
  
RUN echo 'deb http://ftp.uk.debian.org/debian jessie-backports main' >
/etc/apt/sources.list.d/backports.list & apt-get update && apt-get install -y
python2.7 git-all pkg-config libncurses5-dev libssl-dev libnss3-dev libexpat-
dev ffmpeg  
  
WORKDIR /src  
COPY package.json ./  
RUN npm install  
COPY ./ ./  
  
ENV SIGNALER_URL="http://signaling:3000"  
ENV QUEUE_URL="queue:5672"  
EXPOSE 3000  
CMD ["node", "app.js"]  

