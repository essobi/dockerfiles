############################################################  
# Dockerfile to build Idephix Container (http://getidephix.com)  
############################################################  
  
# Set the base image to Ubuntu  
FROM ideato/centos7_base  
  
# File Author / Maintainer  
MAINTAINER Paolo Tonin <pt@ideato.it> Alessandro Mazzoli <am@ideato.it>  
  
ONBUILD RUN yum -y update  
  
# Installing required PHP 5.6 for Idephix  
RUN yum -y --enablerepo=remi,remi-php56 install php-common \  
php-cli \  
php-curl \  
php-bcmath \  
php-gd \  
php-intl \  
php-json \  
php-mbstring \  
php-mcrypt \  
php-mysqlnd \  
php-opcache \  
php-pdo \  
php-xml \  
php-xmlrpc \  
php-pecl-imagick  
  
# Installing Composer  
RUN curl -sS https://getcomposer.org/installer | php && chmod a+x
composer.phar && mv composer.phar /usr/local/bin/composer  
  
# Installing Idephix  
RUN curl http://getidephix.com/idephix.phar > /usr/local/bin/idx && chmod +x
/usr/local/bin/idx  
  
# setting up php.ini  
RUN sed -i "s/memory_limit = .*/memory_limit = 2048M/" /etc/php.ini  
RUN sed -i "s/;date.timezone =/date.timezone = Europe\/Rome/" /etc/php.ini  
RUN sed -i "s/error_reporting = E_ALL & ~E_DEPRECATED &
~E_STRICT/error_reporting = E_ALL/" /etc/php.ini  

