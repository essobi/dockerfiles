FROM alpine:3.5  
MAINTAINER Simon Ball <contact@simonball.me>  
  
ENV PHING_VERSION="2.15.2"  
  
RUN apk --update add \  
php7 \  
php7-bcmath \  
php7-dom \  
php7-ctype \  
php7-curl \  
php7-gd \  
php7-iconv \  
php7-intl \  
php7-json \  
php7-mbstring \  
php7-mcrypt \  
php7-mysqlnd \  
php7-opcache \  
php7-openssl \  
php7-pdo \  
php7-pdo_mysql \  
php7-pdo_sqlite \  
php7-phar \  
php7-posix \  
php7-session \  
php7-soap \  
php7-xdebug \  
php7-xml \  
php7-zip \  
php7-zlib \  
# Command line tools  
autoconf \  
bash \  
ca-certificates \  
curl \  
git \  
libsasl \  
nodejs \  
openssh \  
&& ssh-keygen -A \  
&& rm -rf /var/cache/apk/*  
  
# Symlink PHP7 to be runnable as php  
RUN ln -s /usr/bin/php7 /usr/bin/php  
  
# Enable xDebug  
RUN echo "zend_extension=xdebug.so" > /etc/php7/conf.d/xdebug.ini  
  
# Grab the latest Symfony dedicated installer  
RUN curl -LsS https://symfony.com/installer -o /usr/local/bin/symfony && \  
chmod a+x /usr/local/bin/symfony && \  
symfony --version  
  
# Grab the latest Composer install  
RUN curl -sS https://getcomposer.org/installer | \  
php -- --install-dir=/usr/local/bin --filename=composer && \  
composer --version  
  
# Install PHPUnit  
RUN curl -LsS https://phar.phpunit.de/phpunit.phar \  
-o /usr/local/bin/phpunit && \  
chmod a+x /usr/local/bin/phpunit && phpunit --version  
  
# Install Phing  
RUN curl -LsS http://www.phing.info/get/phing-$PHING_VERSION.phar \  
-o /usr/local/bin/phing && \  
chmod +x /usr/local/bin/phing && \  
phing -v  
  
# GulpJS task runner  
RUN npm install gulp -g && gulp -v  
# bower package manager  
RUN npm install bower -g && bower -v  
  
CMD ["/bin/bash"]  

