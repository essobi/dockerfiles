FROM tabazevedo/base  
MAINTAINER Tiago Azevedo @ https://github.com/tabazevedo  
  
RUN \  
DEBIAN_FRONTEND=noninteractive apt-get -y install software-properties-common
&&\  
add-apt-repository ppa:chris-lea/node.js &&\  
DEBIAN_FRONTEND=noninteractive apt-get update &&\  
DEBIAN_FRONTEND=noninteractive apt-get -y install nodejs &&\  
npm install -g gulp bower  
  
VOLUME /data  
WORKDIR /data

