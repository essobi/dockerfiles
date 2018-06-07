FROM php:7.1-fpm  
  
MAINTAINER Eric Poe <eric.poe@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV TERM xterm  
ENV LANG C.UTF-8  
ENV LC_ALL C.UTF-8  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install -y \  
apt-transport-https \  
ca-certificates \  
lsb-release \  
python-software-properties \  
software-properties-common \  
wget && \  
wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg
&& \  
echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" >
/etc/apt/sources.list.d/php.list  
  
RUN apt-get update && apt-get upgrade -y  
  
RUN apt-get install -y \  
git \  
nginx \  
php-apcu \  
php7.1-cli \  
php7.1-curl \  
php7.1-fpm \  
php7.1-mbstring \  
php7.1-xml \  
unzip \  
zip  
  
# # Install GD extension  
RUN apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng12-dev && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install -j$(nproc) gd  
  
# # Install ZIP extension  
RUN apt-get install -y \  
zlib1g-dev && \  
docker-php-ext-install -j$(nproc) zip  
  
# Install Grav  
RUN mkdir /tmp/grav && \  
wget -O /tmp/grav/grav.zip https://getgrav.org/download/core/grav/latest && \  
cd /tmp/grav && \  
unzip grav.zip && \  
cp -a /tmp/grav/grav/* /var/www/html/ && \  
mkdir /tmp/gravuser && \  
mv /tmp/grav/grav/user/* /tmp/gravuser && \  
rm -Rf /tmp/grav/  
  
RUN find /var/www/html -type f -exec chmod 664 {} \; && \  
find /var/www/html -type d -exec chmod 775 {} \; && \  
find /var/www/html -type d -exec chmod +s {} \; && \  
cd /var/www/html && \  
umask 0002  
  
WORKDIR /var/www/html  
  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
RUN chmod +x bin/gpm && \  
chmod +x bin/grav && \  
chmod +x bin/plugin && \  
chmod 777 -Rf user && \  
chmod +s -Rf user && \  
cd user && \  
umask 0002  
  
RUN chown -hR www-data:www-data /var/www/html  
  
USER "www-data"  
CMD ["php", "/var/www/html/bin/composer.phar", "self-update"]  
CMD ["php", "/var/www/html/bin/composer.phar", "install", "--no-dev", "-o"]  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["php-fpm"]  
ENV DEBIAN_FRONTEND teletype

