FROM ubuntu:16.04  
  
# Add the repository for PHP7.1  
# Notice: Have to set LC_ALL to avoid stuff blowing up  
RUN apt-get update -y \  
&& apt-get upgrade -y \  
&& apt-get install -y python-software-properties software-properties-common \  
&& LC_ALL=C.UTF-8 add-apt-repository -y ppa:ondrej/php  
  
RUN apt-get update && apt-get install -y \  
libapache2-mod-php7.1 \  
php7.1 \  
php7.1-cli \  
php7.1-common \  
php7.1-json \  
php7.1-opcache \  
php7.1-readline \  
php7.1-xml \  
php7.1-dev \  
php7.1-mysql \  
php7.1-mcrypt \  
php7.1-soap \  
php7.1-snmp \  
php7.1-pgsql \  
php7.1-sybase \  
php7.1-mbstring \  
php7.1-gd \  
php7.1-xml \  
php7.1-curl \  
git \  
git-core \  
subversion  
  
# Install xdebug (not enabled or configured! See README)  
RUN cd /tmp \  
&& git clone git://github.com/xdebug/xdebug.git \  
&& cd xdebug \  
&& phpize \  
&& ./configure --enable-xdebug \  
&& make \  
&& make install \  
&& echo "zend_extension="`find /usr/lib/php -iname 'xdebug.so'` >
/etc/php/7.1/mods-available/xdebug.ini \  
&& cat ./xdebug.ini >> /etc/php/7.1/mods-available/xdebug.ini  
  
# Enable "modrewrite" apache2 mod  
RUN a2enmod rewrite  
  
# Provide a vhost for easy testing. Just mount (-v) some local path to
/var/www/docker-web  
RUN mkdir /var/www/docker-web  
ADD ./docker-web.vhost.conf /etc/apache2/sites-enabled/docker-web.vhost.conf  
  
# Change default vhost content  
RUN mv /var/www/html/index.html /var/www/html/orig.index.html  
RUN echo '<?php phpinfo();' > /var/www/html/index.php  
  
# Ensure apahe2 is started  
ENTRYPOINT ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

