FROM debian:wheezy  
MAINTAINER Patrick Poulain <docker@m41l.me>  
RUN apt-get update  
RUN apt-get -y install php5-fpm  
RUN apt-get -y install locales  
RUN echo "fr_FR.UTF-8 UTF-8" > /etc/locale.gen  
RUN locale-gen  
RUN update-locale LANG=fr_FR.UTF-8  
COPY ./php.ini /etc/php5/fpm/php.ini  
COPY ./php-fpm.conf /etc/php5/fpm/php-fpm.conf  
COPY ./www.conf /etc/php5/fpm/pool.d/www.conf  
  
RUN mkdir -p /var/www && \  
echo "<?php phpinfo(); ?>" > /var/www/index.php && \  
chown -R www-data:www-data /var/www  
RUN apt-get -y install php-apc  
RUN apt-get -y autoremove  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 9000  
CMD ["php5-fpm"]

