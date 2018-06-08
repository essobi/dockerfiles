FROM ubuntu:16.04  
MAINTAINER mustafa.bayrak@windowslive.com  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV BIND_USER=bind \  
BIND_VERSION=1:910.3 \  
WEBMIN_VERSION=1.881 \  
DATA_DIR=/data \  
GPG_KEY=http://www.webmin.com/jcameron-key.asc  
#GPG_KEY=https://gist.githubusercontent.com/enoch85/092c8f4c4f5127b99d40/raw/186333393163b7e0d50c8d3b25cae4d63ac78b22/jcameron-
key.asc  
RUN rm -rf /etc/apt/apt.conf.d/docker-gzip-indexes  
RUN apt-get update && \  
apt-get install apt-utils wget -y && \  
wget ${GPG_KEY} -qO - | apt-key add - && \  
echo "deb http://download.webmin.com/download/repository sarge contrib" >>
/etc/apt/sources.list && \  
apt-get update && apt-get dist-upgrade -y && \  
apt-get install -y bind9 bind9-host webmin=${WEBMIN_VERSION} dnsutils  
RUN rm -rf /var/lib/apt/lists/*  
  
COPY entrypoint.sh /sbin/entrypoint.sh  
RUN chmod 755 /sbin/entrypoint.sh  
  
EXPOSE 53/udp 53/tcp 10000/tcp  
ENTRYPOINT ["/sbin/entrypoint.sh"]  
CMD ["/usr/sbin/named"]  

