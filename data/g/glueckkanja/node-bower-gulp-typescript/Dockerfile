FROM debian:latest  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
git \  
nodejs \  
npm \  
&& ln -s /usr/bin/nodejs /usr/bin/node \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN npm install -g bower gulp-cli typescript \  
&& npm cache clean  

