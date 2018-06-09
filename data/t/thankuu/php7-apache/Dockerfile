FROM ubuntu:16.04  
RUN DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get -y install apache2 php7.0 libapache2-mod-php7.0 mcrypt php7.0-mysql
php7.0-curl php7.0-bcmath php7.0-mcrypt php-redis php7.0-mbstring \  
npm \  
git curl vim && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN a2enmod php7.0  
RUN a2enmod rewrite  
  
RUN sed -i "s/short_open_tag = Off/short_open_tag = On/"
/etc/php/7.0/apache2/php.ini  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
  
ADD apache2.conf /etc/apache2/apache2.conf  
ADD 000-default.conf /etc/apache2/sites-enabled/000-default.conf  
ADD default-ssl.conf /etc/apache2/sites-enabled/default-ssl.conf  
  
WORKDIR /data  
  
EXPOSE 80  
EXPOSE 443  
# Set up composer variables  
ENV COMPOSER_BINARY=/usr/local/bin/composer \  
COMPOSER_HOME=/usr/local/composer  
ENV PATH $PATH:$COMPOSER_HOME  
  
# Install composer system-wide  
RUN curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar $COMPOSER_BINARY && \  
chmod +x $COMPOSER_BINARY  
  
# Set up global composer path  
RUN mkdir -p $COMPOSER_HOME && chmod a+rw $COMPOSER_HOME  
  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

