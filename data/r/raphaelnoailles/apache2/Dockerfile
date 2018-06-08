FROM raphaelnoailles/baseimage:latest  
MAINTAINER Raphael Noailles <docker@noailles.de>  
  
# Set correct environment variables  
ENV HOME /root  
  
# don't ask for stupid things  
env DEBIAN_FRONTEND noninteractive  
  
# update the system  
RUN apt-get -y update && apt-get -y upgrade && dpkg-divert --local \--rename
--add /sbin/initctl && \  
ln -sf /bin/true /sbin/initctl  
  
# Start conf  
# Apache2 Install  
RUN apt-get install -y apache2 apache2-utils libapache2-mod-geoip php5-apcu \  
libapache2-mod-php5 graphicsmagick php-pear libapache2-mod-security2  
  
# PHP5 Install  
RUN apt-get install -y php5-cli php5 php5-mcrypt php5-curl php5-pgsql
php5-mysql \  
php5-common php5-fpm php5-gd php5-imagick  
  
RUN apt-get install -y php5-xsl php5-pgsql php5-mysql php5-mcrypt php5-intl \  
php5-imagick php5-geoip php5-gd php5-curl php5-common \  
php5-cli php5-cgi php5  
  
RUN apt-get install -y catdoc unrtf htmldoc unzip graphicsmagick-imagemagick-
compat ghostscript  
  
# Activate a2enmod  
RUN a2enmod rewrite  
RUN a2enmod php5  
RUN a2enmod vhost_alias  
RUN a2enmod expires  
RUN a2enmod ssl  
RUN a2enmod headers  
  
# php.ini mem  
RUN sed -i 's/memory_limit =128M /memory_limit = 512M/g'
/etc/php5/apache2/php.ini  
RUN sed -i 's/upload_max_filesize = 2M/upload_max_filesize = 512M/g'
/etc/php5/apache2/php.ini  
RUN sed -i 's/post_max_size = 8M/post_max_size = 512M/g'
/etc/php5/apache2/php.ini  
RUN sed -i 's/max_execution_time = 30/max_execution_time = 240/g'
/etc/php5/apache2/php.ini  
  
# Apache2 Sicherheit  
RUN sed -i 's/ServerTokens OS/ServerTokens Prod/g' /etc/apache2/conf-
enabled/security.conf  
RUN sed -i 's/ServerSignature On/ServerSignature Off/g' /etc/apache2/conf-
enabled/security.conf  
RUN sed -i 's/#Header set X-Content-Type-Options:/Header set X-Content-Type-
Options:/g' /etc/apache2/conf-enabled/security.conf  
RUN sed -i 's/#Header set X-Frame-Options:/Header set X-Frame-Options:/g'
/etc/apache2/conf-enabled/security.conf  
RUN echo '<DirectoryMatch "/\\.svn">\n\tRequire all denied\n</DirectoryMatch>'
>> /etc/apache2/conf-enabled/security.conf  
RUN echo '<DirectoryMatch "/\\.git">\n\tRequire all denied\n</DirectoryMatch>'
>> /etc/apache2/conf-enabled/security.conf  
  
# Apache default site anpassen  
#RUN sed -i 's#DocumentRoot /var/www/html#DocumentRoot
/var/www/htdocs\n\t\t<IfModule mpm_itk_module>\n\t\tAssignUserId www-data www-
data\n\t\tMaxClientsVHost 50\n\t\tNiceValue 10\n\t</IfModule>#g'
/etc/apache2/sites-available/000-default.conf  
RUN sed -i 's#DocumentRoot /var/www/html#DocumentRoot /var/www/htdocs#g'
/etc/apache2/sites-available/000-default.conf  
  
# Setup Composer  
RUN curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer  
  
# End conf  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME /etc/apache2/sites-available/  
VOLUME /etc/apache2/sites-enabled/  
VOLUME /var/www/  
  
EXPOSE 80 443  
# Use baseimage-docker's init system  
ADD scripts/start_apache2.sh /usr/local/bin/start_apache2.sh  
RUN chmod +x /usr/local/bin/start_apache2.sh  
CMD ["/usr/local/bin/start_apache2.sh"]  

