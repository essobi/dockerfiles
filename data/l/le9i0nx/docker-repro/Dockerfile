FROM ubuntu:16.04  
MAINTAINER Aleksej Gavrilov <le9i0nx@gmail.com>  
ENV LC_ALL C  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update && \  
apt-get dist-upgrade -y && \  
apt-get install -y \  
sudo \  
openssl \  
php-fpm \  
php-mysql \  
php \  
php-auth \  
php-cli \  
php-intl \  
php-json \  
php-mail-mime \  
php-mail-mimedecode \  
php-mcrypt \  
php-net-smtp \  
php-sockets \  
php-net-ldap3 \  
php-net-sieve && \  
apt-get clean && \  
mkdir /srv/www && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*  
  
# Configure FPM to run properly on docker  
RUN sed -i "/;access.log = .*/c\access.log = /proc/self/fd/2"
/etc/php/7.0/fpm/pool.d/www.conf \  
&& sed -i "/;clear_env = .*/c\clear_env = no" /etc/php/7.0/fpm/pool.d/www.conf
\  
&& sed -i "/;catch_workers_output = .*/c\catch_workers_output = yes"
/etc/php/7.0/fpm/pool.d/www.conf \  
&& sed -i "/pid = .*/c\;pid = /run/php/php7.0-fpm.pid" /etc/php/7.0/fpm/php-
fpm.conf \  
&& sed -i "/;daemonize = .*/c\daemonize = no" /etc/php/7.0/fpm/php-fpm.conf \  
&& sed -i "/error_log = .*/c\error_log = /proc/self/fd/2"
/etc/php/7.0/fpm/php-fpm.conf  
  
VOLUME ["/srv/www"]  
CMD ["/usr/sbin/php-fpm7.0", "-F", "-O" ]  
# docker pull le9i0nx/docker-repro:php7-fpm  
# docker run -i -v /srv/www:/srv/www:ro -v /run/php:/run/php:rw --name
php7-fpm le9i0nx/docker-repro:php7-fpm  

