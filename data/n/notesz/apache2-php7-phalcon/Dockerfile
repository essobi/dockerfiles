FROM ubuntu:16.04  
MAINTAINER Norbert Lakatos <norbert@innobotics.eu>  
  
# Install apache, php, etc...  
RUN apt-get update && \  
apt-get install -y \  
apache2 \  
php7.0 \  
php7.0-curl \  
php7.0-gd \  
php7.0-json \  
php7.0-mysql \  
php7.0-intl \  
php7.0-mbstring \  
php7.0-mcrypt \  
libapache2-mod-php7.0 \  
php-imagick \  
php7.0-dev \  
libpcre3-dev \  
gcc \  
make  
  
# Environment variables  
ENV APACHE_APPLICATION_ENV dev  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
  
# Enable php error display  
RUN sed -ri 's/^display_errors\s*=\s*Off/display_errors = On/g'
/etc/php/7.0/apache2/php.ini  
RUN sed -ri 's/^display_errors\s*=\s*Off/display_errors = On/g'
/etc/php/7.0/cli/php.ini  
RUN sed -ri "s/^error_reporting\s*=.*$//g" /etc/php/7.0/apache2/php.ini  
RUN sed -ri "s/^error_reporting\s*=.*$//g" /etc/php/7.0/cli/php.ini  
RUN echo "error_reporting = E_ALL & ~E_DEPRECATED & ~E_NOTICE" >>
/etc/php/7.0/apache2/php.ini  
RUN echo "error_reporting = E_ALL & ~E_DEPRECATED & ~E_NOTICE" >>
/etc/php/7.0/cli/php.ini  
  
# Build and configure phalcon  
RUN mkdir /root/tmp  
ADD https://github.com/phalcon/cphalcon/archive/v3.0.3.tar.gz
/root/tmp/phalcon.tar.gz  
WORKDIR /root/tmp  
RUN tar -xzf phalcon.tar.gz  
WORKDIR /root/tmp/cphalcon-3.0.3/build  
RUN ./install  
RUN /bin/echo 'extension=phalcon.so' >
/etc/php/7.0/apache2/conf.d/30-phalcon.ini  
RUN /bin/echo 'extension=phalcon.so' > /etc/php/7.0/cli/conf.d/30-phalcon.ini  
  
RUN /usr/sbin/a2enmod rewrite  
  
# Make default dir and index.php  
RUN /bin/rm /var/www/html/index.html  
RUN /bin/rmdir /var/www/html  
RUN /bin/mkdir /var/www/public  
RUN /bin/echo '<html><body><?php phpinfo(); ?></body></html>' >
/var/www/public/index.php  
WORKDIR /var/www  
  
# Configure default servername  
RUN echo 'ServerName localhost' >> /etc/apache2/apache2.conf  
  
# Configure default vhost  
RUN echo '<VirtualHost *:80>' > /etc/apache2/sites-available/000-default.conf  
RUN echo ' ServerAdmin norbert@innobotics.eu' >> /etc/apache2/sites-
available/000-default.conf  
RUN echo ' SetEnv APPLICATION_ENV "${APACHE_APPLICATION_ENV}"' >>
/etc/apache2/sites-available/000-default.conf  
RUN echo ' DocumentRoot /var/www/public' >> /etc/apache2/sites-
available/000-default.conf  
RUN echo ' <Directory />' >> /etc/apache2/sites-available/000-default.conf  
RUN echo ' Options FollowSymLinks' >> /etc/apache2/sites-
available/000-default.conf  
RUN echo ' AllowOverride All' >> /etc/apache2/sites-available/000-default.conf  
RUN echo ' </Directory>' >> /etc/apache2/sites-available/000-default.conf  
RUN echo ' <Directory /var/www/>' >> /etc/apache2/sites-
available/000-default.conf  
RUN echo ' Options Indexes FollowSymLinks MultiViews' >> /etc/apache2/sites-
available/000-default.conf  
RUN echo ' AllowOverride All' >> /etc/apache2/sites-available/000-default.conf  
RUN echo ' Order allow,deny' >> /etc/apache2/sites-available/000-default.conf  
RUN echo ' allow from all' >> /etc/apache2/sites-available/000-default.conf  
RUN echo ' </Directory>' >> /etc/apache2/sites-available/000-default.conf  
RUN echo ' ErrorLog ${APACHE_LOG_DIR}/error.log' >> /etc/apache2/sites-
available/000-default.conf  
RUN echo ' CustomLog ${APACHE_LOG_DIR}/access.log combined' >>
/etc/apache2/sites-available/000-default.conf  
RUN echo '</VirtualHost>' >> /etc/apache2/sites-available/000-default.conf  
  
# Set docroot volume  
VOLUME ["/var/www"]  
  
# Set port  
EXPOSE 80  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

