FROM ubuntu:14.04.3  
MAINTAINER Ivan Pushkin <imetalguardi+docker@gmail.com>  
  
ENV TERM xterm  
  
# add ondrej php repository  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
14AA40EC0831756756D7F66C4F4EA0AAE5267A6C  
RUN echo "deb http://ppa.launchpad.net/ondrej/php5-5.6/ubuntu $(lsb_release
-cs) main" > /etc/apt/sources.list.d/php.list  
  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q \  
php5-fpm \  
php5-cli \  
php5-mysql \  
php5-curl \  
php5-gd \  
php5-intl \  
php5-imagick \  
php5-memcached \  
php5-json  
  
RUN php -v  
  
# add php configuration file in specified position  
COPY custom.php.ini /etc/php5/mods-available/custom.ini  
  
# add custom php configuration  
RUN php5enmod custom  
  
# clean apt cache and temps  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# replace php-fpm configuration file  
COPY php-fpm.conf /etc/php5/fpm/php-fpm.conf  
  
# add user "docker" to use it as default user for working with files  
RUN yes "" | adduser --uid=1000 --disabled-password docker  
RUN echo "docker ALL=(ALL:ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
RUN mkdir -p /web/docker  
RUN echo "<?php echo 'web server is running';" > /web/docker/index.php  
RUN chown -R docker:docker /web  
  
EXPOSE 9000  
WORKDIR /web  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["php5-fpm", "-F"]  

