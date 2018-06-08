FROM php:7.1.3-fpm  
  
# Install SSL root cert  
ADD ssl/printed.com-RootCA.crt /usr/local/share/ca-certificates  
  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -  
RUN apt-get update \  
&& apt-get install -y \  
git \  
vim \  
nano \  
zsh \  
telnet \  
bzip2 \  
libbz2-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libghc-postgresql-libpq-dev \  
libpq-dev \  
libmemcached-dev \  
libxml2-dev \  
nodejs \  
libxslt1-dev \  
imagemagick \  
g++ zlib1g-dev libicu-dev \  
&& docker-php-ext-install mcrypt mbstring bz2 bcmath zip \  
&& docker-php-ext-configure gd -with-freetype-dir=/usr/include/ -with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-configure pgsql -with-pgsql=/usr/include/postgresql/ \  
&& docker-php-ext-install -j$(nproc) gd iconv mcrypt mbstring pdo pgsql
pdo_pgsql zip pdo_mysql soap intl xsl opcache bcmath \  
# memcached compilation  
&& git clone --branch php7 https://github.com/php-memcached-dev/php-memcached
/usr/src/php/ext/memcached \  
&& cd /usr/src/php/ext/memcached \  
&& docker-php-ext-configure memcached \  
&& docker-php-ext-install -j$(nproc) memcached \  
# xdebug  
&& pecl install xdebug-2.5.3 \  
&& docker-php-ext-enable xdebug \  
&& curl -sS https://cdn.printed.engineering/php/7.1/extensions/lua.so -o
/usr/local/lib/php/extensions/no-debug-non-zts-20160303/lua.so \  
&& docker-php-ext-enable lua  
  
RUN echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_host=10.0.2.2" >> /usr/local/etc/php/conf.d/xdebug.ini
\  
&& echo "xdebug.remote_autostart=off" >> /usr/local/etc/php/conf.d/xdebug.ini
\  
&& echo "xdebug.remote_connect_back=On" >>
/usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.profiler_enable_trigger=On" >>
/usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.idekey=PHPSTORM" >> /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "memory_limit = 128M" >> /usr/local/etc/php/conf.d/php.ini \  
&& echo "upload_max_filesize = 8M" >> /usr/local/etc/php/conf.d/php.ini  
  
# Install imagick  
RUN runtimeRequirements="libmagickwand-6.q16-dev --no-install-recommends" \  
&& apt-get update && apt-get install -y ${runtimeRequirements} \  
&& ln -s /usr/lib/x86_64-linux-gnu/ImageMagick-6.8.9/bin-Q16/MagickWand-config
/usr/bin/ \  
&& pecl install imagick-3.4.3RC1 \  
&& echo "extension=imagick.so" > /usr/local/etc/php/conf.d/ext-imagick.ini  
  
# Install bower and gulp  
RUN npm install -g bower gulp \  
# The "v" query parameter forces docker to rebuild this build layer, i.e. it's
not something  
# composer.org interprets. In practice, the latest composer version is always
installed.  
&& curl -sS "https://getcomposer.org/installer?v=1.3.1" | php \  
&& mv composer.phar /usr/bin/composer \  
&& update-ca-certificates \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /tmp/pear  
  
CMD ["php-fpm", "-F"]  
  
EXPOSE 9000  

