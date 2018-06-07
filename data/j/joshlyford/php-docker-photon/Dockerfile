FROM php:7-fpm  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libgraphicsmagick1-dev \  
libjpeg-dev \  
libpng-dev \  
libtiff-dev \  
libgif-dev \  
libmagickcore-dev libmagickwand-dev libmagick++-dev \  
optipng --no-install-recommends \  
jpegoptim \  
pngquant \  
graphicsmagick \  
libwebp-dev \  
wget \  
git \  
nano \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt sockets zip \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd  
  
ENV TERM xterm  
ENV PHOTON_DOCKER_VERSION 0.9.1  
ENV WEBP_VERSION 0.5.0  
WORKDIR /tmp  
RUN /bin/bash -c 'echo WEBP && \  
wget -q
"http://downloads.webmproject.org/releases/webp/libwebp-0.5.0-linux-x86-64.tar.gz"
&& \  
tar -xf libwebp-0.5.0-linux-x86-64.tar.gz && cd libwebp-0.5.0-linux-x86-64/bin
&& \  
mv cwebp gif2webp /usr/local/bin/'  
  
RUN pecl install gmagick-2.0.1RC1  
  
RUN /bin/bash -c 'echo "expose_php=Off" >> "/usr/local/etc/php/conf.d/custom-
config.ini" && \  
echo "extension=gmagick.so" >> "/usr/local/etc/php/conf.d/ext-gmagick.ini" &&
\  
echo "date.timezone=UTC" >> "/usr/local/etc/php/conf.d/timezone.ini" && \  
echo "zend_extension=opcache.so" >> "/usr/local/etc/php/conf.d/ext-
opcache.ini" && \  
echo "opcache.enable_cli=1" >> "/usr/local/etc/php/conf.d/ext-opcache.ini" &&
\  
echo "opcache.memory_consumption=128" >> "/usr/local/etc/php/conf.d/ext-
opcache.ini" && \  
echo "opcache.interned_strings_buffer=8" >> "/usr/local/etc/php/conf.d/ext-
opcache.ini" && \  
echo "opcache.max_accelerated_files=4000" >> "/usr/local/etc/php/conf.d/ext-
opcache.ini" && \  
echo "opcache.fast_shutdown=1" >> "/usr/local/etc/php/conf.d/ext-opcache.ini"'  
  
  
# tweak php-fpm config  
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g" /usr/local/etc/php-
fpm.d/www.conf && \  
sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 1000M/g"
/usr/local/etc/php-fpm.d/www.conf && \  
sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 1000M/g"
/usr/local/etc/php-fpm.d/www.conf && \  
sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /usr/local/etc/php-
fpm.d/www.conf && \  
sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g"
/usr/local/etc/php-fpm.d/www.conf && \  
sed -i -e "s/pm = dynamic/pm = ondemand/g" /usr/local/etc/php-fpm.d/www.conf
&& \  
sed -i -e "s/pm.max_children = 5/pm.max_children = 40/g" /usr/local/etc/php-
fpm.d/www.conf && \  
sed -i -e "s/pm.start_servers = 2/pm.start_servers = 20/g" /usr/local/etc/php-
fpm.d/www.conf && \  
sed -i -e "s/pm.min_spare_servers = 1/pm.min_spare_servers = 10/g"
/usr/local/etc/php-fpm.d/www.conf && \  
sed -i -e "s/pm.max_spare_servers = 3/pm.max_spare_servers = 20/g"
/usr/local/etc/php-fpm.d/www.conf && \  
sed -i -e "s/;pm.max_requests = 500/pm.max_requests = 500/g"
/usr/local/etc/php-fpm.d/www.conf && \  
sed -i -e "s/;pm.process_idle_timeout = 10s/pm.process_idle_timeout = 10s/g"
/usr/local/etc/php-fpm.d/www.conf  
  
  
  
  
# install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
WORKDIR /var/www/html

