FROM php:7.1-fpm  
MAINTAINER Plopix  
  
RUN apt-get update -q -y && apt-get install -q -y --force-yes \--no-install-
recommends build-essential libxml2-dev libmemcached-dev libmemcached11 libssl-
dev libfreetype6-dev rsync \  
libcurl4-openssl-dev libmagickwand-dev libmagickcore-dev libjpeg62-turbo-dev
libmcrypt-dev libxpm-dev libpng12-dev libicu-dev libxslt1-dev ca-certificates
openssl \  
mysql-client python openssh-client default-jre curl unzip git imagemagick wget
gnupg jpegoptim && \  
rm -rf /var/lib/apt/lists/* && \  
mkdir -p /root/.ssh && ssh-keyscan -H github.com >> /etc/ssh/ssh_known_hosts  
  
RUN curl -s https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install -q -y --force-yes --no-install-recommends nodejs && npm
install -g uglify-js && npm install -g uglifycss  
  
ADD http://pngquant.org/pngquant-2.11.0-src.tar.gz /usr/src  
RUN cd /usr/src && \  
tar xvzf pngquant-2.11.0-src.tar.gz && \  
cd pngquant-2.11.0 && make && make install && \  
cd .. && rm pngquant-2.11.0-src.tar.gz && rm -rf pngquant-2.11.0  
  
RUN docker-php-ext-configure mysqli --with-mysqli=mysqlnd && \  
docker-php-ext-configure pdo_mysql --with-pdo-mysql=mysqlnd && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \--with-png-dir=/usr/include/ \--with-xpm-dir=/usr/include/
\--enable-gd-jis-conv && \  
echo "autodetect" | pecl install imagick && \  
echo "no" | pecl install mongodb && \  
echo "no" | pecl install redis && \  
echo "no" | pecl install memcached && \  
docker-php-ext-enable memcached mongodb opcache imagick redis && \  
docker-php-ext-install mysqli pdo_mysql iconv mcrypt exif gd pcntl intl curl
xsl xml json zip  
  
RUN curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s
https://blackfire.io/api/v1/releases/probe/php/linux/amd64/$(php -r "echo
PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") && \  
tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp && \  
mv /tmp/blackfire-*.so $(php -r "echo ini_get('extension_dir');")/blackfire.so
&& rm /tmp/blackfire-probe.tar.gz  
  
CMD ["php-fpm"]  

