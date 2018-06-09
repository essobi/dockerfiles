# version: 0.1  
#  
FROM ubuntu:14.04  
MAINTAINER feilunzhou "feilunzhou@126.com"  
ENV BUILD_DATE 2015-06-11  
# prepare tools  
RUN apt-get update  
RUN apt-get install -yqq git curl  
  
# install node.js v0.10.33  
RUN curl -sL https://deb.nodesource.com/setup | sudo bash -  
RUN apt-get install -y nodejs  
  
# install tilestream components  
RUN git clone https://github.com/mapbox/tilestream.git ~/tilestream  
RUN cd ~/tilestream && npm install  
  
WORKDIR /root/tilestream  
ENTRYPOINT ["./index.js", "start"]  
CMD ["--host=*.*.*.*"]  
  
EXPOSE 8888  
# $> docker run -d -P --name tilestream feilunzhou/tilestream  
# $> docer port tilestream  
# $> boot2docker ip  
#  
# $> curl $BOOT2DOCKER_IP:$TILESTREAM_IP_MAPED  

