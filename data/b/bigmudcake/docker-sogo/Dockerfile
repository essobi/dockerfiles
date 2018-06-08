FROM phusion/baseimage:0.9.19  
MAINTAINER Jens Erat <email@jenserat.de>  
  
# Get phusion/baseimage version tag from  
## https://hub.docker.com/r/phusion/baseimage/tags/  
## https://github.com/phusion/baseimage-docker/blob/master/Changelog.md  
# Install Apache, SOGo from repository  
RUN echo "deb http://packages.inverse.ca/SOGo/nightly/3/ubuntu xenial xenial"
> /etc/apt/sources.list.d/inverse.list && \  
apt-key adv --keyserver pool.sks-keyservers.net --recv-key
FE9E84327B18FF82B0378B6719CDA6A9810273C4 && \  
apt-get update && \  
apt-get install -y --no-install-recommends gettext-base iproute2 apache2 sogo
sogo-activesync sope4.9-gdl1-mysql memcached && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Activate required Apache modules  
RUN a2enmod headers proxy proxy_http rewrite ssl  
  
# Move SOGo's data directory to /srv  
RUN usermod --home /srv/lib/sogo sogo  
  
# Fix memcached not listening on IPv6  
RUN sed -i -e 's/^-l.*/-l localhost/' /etc/memcached.conf  
  
# SOGo daemons  
RUN mkdir /etc/service/sogod /etc/service/apache2 /etc/service/memcached  
ADD sogod.sh /etc/service/sogod/run  
ADD apache2.sh /etc/service/apache2/run  
ADD memcached.sh /etc/service/memcached/run  
  
# Make GATEWAY host available, control startup of optional services such as
memcache and apache  
RUN mkdir -p /etc/my_init.d  
ADD gateway.sh control.sh /etc/my_init.d/  
  
# Interface the environment  
VOLUME /srv  
EXPOSE 80 443 8800 20000  
# USER sogo  
# Baseimage init process  
ENTRYPOINT ["/sbin/my_init"]  

