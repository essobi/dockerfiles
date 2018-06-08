FROM atlassian/default-image  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install mariadb-server/trusty-
updates  
  
# Add repo for php 7  
RUN apt-get -y install python-software-properties  
RUN LC_ALL=C.UTF-8 add-apt-repository -y ppa:ondrej/php  
  
# Add repo for varnish  
RUN apt-get -y install apt-transport-https  
RUN curl https://repo.varnish-cache.org/GPG-key.txt | apt-key add -  
RUN echo "deb https://repo.varnish-cache.org/ubuntu/ trusty varnish-4.0" >>
/etc/apt/sources.list.d/varnish-cache.list  
  
RUN apt-get update  
RUN apt-get -y install \  
php7.0/trusty \  
php7.0-bcmath/trusty \  
php7.0-cli/trusty \  
php7.0-curl/trusty \  
php7.0-dev/trusty \  
php7.0-fpm/trusty \  
php7.0-gd/trusty \  
php7.0-mbstring/trusty \  
php7.0-mysql/trusty \  
php7.0-opcache/trusty \  
php7.0-soap/trusty \  
php7.0-xml/trusty  
  
RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar
/usr/bin/composer  
  
RUN COMPOSER_ALLOW_SUPERUSER=1 composer global require drush/drush:8.x  
RUN COMPOSER_ALLOW_SUPERUSER=1 composer global update  
ENV
PATH=/root/.composer/vendor/bin:/root/.nvm:/bin/versions/node/v4.2.1/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
RUN npm install -g npm  
RUN npm install -g bower grunt-cli yo  
  
RUN apt-get -y install apache2/trusty-updates  
  
RUN a2enmod proxy_fcgi setenvif rewrite  
RUN a2enconf php7.0-fpm  
  
RUN apt-get -y install varnish  
  
COPY root /  
  

