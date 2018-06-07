FROM ubuntu:14.04  
MAINTAINER Eric Bittlman <ebittleman@heyo.com>  
  
# install dependencies non-interactively  
RUN \  
DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get install git dos2unix imagemagick libmagickwand-dev build-essential
php5-cgi php5 php5-cli php5-dev php5-fpm php5-curl php5-gd php5-mcrypt
php5-mysql php-pear php-soap php-apc supervisor wget -y  
  
# configure fpm  
RUN sed -i '/^;daemonize = /cdaemonize = no' /etc/php5/fpm/php-fpm.conf  
RUN sed -i '/^listen = /clisten = 0.0.0.0:9000' /etc/php5/fpm/pool.d/www.conf  
RUN sed -i '/^;listen.allowed_clients/clisten.allowed_clients = 0.0.0.0'
/etc/php5/fpm/pool.d/www.conf  
RUN sed -i '/^childlogdir=/anodaemon=true' /etc/supervisor/supervisord.conf  
  
# give us a spot for the wand install  
RUN mkdir -p /tmp/php-wand  
  
# send the wand install script to the container  
ADD scripts/magickwand-php-install.sh /tmp/php-wand/magickwand-php-install.sh  
  
# Add fpm to supervisor  
ADD scripts/php5-fpm.conf /etc/supervisor/conf.d/php5-fpm.conf  
RUN dos2unix /etc/supervisor/conf.d/php5-fpm.conf  
  
# prep the install script  
RUN chmod +x /tmp/php-wand/magickwand-php-install.sh  
  
# install magickwand for php  
RUN \  
TMP_CURR_DIR=`pwd` && \  
cd /tmp/php-wand && \  
dos2unix magickwand-php-install.sh && \  
./magickwand-php-install.sh && \  
cd $TMP_CURR_DIR  
  
# clean up  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 9000  
CMD ["/usr/bin/supervisord"]  

