FROM ubuntu:16.04  
MAINTAINER Frank Perez <frank@fjp.io>  
  
ENV LC_ALL C.UTF-8  
RUN apt update -y  
  
RUN apt install -y nginx  
  
RUN apt install -y supervisor vim software-properties-common python-software-
properties  
  
RUN add-apt-repository -y ppa:ondrej/php  
  
RUN apt-key update && apt update -y  
  
RUN apt-get install -y php7.0-cli \  
php7.0-mysql \  
php7.0-sqlite3 \  
php7.0-gd \  
php7.0-apcu \  
php7.0-mcrypt \  
php7.0-gmp \  
php7.0-curl \  
php7.0-imap \  
php7.0-memcached \  
php7.0-readline \  
php7.0-imagick \  
php7.0-intl \  
php7.0-xdebug \  
php7.0-fpm  
  
RUN mkdir -p /run/php  
  
COPY configurations/nginx-php70.conf /etc/nginx/sites-available/default  
  
COPY scripts/start.sh /start.sh  
RUN chmod 755 /start.sh  
  
WORKDIR /var/www/html  
  
CMD "/start.sh"  
  
EXPOSE 22 80  

