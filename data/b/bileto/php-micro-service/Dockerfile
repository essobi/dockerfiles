FROM php:7.1  
# Howto from https://hub.docker.com/_/php/  
RUN echo "[*] Image uses PHP version ${PHP_VERSION}"  
  
RUN set -x \  
&& echo "[*] Prerequisities..." \  
&& cd /tmp \  
&& apt-get update \  
&& echo "[*] Installing dependencies for PHP extensions..." \  
&& apt-get install -y \  
unzip \  
libpq-dev \  
libicu52 libicu-dev \  
libpng12-dev libjpeg62-turbo-dev libfreetype6-dev \  
&& echo "[*] Installing native PHP extensions..." \  
&& docker-php-ext-install -j$(nproc) opcache pdo_pgsql intl zip bcmath pcntl
sockets \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& echo "[*] Installing PECL extensions..." \  
&& pecl install redis \  
&& docker-php-ext-enable redis \  
&& echo "[*] Installing Composer..." \  
&& curl -fsSL https://getcomposer.org/installer -o composer-setup.php \  
&& php composer-setup.php --install-dir=/usr/local/bin --filename=composer \  
&& rm -r composer-setup.php \  
&& echo "[*] Cleaning up..." \  
&& apt-get clean purge autoremove -y && rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/* \  
&& echo "[*] Done."  
  
COPY tests /usr/local/include/php/docker-tests  
  
RUN /usr/local/include/php/docker-tests/all.sh  
  
COPY php.ini /usr/local/etc/php/conf.d/zzz-php.ini  

