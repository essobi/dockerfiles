# netdata dockerfile by MO  
#  
# VERSION 16.10.0  
FROM ubuntu:16.04  
MAINTAINER MO  
  
# Setup apt  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install dependencies and packages  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install netcat-openbsd lm-sensors python python-mysqldb python-yaml
curl jq nodejs zlib1g-dev uuid-dev libmnl-dev gcc make git autoconf autoconf-
archive autogen automake pkg-config && \  
  
# Install netdata  
cd /root && \  
git clone https://github.com/firehol/netdata -b v1.6.0 && \  
cd netdata && \  
./netdata-installer.sh \--dont-wait --dont-start-it && \  
cd .. && \  
rm -rf netdata && \  
  
# Clean up  
apt-get purge -y make gcc zlib1g-dev uuid-dev libmnl-dev git autoconf autogen
automake pkg-config && \  
apt-get -y autoremove && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Start netdata  
WORKDIR /  
CMD ["/usr/sbin/netdata","-D","-s","/host","-i","127.0.0.1","-p","64301"]  

