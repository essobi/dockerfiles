FROM debian:wheezy  
ENV NODE_VERSION 0.12.0  
ENV PATH /opt/node-v$NODE_VERSION-linux-x64/bin:$PATH  
  
RUN apt-get update && \  
apt-get -y install git wget build-essential python bzip2 openssh-client curl
--no-install-recommends && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /opt  
RUN wget --quiet -O -
http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz |
tar zxf -  
RUN npm install bower gulp -g --production && \  
npm cache clean  

