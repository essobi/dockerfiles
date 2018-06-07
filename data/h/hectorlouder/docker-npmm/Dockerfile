################################################################################  
# Base image  
# http://phusion.github.io/baseimage-docker/  
################################################################################  
FROM phusion/baseimage:0.9.18  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
ENV HOME /root  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
#Install Tools  
RUN curl -sL https://deb.nodesource.com/setup_5.x | sudo -E bash -  
RUN apt-get update && DEBIAN_FRONTEND="noninteractive" apt-get install -y
build-essential vim wget git  
RUN add-apt-repository -y ppa:ondrej/php5  
RUN add-apt-repository -y ppa:nginx/stable  
  
################################################################################  
# PHP  
################################################################################  
RUN apt-get update && \  
DEBIAN_FRONTEND="noninteractive" apt-get install --yes \  
php-pear \  
php5-cli \  
php5-common \  
php5-curl \  
php5-gd \  
php5-imagick \  
php5-imap \  
php5-intl \  
php5-json \  
php5-ldap \  
php5-mcrypt \  
php5-memcache \  
php5-mysql \  
php5-redis \  
php5-tidy \  
php-apc \  
&& pecl install mongodb  
  
RUN sed -ir 's@^#@//@' /etc/php5/mods-available/*  
RUN apt-get update && DEBIAN_FRONTEND="noninteractive" apt-get install --yes
php5-dev  
  
# Xdebug  
ENV XDEBUG_VERSION='XDEBUG_2_3_3'  
RUN git clone -b $XDEBUG_VERSION --depth 1
https://github.com/xdebug/xdebug.git /usr/local/src/xdebug  
RUN cd /usr/local/src/xdebug && \  
phpize && \  
./configure && \  
make clean && \  
make && \  
make install  
  
RUN echo "zend_extension=xdebug.so" > /etc/php5/mods-available/xdebug.ini  
RUN php5enmod xdebug  
  
# PHP-FPM  
RUN apt-get update && DEBIAN_FRONTEND="noninteractive" apt-get install --yes
php5-fpm  
RUN php5enmod -s fpm mcrypt xdebug  
  
# Enable MongoDB PHP  
RUN echo "extension=mongodb.so" > /etc/php5/mods-available/mongodb.ini  
RUN php5enmod mcrypt mongodb  
  
# Install phalcon  
RUN git clone --depth=1 git://github.com/phalcon/cphalcon.git  
RUN cd cphalcon/build && ./install 64bits  
RUN echo "extension=phalcon.so" > /etc/php5/fpm/conf.d/30-phalcon.ini  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
################################################################################  
# NGNIX  
################################################################################  
RUN apt-get update && \  
DEBIAN_FRONTEND="noninteractive" apt-get install --yes \  
nginx \  
ssl-cert  
RUN service nginx stop  
  
################################################################################  
# SSH (for remote drush)  
################################################################################  
RUN apt-get update && \  
DEBIAN_FRONTEND="noninteractive" apt-get install --yes \  
openssh-server  
RUN dpkg-reconfigure openssh-server  
  
################################################################################  
# Drush  
################################################################################  
RUN apt-get update && \  
DEBIAN_FRONTEND="noninteractive" apt-get install --yes \  
mysql-client  
  
ENV DRUSH_VERSION='8.0.3'  
RUN git clone -b $DRUSH_VERSION --depth 1 https://github.com/drush-
ops/drush.git /usr/local/src/drush  
RUN cd /usr/local/src/drush && composer install  
RUN ln -s /usr/local/src/drush/drush /usr/local/bin/drush  
COPY ./conf/drush/drush-remote.sh /usr/local/bin/drush-remote  
RUN chmod +x /usr/local/bin/drush-remote  
  
################################################################################  
# sSMTP  
# note php is configured to use ssmtp, which is configured to send to
mail:1025,  
# which is standard configuration for a mailhog/mailhog image with hostname
mail.  
################################################################################  
RUN apt-get update && DEBIAN_FRONTEND="noninteractive" apt-get install --yes
ssmtp  
  
################################################################################  
# Configure  
################################################################################  
RUN mkdir /var/www_files && \  
chgrp www-data /var/www_files && \  
chmod 775 /var/www_files  
  
# Pass all docker environment  
RUN sed -i '/^;clear_env = no/s/^;//' /etc/php5/fpm/pool.d/www.conf  
  
# Get access to FPM-ping page /ping  
RUN sed -i '/^;ping\\.path/s/^;//' /etc/php5/fpm/pool.d/www.conf  
  
# Get access to FPM_Status page /status  
RUN sed -i '/^;pm\\.status_path/s/^;//' /etc/php5/fpm/pool.d/www.conf  
  
# Prevent PHP Warning: 'xdebug' already loaded.  
# XDebug loaded with the core  
RUN sed -i '/.*xdebug.so$/s/^/;/' /etc/php5/mods-available/xdebug.ini  
  
# Copy configs  
COPY ./conf/php5/fpm/php.ini /etc/php5/fpm/php.ini  
COPY ./conf/php5/fpm/pool.d/www.conf /etc/php5/fpm/pool.d/www.conf  
COPY ./conf/php5/cli/php.ini /etc/php5/cli/php.ini  
COPY ./conf/nginx/default /etc/nginx/sites-available/default  
COPY ./conf/nginx/nginx.conf /etc/nginx/nginx.conf  
COPY ./conf/ssh/sshd_config /etc/ssh/sshd_config  
COPY ./conf/ssmtp/ssmtp.conf /etc/ssmtp/ssmtp.conf  
  
# Use baseimage-docker's init system.  
ADD init/ /etc/my_init.d/  
ADD services/ /etc/service/  
RUN chmod -v +x /etc/service/*/run  
RUN chmod -v +x /etc/my_init.d/*.sh  
  
################################################################################  
# Clean up  
################################################################################  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
################################################################################  
# Ports  
################################################################################  
EXPOSE 80 443 22  
################################################################################  
# Volumes  
################################################################################  
VOLUME ["/var/www", "/etc/nginx/conf.d", "/etc/php5/fpm/"]  

