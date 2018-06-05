FROM ubuntu:bionic  
  
ENV VERSION 2.6.2  
  
RUN apt-get update && \  
apt-get upgrade -y  
  
RUN apt-get install git cmake make libuv1-dev libmicrohttpd-dev build-
essential -y  
  
RUN apt-get autoclean && \  
apt-get autoremove  
  
COPY entrypoint.sh /usr/local/bin/xmrig.sh  
  
ENTRYPOINT ["xmrig.sh"]  

