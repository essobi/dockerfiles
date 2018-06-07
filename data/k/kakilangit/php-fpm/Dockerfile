FROM debian:jessie  
MAINTAINER kakilangit <theguywhodrinkscoffeeandcodes@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# https://secure.php.net/downloads.php  
RUN apt-get update && apt-get install -y wget apt-transport-https lsb-release
ca-certificates && wget -O /etc/apt/trusted.gpg.d/php.gpg
https://packages.sury.org/php/apt.gpg  
RUN echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" >
/etc/apt/sources.list.d/php.list  
RUN apt-get update  
RUN apt-get install -y \  
php7.1-bz2 \  
php7.1-bcmath \  
php7.1-cgi \  
php7.1-common \  
php7.1-cli \  
php7.1-curl \  
php7.1-dev \  
php7.1-enchant \  
php7.1-fpm \  
php7.1-gd \  
php7.1-gmp \  
php7.1-intl \  
php7.1-json \  
php7.1-mcrypt \  
php7.1-mysql \  
php7.1-mbstring \  
php7.1-opcache \  
php7.1-pgsql \  
php7.1-phpdbg \  
php7.1-readline \  
php7.1-recode \  
php7.1-sqlite3 \  
php7.1-tidy \  
php7.1-xsl \  
php7.1-xml \  
php7.1-xmlrpc \  
php7.1-zip  
RUN apt-get install -y \  
memcached \  
optipng \  
gifsicle \  
libjpeg-turbo-progs  
  
COPY config/php.ini /etc/php/7.1/fpm/php.ini  
COPY config/php-fpm.conf /etc/php/7.1/fpm/php-fpm.conf  
COPY config/www.conf /etc/php/7.1/fpm/pool.d/www.conf  
  
RUN rm -rf /etc/php/7.1/cli/php.ini \  
&& ln -s /etc/php/7.1/fpm/php.ini /etc/php/7.1/cli/php.ini \  
&& cd /tmp \  
&& php -r "readfile('https://getcomposer.org/installer');" | php \  
&& mv composer.phar /usr/local/bin/composer \  
&& apt-get autoremove -y \  
&& apt-get autoclean \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD ["php-fpm7.1"]  
  
EXPOSE 9000  

