FROM ubuntu:xenial  
  
RUN apt-get update \  
&& apt-get install -y php7.0 php7.0-xml php7.0-mbstring php7.0-fpm php7.0-cli
php7.0-json php7.0-curl php7.0-gd \  
php7.0-mysqlnd php7.0-imap php7.0-mcrypt php7.0-zip php7.0-intl php7.0-dev \  
pkg-config php-pear libcurl4-openssl-dev libssl-dev libsslcommon2-dev \  
&& pecl install mongodb \  
&& echo "extension=mongodb.so" >> `php --ini | grep "Loaded Configuration" |
sed -e "s|.*:\s*||"` \  
&& echo "extension=mongodb.so" >> /etc/php/7.0/fpm/php.ini \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  

