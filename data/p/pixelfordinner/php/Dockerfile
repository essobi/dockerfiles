FROM php:7.1-fpm-alpine  
MAINTAINER Karl Fathi <karl@pixelfordinner.com>  
  
ENV LANG C.UTF-8  
ENV IMAGICK_VERSION 3.4.3  
RUN apk add --no-cache \  
zip \  
unzip \  
less \  
mysql-client \  
git \  
su-exec  
  
# Install PHP extensions.  
# pdo_mysql  
RUN docker-php-ext-install pdo_mysql  
  
# mysqli  
RUN docker-php-ext-install mysqli  
  
# opcache  
RUN docker-php-ext-install opcache  
  
# zip  
RUN apk add --no-cache zlib-dev \  
&& docker-php-ext-install zip \  
&& apk del zlib-dev  
  
# intl  
RUN apk add --no-cache icu-dev \  
&& docker-php-ext-install intl  
  
# bz2  
RUN apk add --no-cache bzip2-dev \  
&& docker-php-ext-install bz2  
# exif  
RUN docker-php-ext-install exif  
  
# apcu  
RUN apk add --no-cache autoconf gcc g++ make \  
&& pecl install apcu \  
&& echo "extension=apcu.so" > /usr/local/etc/php/conf.d/ext-apcu.ini \  
&& apk del autoconf gcc g++ make  
  
# Imagick  
RUN apk add --no-cache imagemagick-dev libtool autoconf gcc g++ make \  
&& pecl install imagick-$IMAGICK_VERSION \  
&& echo "extension=imagick.so" > /usr/local/etc/php/conf.d/ext-imagick.ini \  
&& apk del libtool autoconf gcc g++ make  
  
# SOAP  
RUN apk add --no-cache libxml2-dev libtool autoconf gcc g++ make \  
&& docker-php-ext-install soap \  
&& apk del libtool autoconf gcc g++ make  
  
# Utilities  
# wp-cli  
ADD https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar
/usr/local/bin/wp-cli.phar  
ADD data/wp.sh /usr/local/bin/wp  
RUN chmod +rx /usr/local/bin/wp-cli.phar  
RUN chmod +x /usr/local/bin/wp  
  
# composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer.phar  
RUN chmod +rx /usr/local/bin/composer.phar  
ADD data/composer.sh /usr/local/bin/composer  
RUN chmod +x /usr/local/bin/composer  
  
RUN sed -i -e "s/pm.max_children = 5/pm.max_children = 3/g"
/usr/local/etc/php-fpm.d/www.conf  
  
# local php.ini  
COPY data/conf.d/* /usr/local/etc/php/conf.d/  
  
# Entrypoint  
COPY data/entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/entrypoint.sh  
  
RUN mkdir -p /opt/www  
  
VOLUME ["/opt/www"]  
  
EXPOSE 9000  
CMD ["entrypoint.sh"]  

