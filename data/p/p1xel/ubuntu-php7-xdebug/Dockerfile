FROM ubuntu:16.04  
MAINTAINER Vadym Panchenko<vadym.intertech@gmail.com>  
  
RUN apt-get update  
RUN apt-get -y upgrade  
  
#RUN ln -s /usr/bin/php7 /usr/bin/php  
RUN apt-get -y install python-software-properties software-properties-common  
  
RUN LC_ALL=C.UTF-8 add-apt-repository -y -s ppa:ondrej/php  
  
RUN apt-get -y update  
  
RUN apt-get -y install apache2 libapache2-mod-php7.1 php7.1-mysql php7.1-gd
php-apcu  
RUN apt-get -y install php7.1-curl php7.1-xml php7.1-zip php7.1-mcrypt
php7.1-mbstring  
RUN apt-get -y install php7.1-dev php7.1-json php7.1-intl php7.1-cli php7.1
php-xdebug php-soap php-curl  
  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
#RUN usermod -u www-data www-data  
#RUN a2enmod php5  
RUN a2enmod php7.1  
RUN a2enmod rewrite  
  
RUN apt-get install -y mc vim  
  
# ----------------------------  
# Configure a xDebug Extension  
# ----------------------------  
RUN echo "zend_extension=/usr/lib/php/20160303/xdebug.so" >>
/etc/php/7.1/apache2/php.ini  
RUN echo "xdebug.max_nesting_level=250" >> /etc/php/7.1/apache2/php.ini  
RUN echo "xdebug.var_display_max_depth=10" >> /etc/php/7.1/apache2/php.ini  
RUN echo "xdebug.remote_enable=true" >> /etc/php/7.1/apache2/php.ini  
RUN echo "xdebug.remote_handler=dbgp" >> /etc/php/7.1/apache2/php.ini  
RUN echo "xdebug.remote_mode=req" >> /etc/php/7.1/apache2/php.ini  
RUN echo "xdebug.remote_port=9000" >> /etc/php/7.1/apache2/php.ini  
RUN echo "xdebug.remote_host=172.18.0.2" >> /etc/php/7.1/apache2/php.ini
#Please provide your host (local machine IP)  
RUN echo "xdebug.idekey=phpstorm-xdebug" >> /etc/php/7.1/apache2/php.ini  
RUN echo "xdebug.remote_autostart=1" >> /etc/php/7.1/apache2/php.ini  
RUN echo "xdebug.remote_log=/var/log/apache2/xdebug_remote.log" >>
/etc/php/7.1/apache2/php.ini  
  
# -----------------  
# Configure Apache2  
# -----------------  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
  
EXPOSE 9000  
EXPOSE 80  
ENV PHP_XDEBUG_ENABLED: 1 # Set 1 to enable debuger  
ENV XDEBUG_CONFIG: remote_host=172.18.0.2  
#ADD www /var/www/site  
VOLUME ["/var","/var/www/site"]  
  
ADD apache-config.conf /etc/apache2/sites-enabled/000-default.conf  
  
CMD /usr/sbin/apache2ctl -D FOREGROUND

