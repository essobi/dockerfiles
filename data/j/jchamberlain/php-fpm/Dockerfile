# Dockerfile for running PHP-FPM  
FROM debian:jessie  
  
# install the packages we need  
RUN apt-get update && apt-get install -y \  
curl \  
git \  
php5 \  
php5-curl \  
php5-cli \  
php5-fpm \  
php5-json \  
php5-mcrypt  
  
# configure php  
COPY php-fpm.conf /etc/php5/fpm/  
COPY php.ini /etc/php5/fpm/  
  
# install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --filename=composer
--install-dir=/usr/bin  
  
# redirect fpm logs to stdout  
RUN mkdir /var/log/php-fpm && \  
chmod 777 /var/log/php-fpm && \  
ln -s /proc/self/fd/2 /var/log/php-fpm/error.log && \  
ln -s /proc/self/fd/2 /var/log/php-fpm/access.log  
  
EXPOSE 9000  
CMD ["/usr/sbin/php5-fpm", "--nodaemonize"]

