FROM lsiobase/xenial  
MAINTAINER Poag  
  
#Setup Repos  
RUN \  
apt update && \  
apt-get install -y software-properties-common python-software-properties && \  
add-apt-repository ppa:jon-hedgerows/get-iplayer  
# install packages  
RUN \  
apt-get update && \  
apt-get install -y get-iplayer && \  
  
# cleanup  
apt-get clean && \  
rm -rf \  
/tmp/* \  
/var/lib/apt/lists/* \  
/var/tmp/*  
  
# ports and volumes  
EXPOSE 1935  
VOLUME /config /data  
  
COPY root/ /root/  
CMD ["/bin/bash", "/root/start.sh"]  

