FROM kaidenp/baseimage-node  
MAINTAINER Kaiden Prince <github+me@kaidenprince.com>  
  
ADD docker/my_init.d /etc/my_init.d  
RUN chmod +x /etc/my_init.d/*.sh  
  
VOLUME /data  
  
ADD . /usr/src/app/  
RUN cd /usr/src/app && \  
rm -rf node_modules && \  
npm install

