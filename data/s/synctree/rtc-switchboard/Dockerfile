FROM ubuntu:14.04  
MAINTAINER Masahji Stewart <masahji@synctree.com>  
  
RUN apt-get update -y  
RUN apt-get install -y curl  
  
RUN curl -sL https://deb.nodesource.com/setup | bash -  
RUN apt-get install -y nodejs  
  
RUN mkdir -p /usr/local/src  
WORKDIR /usr/local/src  
RUN curl -L https://api.github.com/repos/rtc-io/rtc-switchboard/tarball | tar
xzf -  
RUN mv rtc-io-rtc-switchboard-* rtc-switchboard  
  
WORKDIR /usr/local/src/rtc-switchboard  
RUN npm install  
  
EXPOSE 8080  
ENV NODE_PORT 8080  
ENTRYPOINT /usr/bin/nodejs server.js  

