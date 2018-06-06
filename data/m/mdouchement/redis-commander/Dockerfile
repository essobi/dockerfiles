FROM ubuntu:14.04  
MAINTAINER mdouchement  
  
RUN apt-get update; \  
apt-get -y dist-upgrade; \  
apt-get install -y software-properties-common; \  
add-apt-repository ppa:chris-lea/node.js; \  
apt-get update; \  
apt-get install -y nodejs  
  
RUN npm install -g redis-commander  
EXPOSE 8081  
CMD /usr/bin/redis-commander  

