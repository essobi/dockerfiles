FROM ubuntu:16.04  
LABEL maintainer="paolobanez@gmail.com"  
  
# Install apache, PHP, and supplimentary programs. curl, and lynx-cur are for
debugging the container.  
RUN apt-get update && apt-get -y upgrade && DEBIAN_FRONTEND=noninteractive  
RUN apt-get -y install imagemagick  
RUN apt-get -y install vim apache2 php libapache2-mod-php php-mcrypt php-curl
php-cli php-common php-json php-mysql php-readline php-mbstring php-xml php-
imagick php-zip curl php-intl lynx-cur php-soap poppler-utils  
  
# Enable apache mods.  
RUN a2enmod php7.0  
RUN a2enmod rewrite  
  
# Update the PHP.ini file  
RUN sed -i "s/memory_limit = 128M/memory_limit = 500M/"
/etc/php/7.0/apache2/php.ini  
RUN sed -i "s/post_max_size = 8M/post_max_size = 25M/"
/etc/php/7.0/apache2/php.ini  
RUN sed -i "s/upload_max_filesize = 2M/upload_max_filesize = 25M/"
/etc/php/7.0/apache2/php.ini  
  
# Manually set up the apache environment variables  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
  
RUN mkdir /tmp/composer/ && \  
cd /tmp/composer && \  
curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer && \  
chmod a+x /usr/local/bin/composer && \  
cd / && \  
rm -rf /tmp/composer  
  
# Expose apache.  
EXPOSE 80  
# Suppress error on apache2  
RUN echo 'ServerName localhost' >> /etc/apache2/apache2.conf  
  
# Update the default apache site with the config we created.  
ADD apache-config.conf /etc/apache2/sites-enabled/000-default.conf  
  
# set permission  
ENV SITE_PATH /var/www/site  
RUN mkdir ${SITE_PATH}  
RUN chmod a+x ${SITE_PATH}  
RUN chown -R www-data:www-data ${SITE_PATH}  
RUN chmod -R 775 ${SITE_PATH}  
RUN adduser root www-data  
  
# By default start up apache in the foreground  
CMD /usr/sbin/apache2ctl -D FOREGROUND  

