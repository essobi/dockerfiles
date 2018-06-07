FROM alpine:edge  
  
MAINTAINER Juliano Petronetto <juliano@petronetto.com.br>  
  
# Install packages  
RUN apk --update add \  
php7 \  
php7-dom \  
php7-fpm \  
php7-mbstring \  
php7-mcrypt \  
php7-opcache \  
php7-pdo \  
php7-pdo_mysql \  
php7-pdo_pgsql \  
php7-xml \  
php7-phar \  
php7-openssl \  
php7-json \  
php7-ctype \  
php7-session \  
php7-xdebug \  
php7-mysqlnd \  
php7-curl \  
php7-gd \  
php7-intl \  
php7-posix \  
php7-iconv \  
curl \  
vim \  
  
# Cleanup  
&& rm -rf /var/cache/apk/*  
  
# Creating symbolic link to php  
RUN ln -s /usr/bin/php7 /usr/bin/php  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer  
  
# Configure XDebug  
COPY xdebug.ini /etc/php7/conf.d/xdebug.ini  
  
# Configure the container bootstrap  
COPY start-container /usr/local/bin/start-container  
RUN chmod +x usr/local/bin/start-container  
  
EXPOSE 80  
CMD ["start-container"]  

