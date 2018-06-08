FROM ubuntu:xenial  
  
RUN apt-get update  
  
#install php7.0 and dependecies  
RUN apt-get -y install apache2 libapache2-mod-php7.0 php7.0 php7.0-mysql
php7.0-intl php7.0-curl curl php7.0-cli php7.0-common php7.0-dev php7.0-fpm
php7.0-json php7.0-mbstring php7.0-opcache php7.0-readline php7.0-soap
php7.0-xml php7.0-bcmath git zip unzip php7.0-zip  
  
# enable add-apt-repository command:  
RUN apt-get -y install software-properties-common  
  
# The main PPA for supported PHP versions with many PECL extensions  
RUN LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php  
RUN apt-get update  
  
# install composer dependecy manager  
RUN php -r "readfile('http://getcomposer.org/installer');" | php -- --install-
dir=/usr/bin/ --filename=composer  
  
#  
# install php dependecies  
COPY ./app /var/www/webapp  
WORKDIR /var/www/webapp  
  
#  
# speedup composer:  
# 1 - setup https to speedup composer. see: https://debril.org/how-to-fix-
composers-slowness.html  
RUN php /usr/bin/composer config --global repo.packagist composer
https://packagist.org  
  
# 2 - speed up composer with this library that do parallel downloads  
RUN php /usr/bin/composer -vvv global require hirak/prestissimo  
  
# fix and update  
RUN php /usr/bin/composer self-update  
  
# apache enable mod_rewrite  
RUN a2enmod rewrite  
  
#setup apache2  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
  
EXPOSE 80  
CMD /usr/sbin/apache2ctl -D FOREGROUND  
  

