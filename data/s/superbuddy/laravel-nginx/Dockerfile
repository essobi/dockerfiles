# docker build -f Dockerfile -t superbuddy/laravel-nginx .  
FROM php:5-fpm  
  
MAINTAINER svlentink <sander@superbuddy.nl>  
LABEL Description="Laravel and Nginx"  
  
# https://github.com/phusion/baseimage-docker/issues/58  
# http://serverfault.com/questions/618994/when-building-from-dockerfile-
debian-ubuntu-package-install-debconf-noninteract  
ENV DEBIAN_FRONTEND noninteractive  
  
# runs during installation and remove junk, as described in
http://docs.docker.com/engine/articles/dockerfile_best-practices/#apt-get  
RUN apt-get update && \  
apt-get install -y \  
git \  
cron \  
nginx \  
# https://github.com/docker-library/php/issues/60  
zlib1g-dev \  
mcrypt \  
# ubuntu = php-mcrypt, debian = php5-mcrypt  
php5-mcrypt \  
php5-fpm \  
# gd; http://serverfault.com/questions/436634/installing-php-extensions-on-
linux  
php5-gd \  
php5-mysql \  
php5-imap \  
# https://laravel.com/docs/5.0#server-requirements  
php5-json \  
php5-curl \  
# The following three are mentioned by
https://hub.docker.com/r/cheezykins/laravel/~/dockerfile/  
libgmp10 \  
libgmp-dev \  
mysql-client \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN docker-php-ext-install \  
bcmath \  
# gmp \  
mbstring \  
mysql \  
pdo \  
pdo_mysql \  
# https://hub.docker.com/r/ganiutomo/docker-php-laravel/~/dockerfile/  
zip  
  
# Install composer (PHP dep. manager)  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
RUN cp /etc/php5/cli/php.ini /usr/local/etc/php/conf.d/php.ini  
  
RUN php5enmod mcrypt  
# && php5enmod imap \  
# && php5enmod mysql \  
# && php5enmod  
# defining the volumes that need to be mounted  
VOLUME /var/www/storage/logs  
VOLUME /var/log/nginx  
  
# Set up cron  
# https://laravel.com/docs/5.1/scheduling  
ADD crontab /var/spool/cron/crontabs/www-data  
RUN chown www-data.crontab /var/spool/cron/crontabs/www-data  
RUN chmod 0600 /var/spool/cron/crontabs/www-data  
  
COPY nginx.conf /etc/nginx/sites-available/default  
RUN sed -i "s/request_terminate_timeout =.*/request_terminate_timeout=3600/g"
/etc/php5/fpm/php.ini  
RUN sed -i "s/default_socket_timeout =.*/default_socket_timeout=3600/g"
/etc/php5/fpm/php.ini  
RUN sed -i "s/max_execution_time =.*/max_execution_time=3600/g"
/etc/php5/fpm/php.ini  
RUN sed -i "s/cgi.fix_pathinfo=/cgi.fix_pathinfo=0#/g" /etc/php5/fpm/php.ini  
  
COPY run_after_copying_repo.sh /usr/local/bin/run_after_copying_repo  
  
# https://www.digitalocean.com/community/tutorials/docker-explained-how-to-
containerize-and-use-nginx-as-a-proxy  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
# https://github.com/nginxinc/docker-
nginx/blob/11fc019b2be3ad51ba5d097b1857a099c4056213/mainline/jessie/Dockerfile#L27  
CMD service php5-fpm start && nginx  

