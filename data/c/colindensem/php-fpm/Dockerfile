FROM debian:wheezy  
MAINTAINER Colin Densem "hello@summit360.co.uk"  
# Add dotdeb for extra php support packages, e.g. redis, php5.6 etc  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E9C74FEEA2098A6E
&& \  
echo "deb http://packages.dotdeb.org wheezy-php56-zts all" >>
/etc/apt/sources.list.d/dotdeb.list && \  
echo "deb-src http://packages.dotdeb.org wheezy-php56-zts all" >>
/etc/apt/sources.list.d/dotdeb.list && \  
apt-get update && \  
apt-get install -y \  
php5-apcu \  
php5-cli \  
php5-curl \  
php5-fpm \  
php5-json \  
php5-gd \  
php5-intl \  
php5-imagick \  
php5-imap \  
php5-mcrypt \  
php5-memcache \  
php5-mysql \  
php5-redis && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
  
COPY config/etc /etc  
  
VOLUME ["/srv/application"]  
  
# EXPOSE  
EXPOSE 9000  
WORKDIR /srv/application/public  
CMD ["/usr/sbin/php5-fpm", "--nodaemonize"]  
  

