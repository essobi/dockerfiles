FROM alpine  
MAINTAINER Arnaud Piroelle  
  
RUN apk update && \  
apk --update add python git unrar zip unzip openssl py-openssl py-mako \  
rm -rf /var/cache/apk/*  
  
RUN cd / && git clone https://github.com/SickRage/SickRage.git sickrage  
  
EXPOSE 8081  
VOLUME ["/data"]  
VOLUME ["/media"]  
  
CMD ["/usr/bin/env", "python2", "/sickrage/SickBeard.py", "--datadir=/data", "
--nolaunch"]  

