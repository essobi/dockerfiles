FROM php:5.6-fpm  
  
# set environment  
ENV COMPOSER_HOME=/root/composer \  
PATH=$COMPOSER_HOME/vendor/bin:$PATH \  
COMPOSER_ALLOW_SUPERUSER=1 \  
PHALCON_VERSION=3.2.4  
RUN apt-get update  
  
# package install  
RUN apt-get install -y zlib1g-dev curl libcurl3 libcurl4-gnutls-dev libicu-dev  
RUN docker-php-ext-install pdo pdo_mysql zip curl mbstring intl  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer && \  
chmod +x /usr/local/bin/composer && \  
composer --ansi --version  
  
# set packagist.jp  
RUN composer config -g repos.packagist composer https://packagist.jp  
  
# install prestissimo  
RUN mkdir -p $COMPOSER_HOME && \  
composer global require hirak/prestissimo  
  
# install phalcon  
RUN curl -sSL
"https://codeload.github.com/phalcon/cphalcon/tar.gz/v${PHALCON_VERSION}" |
tar -xz \  
&& cd cphalcon-${PHALCON_VERSION}/build \  
&& ./install \  
&& cp ../tests/_ci/phalcon.ini $(php-config --configure-options | grep -o
"with-config-file-scan-dir=\\([^ ]*\\)" | awk -F'=' '{print $2}') \  
&& cd ../../ \  
&& rm -r cphalcon-${PHALCON_VERSION}  
  
# install memcached  
RUN apt-get install -y libz-dev libmemcached-dev && \  
pecl install memcached-2.2.0 && \  
docker-php-ext-enable memcached  
  
RUN apt-get install locales  
RUN echo "LC_ALL=en_US.UTF-8" >> /etc/environment  
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen  
RUN echo "LANG=en_US.UTF-8" > /etc/locale.conf  
RUN locale-gen ja_JP.UTF-8  
ENV LANG ja_JP.UTF-8  
ENV LC_CTYPE ja_JP.UTF-8  
RUN localedef -f UTF-8 -i ja_JP ja_JP.utf8  

