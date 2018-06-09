FROM ubuntu:16.04  
MAINTAINER Vadzim Budzishyn <vadim.budzishyn@gmail.com>  
  
RUN \  
apt-get update -y && \  
apt-get install -y --no-install-recommends transmission-cli transmission-
common transmission-daemon && \  
apt-get clean && \  
rm -rf \  
/tmp/* \  
/var/lib/apt/lists/* \  
/var/tmp/*  
  
COPY ./entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
  
EXPOSE 9091 51413  
ENTRYPOINT ["/entrypoint.sh"]  

