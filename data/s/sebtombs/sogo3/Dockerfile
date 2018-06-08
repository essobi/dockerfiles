FROM phusion/baseimage  
MAINTAINER "Mark D-B" <dh1@sebtombs.com>  
# Based on work by Jens Erat <email@jenserat.de>, jenserat/sogo  
# Install Apache, SOGo 3 from nightly repository  
# Nightly must be used because stable versions are only available to those
with active support from Inverse  
# This does not automatically keep track of the Ubuntu version used in
phusion/baseimage  
RUN apt-get install apt-transport-https && \  
echo "deb https://packages.inverse.ca/SOGo/nightly/3/ubuntu/ xenial xenial" >
/etc/apt/sources.list.d/SOGo.list && \  
apt-key adv --keyserver keys.gnupg.net --recv-key 0x810273C4 && \  
apt-get update  
# Original method suggested by Inverse - echo should be OK instead  
# cat >/etc/apt/sources.list.d/SOGo.list <<EOF && \  
# deb https://packages.inverse.ca/SOGo/nightly/3/ubuntu/ xenial xenial  
# EOF  
# SOGo and dependencies such as sope  
RUN apt-get install -y sogo && \  
#  
apt-get install -y --no-install-recommends gettext-base apache2 memcached && \  
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
  
# Make GATEWAY host available, control memcached startup  
RUN mkdir -p /etc/my_init.d  
ADD gateway.sh memcached-control.sh /etc/my_init.d/  
  
# Interface the environment  
VOLUME /srv  
EXPOSE 80 443 8800  
# Baseimage init process  
ENTRYPOINT ["/sbin/my_init"]  

