FROM ubuntu:latest  
  
ENV ENVIRONMENT local  
  
# Install development packages  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y -q \  
apache2 \  
mysql-server \  
php7.0 \  
php7.0-common \  
php7.0-fpm \  
php7.0-mysql \  
php7.0-mbstring \  
php7.0-xml \  
php7.0-curl \  
unzip \  
curl \  
git  
  
# Install composer global bin  
RUN curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer  
  
# Install Drush  
RUN php -r "readfile('http://files.drush.org/drush.phar');" > drush && \  
chmod +x drush && \  
mv drush /usr/local/bin  
  
RUN a2enmod rewrite  
ADD ./001-docker.conf /etc/apache2/sites-available/  
RUN ln -s /etc/apache2/sites-available/001-docker.conf /etc/apache2/sites-
enabled/  
  
# Fixes issues with Apache startup  
RUN mkdir /var/lock/apache2  
RUN mkdir /var/www/src  
  
# Adds area for ssh keys  
RUN mkdir /root/.ssh  
RUN ssh-keyscan bitbucket.org >> /root/.ssh/known_hosts  
  
# Set Apache environment variables (can be changed on docker run with -e)  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_SERVERADMIN admin@localhost  
ENV APACHE_SERVERNAME localhost  
ENV APACHE_SERVERALIAS docker.localhost  
ENV APACHE_DOCUMENTROOT /var/www/src  
  
RUN service apache2 start && service mysql start  
  
# Expose Ports  
EXPOSE 443  
EXPOSE 80  
ADD start.sh /start.sh  
RUN chmod 0755 /start.sh  
CMD ["bash", "start.sh"]

