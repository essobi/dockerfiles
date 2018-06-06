FROM ubuntu:15.04  
MAINTAINER "The Impact Bot" <technology@bcorporation.net>  
  
WORKDIR /tmp  
  
RUN apt-get update -y && \  
apt-get install -y php5-cli php5-curl curl git php5-mcrypt php5-gd && \  
apt-get install -y php5-memcached memcached && \  
curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer && \  
composer self-update && \  
apt-get remove --purge curl -y && \  
apt-get clean  
  
RUN mkdir -p /data/www  
VOLUME ["/data"]  
WORKDIR /data/www  
  
ENTRYPOINT ["composer"]  
CMD ["--help"]  

