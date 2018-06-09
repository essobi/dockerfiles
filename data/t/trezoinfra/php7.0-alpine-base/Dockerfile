FROM alpine:3.7  
#Add PHP.earth repository  
RUN apk add --no-cache wget ca-certificates git openssh-client \  
&& wget -O /etc/apk/keys/phpearth.rsa.pub
https://repos.php.earth/alpine/phpearth.rsa.pub \  
&& echo "https://repos.php.earth/alpine/v3.7" >> /etc/apk/repositories  
  
#Install php 7.0, FPM and extensions  
RUN apk --update --no-cache add \  
php7.0 \  
php7.0-bcmath \  
php7.0-dom \  
php7.0-ctype \  
php7.0-curl \  
php7.0-fileinfo \  
php7.0-fpm \  
php7.0-gd \  
php7.0-iconv \  
php7.0-intl \  
php7.0-json \  
php7.0-mbstring \  
php7.0-mcrypt \  
php7.0-mysqlnd \  
php7.0-opcache \  
php7.0-openssl \  
php7.0-pdo \  
php7.0-pdo_mysql \  
php7.0-pdo_pgsql \  
php7.0-pdo_sqlite \  
php7.0-phar \  
php7.0-posix \  
php7.0-simplexml \  
php7.0-session \  
php7.0-soap \  
php7.0-tokenizer \  
php7.0-xml \  
php7.0-xsl \  
php7.0-xmlreader \  
php7.0-xmlwriter \  
php7.0-zip \  
php7.0-redis \  
php7.0-memcached \  
pcre \  
&& rm -rf /var/cache/apk/*  
  
  
#Install composer  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
\  
&& php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" \  
&& php composer-setup.php \  
&& php -r "unlink('composer-setup.php');" \  
&& mv composer.phar /usr/local/bin/composer  
  
RUN adduser deploy -s /bin/sh -G www-data -u 2500 -D  
  
RUN apk del wget  
  
  
CMD ["php-fpm7.0", "-F"]  

