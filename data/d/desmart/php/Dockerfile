FROM debian:jessie-slim  
  
COPY build /build  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
apt-transport-https \  
lsb-release \  
ca-certificates \  
curl \  
&& curl -o /etc/apt/trusted.gpg.d/php.gpg
https://packages.sury.org/php/apt.gpg \  
&& echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" >
/etc/apt/sources.list.d/php.list \  
&& apt-get remove --purge -y lsb-release \  
&& /build/cleanup.sh  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
php7.1 \  
php7.1-fpm \  
php7.1-bz2 \  
php7.1-curl \  
php7.1-exif \  
php7.1-iconv \  
php7.1-mbstring \  
php7.1-mcrypt \  
php7.1-pdo \  
php7.1-pdo-mysql \  
php7.1-pdo-pgsql \  
php7.1-json \  
php7.1-phar \  
php7.1-dom \  
php7.1-gd \  
php7.1-ctype \  
git \  
unzip \  
make \  
&& /build/cleanup.sh  
  
RUN mkdir -p /run/php && chown www-data:www-data /run/php  
  
COPY container /  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
\  
&& php composer-setup.php --install-dir=/usr/local/bin --filename=composer \  
&& php -r "unlink('composer-setup.php');"  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
EXPOSE 9000  
CMD ["php-fpm7.1"]  

