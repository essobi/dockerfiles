FROM jazzypro/ubuntu-frontend:latest  
  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
  
#  
# Add repositories and update packages list  
#  
RUN apt-add-repository ppa:ondrej/php -y  
RUN apt-get update  
  
#  
# Install PHP 5.6 and 7.0, set 5.6 as default  
#  
RUN apt-get install -y php5.6-apcu php5.6-cli php5.6-curl php5.6-fpm php5.6-gd
php5.6-imagick php5.6-intl php5.6-json php5.6-ldap php5.6-mbstring
php5.6-mcrypt php5.6-memcached php5.6-mongo php5.6-mysql php5.6-pgsql
php5.6-readline php5.6-redis php5.6-sqlite php5.6-xdebug php5.6-xml php5.6-zip  
RUN apt-get install -y php7.0-apcu php7.0-cli php7.0-curl php7.0-fpm php7.0-gd
php7.0-imagick php7.0-intl php7.0-json php7.0-ldap php7.0-mbstring
php7.0-mcrypt php7.0-memcached php7.0-mongo php7.0-mysql php7.0-pgsql
php7.0-readline php7.0-redis php7.0-sqlite php7.0-xdebug php7.0-xml php7.0-zip  
RUN update-alternatives --set php /usr/bin/php5.6  
RUN apt-get install -y php-pear  
RUN php -v  
RUN echo $(php -v) >> /root/soft_versions  
  
#  
# Set php.ini timezone  
#  
RUN sed -i".bak" "s/^\;date\\.timezone.*$/date\\.timezone = \"Europe\/Warsaw\"
/g" /etc/php/5.6/fpm/php.ini  
RUN sed -i".bak" "s/^\;date\\.timezone.*$/date\\.timezone = \"Europe\/Warsaw\"
/g" /etc/php/5.6/cli/php.ini  
RUN sed -i".bak" "s/^\;date\\.timezone.*$/date\\.timezone = \"Europe\/Warsaw\"
/g" /etc/php/7.0/fpm/php.ini  
RUN sed -i".bak" "s/^\;date\\.timezone.*$/date\\.timezone = \"Europe\/Warsaw\"
/g" /etc/php/7.0/cli/php.ini  
  
#  
# Install PHPUnit  
#  
RUN wget -O /bin/phpunit https://phar.phpunit.de/phpunit.phar && chmod a+x
/bin/phpunit  
  
#  
# Install Composer  
#  
RUN wget -O /bin/composer https://getcomposer.org/composer.phar && chmod a+x
/bin/composer  
  
#  
# Enable XDebug  
#  
RUN echo "xdebug.remote_enable=1" >> /etc/php/5.6/mods-available/xdebug.ini \  
&& echo "xdebug.default_enable=1" >> /etc/php/5.6/mods-available/xdebug.ini \  
&& echo "xdebug.remote_autostart=1" >> /etc/php/5.6/mods-available/xdebug.ini
\  
&& echo "xdebug.remote_host=127.0.0.1" >> /etc/php/5.6/mods-
available/xdebug.ini \  
&& echo "xdebug.profiler_enable=1" >> /etc/php/5.6/mods-available/xdebug.ini  
RUN echo "xdebug.remote_enable=1" >> /etc/php/7.0/mods-available/xdebug.ini \  
&& echo "xdebug.default_enable=1" >> /etc/php/7.0/mods-available/xdebug.ini \  
&& echo "xdebug.remote_autostart=1" >> /etc/php/7.0/mods-available/xdebug.ini
\  
&& echo "xdebug.remote_host=127.0.0.1" >> /etc/php/7.0/mods-
available/xdebug.ini \  
&& echo "xdebug.profiler_enable=1" >> /etc/php/7.0/mods-available/xdebug.ini  

