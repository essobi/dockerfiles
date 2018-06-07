#Base image you want to build from  
FROM node:6.5  
#Name of Maintainer  
MAINTAINER Eddie Posey <eposey89@gmail.com>  
  
#Show colors in docker terminal  
ENV COMPOSE_HTTP_TIMEOUT=50000  
ENV TERM="xterm-256color"  
#Environment Variables  
ENV CONTAINER_PATH /angular-build-starter  
  
#Location in the container where the app will run  
RUN mkdir -p $CONTAINER_PATH  
WORKDIR $CONTAINER_PATH  
  
#Install Ruby  
RUN \  
apt-get update && \  
apt-get install build-essential chrpath libssl-dev libxft-dev -y ruby ruby-dev
&& \  
rm -rf /var/lib/apt/lists/*  
  
RUN cd $(npm root -g)/npm \  
&& npm install fs-extra \  
&& sed -i -e s/graceful-fs/fs-extra/ -e s/fs.rename/fs.move/
./lib/utils/rename.js  
  
ENV NPM_VERSION 3.8.6  
#Installing global dependencies for global environment of container  
RUN \  
gem install scss_lint && \  
npm install -g npm@"$NPM_VERSION" && \  
npm install gulp@3.9.1 -g && \  
npm install jspm@0.16.45 -g && \  
npm install karma-cli@1.0.1 -g && \  
npm install phantomjs-prebuilt@2.1.12 -g

