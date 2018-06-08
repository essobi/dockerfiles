FROM ubuntu:14.04  
MAINTAINER meng.lj@gmail.com  
ENV SQUID_CACHE_DIR=/var/spool/squid3 \  
SQUID_LOG_DIR=/var/log/squid3 \  
SQUID_USER=proxy  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
80F70E11F0F0D5F10CB20E62F5DA5F09C3173AA6 \  
&& echo "deb http://ppa.launchpad.net/brightbox/squid-ssl/ubuntu trusty main"
>> /etc/apt/sources.list \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y
squid3-ssl=${SQUID_VERSION}* \  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE 3128/tcp  
VOLUME ["${SQUID_CACHE_DIR}"]  

