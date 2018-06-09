# version: 0.1  
#  
FROM ubuntu:14.04  
MAINTAINER feilunzhou "feilunzhou@126.com"  
ENV BUILD_DATE 2015-06-13  
# prepare tools  
RUN apt-get update  
RUN apt-get install -yqq git curl  
  
# install node.js v0.10.33  
RUN curl -sL https://deb.nodesource.com/setup | sudo bash -  
RUN apt-get install -y nodejs  
  
# install tilestream components  
RUN git clone https://github.com/tangrams/tangram.git ~/tangram  
RUN cd ~/tangram && npm install  
RUN npm install -g http-server  
  
WORKDIR /root/tangram  
# ENTRYPOINT ["./index.js", "start"]  
CMD ["./index.js", "."]  
  
# EXPOSE 8888  
# $> docker run -d -P --name tilestream feilunzhou/tilestream  
# $> docer port tilestream  
# $> boot2docker ip  
#  
# $> curl $BOOT2DOCKER_IP:$TILESTREAM_IP_MAPED  

