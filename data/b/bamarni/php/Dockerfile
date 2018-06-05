FROM php:5-fpm  
  
# Dependencies  
# bz2 extension : libbz2-dev  
# composer : git (to install packages from source)  
# gd extension : libfreetype6-dev libjpeg-dev libpng12-dev  
# intl extension : libicu-dev  
# pdo_pgsql extension : libpq-dev  
# soap extension : libxml2-dev  
# zip extension : zlib1g-dev  
  
RUN apt-get update \  
&& apt-get -y install \  
git \  
libbz2-dev \  
libfreetype6-dev \  
libicu-dev \  
libjpeg-dev \  
libpng12-dev \  
libpq-dev \  
libxml2-dev \  
zlib1g-dev \  
&& docker-php-ext-configure gd \  
\--enable-gd-native-ttf \  
\--with-freetype-dir=/usr/include/freetype2 \  
\--with-jpeg-dir=/usr/include \  
\--with-png-dir=/usr/include \  
&& docker-php-ext-configure intl \  
&& docker-php-ext-install \  
bcmath \  
bz2 \  
gd \  
intl \  
mbstring \  
opcache \  
pcntl \  
pdo_pgsql \  
soap \  
sockets \  
zip \  
&& yes "" | pecl install apcu apcu_bc-beta hrtime mongodb redis \  
&& echo "extension=apcu.so" > $PHP_INI_DIR/conf.d/apcu.ini \  
&& echo "extension=apc.so" > $PHP_INI_DIR/conf.d/apcu_bc.ini \  
&& echo "extension=hrtime.so" > $PHP_INI_DIR/conf.d/hrtime.ini \  
&& echo "extension=mongodb.so" > $PHP_INI_DIR/conf.d/mongodb.ini \  
&& echo "extension=redis.so" > $PHP_INI_DIR/conf.d/redis.ini \  
&& chmod +x /root && mkdir /root/bin \  
&& echo "$(curl -sS https://composer.github.io/installer.sig) -" > composer-
setup.php.sig \  
&& curl -sS https://getcomposer.org/installer | tee composer-setup.php |
sha384sum -c composer-setup.php.sig \  
&& php composer-setup.php -- --install-dir=/root/bin --filename=composer \  
&& apt-get clean \  
&& rm -rf composer-setup.php* /var/lib/apt/lists/*  
  
COPY php.ini $PHP_INI_DIR/conf.d/php.ini  
  
  
  
ENV PATH="/root/bin:/root/.composer/vendor/bin:$PATH"  
ENV COMPOSER_ALLOW_SUPERUSER=1 COMPOSER_HOME=/root/.composer  

