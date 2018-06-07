# Debian: PHP5  
#  
# VERSION 0.0.1  
FROM debian:jessie  
  
RUN apt-get clean && \  
apt-get update && \  
apt-get install -y \  
php5-apcu \  
php5-cli \  
php5-common \  
php5-curl \  
php5-fpm \  
php5-mysql  
  
RUN apt-get update && \  
apt-get install -y \  
curl && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer && \  
apt-get purge -y curl  
  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENTRYPOINT ["php5-fpm"]  
  
CMD ["-F"]  
  
EXPOSE 9000  

