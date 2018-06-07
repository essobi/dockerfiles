FROM ubuntu:trusty  
  
MAINTAINER Diego Ferri <diego.ferri@looptribe.com>  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive \  
apt-get -o Dpkg::Options::="--force-confnew" install -y \  
php5-cli \  
php5-curl \  
php5-dev \  
php5-gd \  
php5-intl \  
php5-mcrypt \  
php5-mysql \  
php5-sqlite \  
php5-xdebug \  
zip \  
unzip \  
git  
  
RUN php5enmod mcrypt  
  
COPY web.ini /etc/php5/cli/conf.d/90-web.ini  
  
RUN curl -sS https://getcomposer.org/installer | \  
php -- --install-dir=/usr/local/bin  

