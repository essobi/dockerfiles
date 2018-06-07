FROM php:5.6-apache  
  
RUN apt-get update  
RUN apt-get install -y unzip vim libssl-dev ssmtp libxml2-dev gettext locales
freetds-dev  
  
# locale  
RUN localedef -i de_DE -f UTF-8 de_DE.UTF8  
RUN localedef -i en_GB -f UTF-8 en_GB.UTF8  
  
# mssql  
RUN ln -s /usr/lib/x86_64-linux-gnu/libsybdb.a /usr/lib/libsybdb.a  
  
# extensions  
RUN docker-php-ext-install mysql mysqli pdo pdo_mysql mbstring mssql ftp soap
gettext  
RUN a2enmod rewrite  
RUN a2enmod php5  
RUN a2enmod ssl  
  
# redis  
RUN curl -L -o ./phpredis.zip
https://github.com/phpredis/phpredis/archive/develop.zip \  
&& unzip phpredis.zip \  
&& cd phpredis-develop \  
&& phpize \  
&& ./configure \  
&& make \  
&& make install \  
&& cd .. \  
&& rm -rf phpredis-develop \  
&& rm -f phpredis.zip  
ADD docker_config/redis.ini /usr/local/etc/php/conf.d/redis.ini  
  
# mail  
COPY docker_config/sendmail.ini /usr/local/etc/php/conf.d/sendmail.ini  
COPY docker_config/ssmtp.conf /etc/ssmtp/ssmtp.conf  
  
# php  
ADD docker_config/php.ini /usr/local/etc/php/conf.d/php.ini  
  
# apache  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
RUN mkdir -p /etc/apache2/certs  
RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 \  
-keyout /etc/apache2/certs/localhost.key \  
-out /etc/apache2/certs/localhost.crt \  
-subj \  
"/C=US/ST=CA/O=localhost/OU=Engineering/CN=localhost/emailAddress=ssl@localhost"  
ADD docker_config/000-default.conf /etc/apache2/sites-enabled/000-default.conf  
  
EXPOSE 80  
CMD /usr/sbin/apache2ctl -D FOREGROUND  

