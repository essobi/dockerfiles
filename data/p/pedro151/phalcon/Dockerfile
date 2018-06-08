FROM ubuntu:16.10  
MAINTAINER Pedro Alarcao  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install apache, PHP, and supplimentary programs. openssh-server, curl, and
lynx-cur are for debugging the container.  
RUN PACKAGES_TO_INSTALL="sudo apache2 git cron re2c php7.0-dev composer php-
xdebug php7.0-mbstring php7.0-curl php7.0-fpm supervisor libyaml-dev
php7.0-pgsql libapache2-mod-php7.0 php7.0-phar " \  
&& apt-get update \  
&& apt-get install -y software-properties-common \  
&& apt-get install -y $PACKAGES_TO_INSTALL \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& apt-get autoclean  
  
# Enable apache mods.  
RUN a2enmod php7.0  
RUN a2enmod rewrite  
  
RUN git clone \--depth=1 https://github.com/phalcon/cphalcon.git
/usr/local/src/cphalcon  
RUN cd /usr/local/src/cphalcon/build && ./install  
RUN echo "extension=phalcon.so" > /etc/php/7.0/mods-available/phalcon.ini && \  
ln -s /etc/php/7.0/mods-available/phalcon.ini
/etc/php/7.0/cli/conf.d/20-phalcon.ini && \  
ln -s /etc/php/7.0/mods-available/phalcon.ini
/etc/php/7.0/fpm/conf.d/20-phalcon.ini && \  
phpenmod phalcon  
  
# XDebug  
RUN echo
"xdebug.remote_enable=on\nxdebug.idekey=PHPSTORM\nxdebug.remote_host=192.168.99.100\nxdebug.remote_port=9000\nxdebugutostart=on\nxdebug.remote_connect_back=on"
>> /etc/php/7.0/mods-available/xdebug.ini \  
&& ln -sf /etc/php/7.0/mods-available/xdebug.ini
/etc/php/7.0/cli/conf.d/20-xdebug.ini \  
&& ln -sf /etc/php/7.0/mods-available/xdebug.ini
/etc/php/7.0/fpm/conf.d/20-xdebug.ini  
  
# Update the PHP.ini file, enable <? ?> tags and quieten logging.  
RUN sed -i "s/short_open_tag = Off/short_open_tag = On/"
/etc/php/7.0/apache2/php.ini \  
&& sed -i "s/short_open_tag = Off/short_open_tag = On/"
/etc/php/7.0/cli/php.ini \  
&& sed -i "s/;date.timezone =/date.timezone = America\/Sao_Paulo/"
/etc/php/7.0/cli/php.ini \  
&& sed -i "s/;date.timezone =/date.timezone = America\/Sao_Paulo/"
/etc/php/7.0/fpm/php.ini \  
&& sed -i "s/;date.timezone =/date.timezone = America\/Sao_Paulo/"
/etc/php/7.0/apache2/php.ini \  
&& sed -i "s/error_reporting = E_ALL & ~E_DEPRECATED &
~E_STRICT/error_reporting = E_ALL/" /etc/php/7.0/cli/php.ini \  
&& sed -i "s/error_reporting = E_ALL & ~E_DEPRECATED &
~E_STRICT/error_reporting = E_ALL/" /etc/php/7.0/fpm/php.ini \  
&& sed -i "s/error_reporting = E_ALL & ~E_DEPRECATED &
~E_STRICT/error_reporting = E_ALL/" /etc/php/7.0/apache2/php.ini \  
&& sed -i "s/display_errors = Off/display_errors = On/"
/etc/php/7.0/cli/php.ini \  
&& sed -i "s/display_errors = Off/display_errors = On/"
/etc/php/7.0/fpm/php.ini \  
&& sed -i "s/display_errors = Off/display_errors = On/"
/etc/php/7.0/apache2/php.ini \  
&& sed -i "s/display_startup_errors = Off/display_startup_errors = On/"
/etc/php/7.0/cli/php.ini \  
&& sed -i "s/display_startup_errors = Off/display_startup_errors = On/"
/etc/php/7.0/apache2/php.ini \  
&& sed -i "s/display_startup_errors = Off/display_startup_errors = On/"
/etc/php/7.0/fpm/php.ini  
  
# install phpunit  
RUN curl https://phar.phpunit.de/phpunit.phar -L > phpunit.phar \  
&& chmod +x phpunit.phar \  
&& mv phpunit.phar /usr/local/bin/phpunit \  
&& phpunit --version  
  
# Manually set up the apache environment variables  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
  
# Expose apache.  
EXPOSE 80 443  
RUN mkdir /var/www/public  
  
# add a phpinfo script for INFO purposes  
RUN echo "<?php phpinfo();" >> /var/www/public/index.php  
  
# apache mountable directory for apps  
VOLUME [ "/var/www" ]  
WORKDIR /var/www  
  
# Update the default apache site with the config we created.  
COPY apache-config.conf /etc/apache2/sites-enabled/000-default.conf  
  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

