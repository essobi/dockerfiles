FROM node:0.10  
MAINTAINER Jean-Tiare Le Bigot "jt@lebigot.net"  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN useradd ttyjs --password '*' \--create-home  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install htop vim  
  
USER ttyjs  
EXPOSE 8080  
WORKDIR /home/ttyjs  
  
RUN npm install tty.js  
CMD ["node_modules/.bin/tty.js"]  
  

