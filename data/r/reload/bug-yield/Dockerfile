FROM phusion/baseimage:0.9.17  
  
COPY ./ /bug-yield/  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
php5-cli \  
php5-curl \  
&& \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# Link output into /var/www/html.  
  
RUN curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer && \  
cd /bug-yield && composer install && \  
crontab /bug-yield/docker/crontab  

