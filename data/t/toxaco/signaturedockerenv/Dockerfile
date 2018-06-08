FROM php:7.2.2-fpm  
ENV SSH_KEY id_efc6468efd14481c3db849b88f41b51f  
ARG host=172.18.0.1  
ENV APP_NAME Signature  
WORKDIR /var/www/html  
  
# Install sys deps  
RUN echo "deb http://http.debian.net/debian jessie-backports main" >>
/etc/apt/sources.list \  
&& echo 'APT::Install-Recommends "0";' > /etc/apt/apt.conf.d/99norecommends \  
&& apt-get update && apt-get install -y \  
git \  
vim \  
htop \  
libmcrypt-dev \  
libxml2-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng-dev \  
libmemcached-dev \  
nginx-light \  
ssh-client \  
supervisor \  
wget \  
zip \  
zlib1g-dev \  
libicu-dev \  
g++ \  
poppler-utils  
  
RUN apt-get clean -y && rm /var/lib/apt/lists/*.*  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/  
RUN docker-php-ext-install -j$(nproc) gd  
RUN docker-php-ext-configure intl  
  
# Install php libraries  
RUN pecl install mailparse  
RUN docker-php-ext-enable opcache mailparse  
RUN docker-php-ext-install \  
bcmath \  
mysqli \  
pcntl \  
pdo \  
pdo_mysql \  
zip \  
gd \  
soap \  
intl  
  
RUN yes '' | pecl install -f mcrypt  
RUN echo "extension=mcrypt.so" > /usr/local/etc/php/conf.d/mcrypt.ini  
RUN apt-get clean -y  
  
# Setup php  
RUN echo "date.timezone=UTC" > /usr/local/etc/php/conf.d/timezone.ini  
RUN echo "upload_max_filesize = 10M;" > /usr/local/etc/php/conf.d/uploads.ini
\  
&& echo "post_max_size = 11M;" >> /usr/local/etc/php/conf.d/uploads.ini  
  
# Install APCu  
RUN pecl install apcu  
RUN echo "extension=apcu.so" > /usr/local/etc/php/conf.d/apcu.ini  
  
# Install Memcached for php 7  
RUN curl -L -o /tmp/memcached.tar.gz "https://github.com/php-memcached-
dev/php-memcached/archive/php7.tar.gz" \  
&& mkdir -p /usr/src/php/ext/memcached \  
&& tar -C /usr/src/php/ext/memcached -zxvf /tmp/memcached.tar.gz --strip 1 \  
&& docker-php-ext-configure memcached \  
&& docker-php-ext-install memcached \  
&& rm /tmp/memcached.tar.gz  
  
# Install composer  
RUN wget
https://raw.githubusercontent.com/composer/getcomposer.org/1b137f8bf6db3e79a38a5bc45324414a6b1f9df2/web/installer
-O - -q | php -- && cp composer.phar /usr/local/bin/composer  
  
# Install xdebug  
# RUN pecl install xdebug \  
# && docker-php-ext-enable xdebug \  
# && sed -i '1 a xdebug.remote_autostart=true'
/usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \  
# && sed -i '1 a xdebug.idekey=phpstorm' /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
# && sed -i '1 a xdebug.remote_mode=req' /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
# && sed -i '1 a xdebug.remote_handler=dbgp' /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini \  
# && sed -i '1 a xdebug.remote_connect_back=0 '
/usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \  
# && sed -i '1 a xdebug.remote_port=9000' /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini \  
# && sed -i '1 a xdebug.remote_host=10.254.254.254'
/usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \  
# && sed -i '1 a xdebug.remote_enable=1' /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
# && sed -i '1 a xdebug.max_nesting_level=500'
/usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini  
# Install Blackfire [11/2017]  
# RUN version=$(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") \  
# && curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s
https://blackfire.io/api/v1/releases/probe/php/linux/amd64/$version \  
# && tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp \  
# && mv /tmp/blackfire-*.so $(php -r "echo
ini_get('extension_dir');")/blackfire.so \  
# && printf
"extension=blackfire.so\nblackfire.agent_socket=tcp://blackfire:8707\n" >
$PHP_INI_DIR/conf.d/blackfire.ini  
# Install node and npm  
RUN apt-get update && apt-get install -my wget gnupg  
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash -  
RUN apt-get install -y nodejs  
RUN y|npm i -g webpack && y|npm i -g typescript && y|npm i -g yarn  
  
# Configure sudoers for better dev experience ;-)  
RUN echo "Defaults umask=0002" >> /etc/sudoers \  
&& echo "Defaults umask_override" >> /etc/sudoers  
  
VOLUME /var/www/html  
VOLUME /var/lib/nginx  
VOLUME /tmp  
VOLUME /tmp/nginx  
VOLUME /tmp/nginx/cache  
VOLUME /tmp/nginx/fcgicache  
  
# Remove apt cache to make the image smaller  
RUN apt-get clean -y  
RUN rm -rf /var/lib/apt/lists/*  
RUN apt-get purge -y --auto-remove  
  
# These two commands are SUPER important!  
EXPOSE 80  
CMD ["/usr/bin/bash”]

