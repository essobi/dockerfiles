FROM ubuntu:12.04  
MAINTAINER Oliver Letterer <oliver.letterer@sparrow-labs.de>  
  
# Install sources  
RUN apt-get update  
RUN apt-get upgrade -y  
  
RUN apt-get install -y wget git make build-essential g++ && apt-get clean  
RUN apt-get install -y libcairo2-dev libjpeg8-dev libpango1.0-dev libgif-dev
&& apt-get clean  
  
RUN wget -O - http://nodejs.org/dist/v0.10.32/node-v0.10.32-linux-x64.tar.gz |
tar -C /usr/local/ --strip-components=1 -zx  
RUN npm install -g node-gyp@1.0.2  
RUN npm install -g coffee-script@1.6.2  
  
RUN mkdir -p /app  
WORKDIR /app  
  
ENV NODE_ENV production  
  
ONBUILD ADD ./package.json /app/package.json  
ONBUILD RUN npm install -p && npm cache clean  

