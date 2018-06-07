FROM phusion/baseimage  
  
  
# Install packages. TODO: review packages  
RUN apt-get update && \  
apt-get -y install \  
curl \  
php5-fpm \  
php5-mysql \  
php5-imagick \  
php5-imap \  
php5-mcrypt \  
php5-curl \  
php5-cli \  
php5-gd \  
php5-common \  
php-pear \  
php5-json \  
php5-intl \  
php5-xdebug  
  
# Install composer globally  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/bin/ && \  
mv /usr/bin/composer.phar /usr/bin/composer  
  
# Clean image  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Configure php5-fpm  
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php5/fpm/php-
fpm.conf  
  
# Add pool config file.  
ADD dev-pool.conf /etc/php5/fpm/pool.d/  
  
# Default php-fpm settings  
ADD 01-change_default.ini /etc/php5/fpm/conf.d/  
# Add xbegug config file  
ADD 30-xdebug.ini /etc/php5/fpm/conf.d/  
  
# TODO: add data volumes  
EXPOSE 9000  
ENTRYPOINT ["php5-fpm","-F"]  

