FROM dylanlindgren/docker-phpcli:latest  
  
MAINTAINER skyscrapers "support@skyscrapers.eu"  
WORKDIR /tmp  
  
RUN apt-get update -y && \  
apt-get install -y curl git php5-mcrypt php5-gd php5-curl php5-intl php-
gettext gettext && \  
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

