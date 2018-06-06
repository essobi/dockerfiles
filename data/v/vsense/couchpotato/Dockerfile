FROM vsense/baseimage:alpine  
  
MAINTAINER vSense <docker@vsense.fr>  
  
ENV BRANCH master  
  
RUN apk add --update \  
git \  
python \  
unrar \  
zip \  
py-lxml \  
py-openssl \  
py-cryptography \  
py-enum34 \  
py-cffi \  
&& git clone -b $BRANCH \--single-branch
https://github.com/RuudBurger/CouchPotatoServer.git /couchpotato \  
&& mkdir /config \  
&& mkdir /downloads \  
&& adduser -D -h /couchpotato -s /sbin/nologin -u 5001 couchpotato \  
&& chown -R couchpotato:couchpotato /couchpotato /config /downloads \  
&& rm -rf /var/cache/apk/*  
  
VOLUME /config /downloads  
  
EXPOSE 5050  
USER couchpotato  
  
CMD ["--data_dir=/config"]  
  
ENTRYPOINT ["/usr/bin/env","python2","/couchpotato/CouchPotato.py"]  

