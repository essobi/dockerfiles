FROM node:6  
RUN echo "deb http://ftp.debian.org/debian jessie-backports main contrib non-
free" > /etc/apt/sources.list.d/jessie-backport.list \  
&& apt-get update \  
&& apt-get install ffmpeg -y  
  
COPY package.json /usr/src/app/package.json  
  
WORKDIR /usr/src/app  
  
RUN npm install --production  
  
COPY . /usr/src/app  
  
WORKDIR /download  
  
VOLUME /download  
  
ENTRYPOINT [ "node", "/usr/src/app/src/index.js" ]  

