FROM ubuntu:latest  
  
RUN apt-get update && apt-get -y upgrade && DEBIAN_FRONTEND=noninteractive
apt-get -y install \  
apache2 php7.2 php7.2-pgsql php7.2-xml php-mbstring libapache2-mod-php7.2 curl
git postgresql-client  
  
RUN a2enmod php7.2  
RUN a2enmod rewrite  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
  
EXPOSE 80  
ADD . /var/www/organization_relationships  
  
# Update the default apache site with the config we created.  
ADD apache-config.conf /etc/apache2/sites-enabled/000-default.conf  
  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/ \  
&& ln -s /usr/local/bin/composer.phar /usr/local/bin/composer  
  
WORKDIR /var/www/organization_relationships  
  
RUN composer install --prefer-source --no-interaction  
  
# By default start up apache in the foreground, override with /bin/bash for
interative.  
CMD /usr/sbin/apache2ctl -D FOREGROUND  
  
#RUN php ./vendor/bin/phinx migrate

