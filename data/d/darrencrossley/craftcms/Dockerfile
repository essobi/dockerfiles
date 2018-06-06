FROM php:7.0-apache  
  
# Update and Install Base Dependencies  
RUN apt-get update && \  
apt-get -yq install \  
wget apt-transport-https git pwgen unzip tar bzip2 \  
libz-dev \  
libsasl2-dev \  
libmagickwand-dev --no-install-recommends  
  
# Add publickey for yarn  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
# Install modules : GD mcrypt iconv  
RUN apt-get update && \  
apt-get -yq install \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
&& docker-php-ext-install iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install mbstring  
  
# install Nodejs and Yarn  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -yq nodejs yarn  
  
# install PHP pdo_mysql  
RUN docker-php-ext-install pdo pdo_mysql  
  
# Install Memcached Module  
RUN apt-get install -yq libmemcached-dev  
RUN curl -o /root/memcached.zip https://github.com/php-memcached-dev/php-
memcached/archive/php7.zip -L  
RUN cd /root && unzip memcached.zip && rm memcached.zip && \  
cd php-memcached-php7 && \  
phpize && ./configure --enable-sasl && make && make install && \  
cd /root && rm -rf /root/php-memcached-* && \  
echo "extension=memcached.so" > /usr/local/etc/php/conf.d/memcached.ini && \  
echo "memcached.use_sasl = 1" >> /usr/local/etc/php/conf.d/memcached.ini  
  
# memcached module with sasl  
RUN curl -o /root/libmemcached.tar.gz
https://launchpad.net/libmemcached/1.0/1.0.18/+download/libmemcached-1.0.18.tar.gz
-L  
RUN cd /root && tar zxvf libmemcached.tar.gz && cd libmemcached-1.0.18 && \  
./configure --enable-sasl && make && make install && \  
cd /root && rm -rf /root/libmemcached*  
  
RUN pecl install imagick-3.4.0RC4 && docker-php-ext-enable imagick  
  
RUN a2enmod rewrite  
  
# PHP Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
COPY php.ini /usr/local/etc/php/  
COPY src/ /var/www/  
  
RUN mkdir -p /var/www/craft/app  
  
# Download latest craft  
RUN ["/bin/bash", "-c", "curl -L -o /craft.zip
https://craftcms.com/latest.zip?accept_license=yes"]  
  
# Unzip craft and move app to app folder  
RUN unzip /craft.zip -d /tmp/crafty && \  
mv /tmp/crafty/craft/app/* /var/www/craft/app  
  
# log to /var/www/log  
RUN mkdir -p /var/www/log  
RUN echo "error_log = /var/www/log/php_error.log" >
/usr/local/etc/php/conf.d/log.ini  
RUN echo "log_errors = On" >> /usr/local/etc/php/conf.d/log.ini  
RUN echo "" > /etc/apache2/conf-enabled/log.conf  
  
# (Dev only)  
# RUN apt-get update && apt-get -yq install vim && curl http://j.mp/spf13-vim3
-L -o - | sh  
RUN rm -rf /var/lib/apt/lists/*  
  
WORKDIR /var/www  
  
RUN usermod -u 1000 www-data  
RUN mkdir /var/www/html/config  
RUN chown -R www-data:www-data /var/www/craft/config  
RUN chown -R www-data:www-data /var/www/craft/storage  
  
EXPOSE 80  

