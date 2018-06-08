FROM marmotz/debian-fr  
  
USER root  
  
ADD init_php.sh /  
  
# Upgrade PECL  
RUN apt-get update -y && \  
apt-get install -y --force-yes php-pear && \  
pear upgrade  
  
# PHP  
RUN apt-get install -y --force-yes php7.0-cli php7.0-mysql php7.0-json
php7.0-xsl php7.0-intl php7.0-xdebug \  
php7.0-curl php7.0-gd php7.0-apcu php7.0-mbstring php7.0-zip  
  
# Xdebug  
ADD xdebug.ini /etc/php/7.0/cli/conf.d/20-xdebug.ini  
  
# Default php conf  
RUN sed -i "s@^;date.timezone =.*@date.timezone = $TIMEZONE@"
/etc/php/7.0/cli/php.ini  
  
# DEV conf for php  
RUN sed -i "s@^error_reporting =.*@error_reporting = E_ALL@"
/etc/php/7.0/cli/php.ini  
RUN sed -i "s@^display_errors =.*@display_errors = On@"
/etc/php/7.0/cli/php.ini  
RUN sed -i "s@^display_startup_errors =.*@display_startup_errors = On@"
/etc/php/7.0/cli/php.ini  
  
# Composer  
RUN curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer && \  
chmod +x /usr/local/bin/composer  
  
# Mysql client  
RUN apt-get install -y mysql-client  
  
# Clean  
RUN rm -rf /var/lib/apt/lists/*  
  
USER nonrootuser  
  
VOLUME [ "/var/php" ]  
WORKDIR /var/php  
CMD ["/init_php.sh"]  

