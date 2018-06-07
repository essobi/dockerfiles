FROM php:5-fpm-alpine  
  
RUN apk add --no-cache openssh-client nginx supervisor curl gzip tzdata \  
bash jq autoconf g++ make openssl openssl-dev git libmcrypt-dev libpng  
  
COPY conf/fastcgi_params conf/nginx.conf /etc/nginx/  
COPY conf/nginx-site.conf /etc/nginx/sites-enabled/default.conf  
COPY conf/api.conf /etc/nginx/sites-enabled/api.conf  
  
COPY conf/supervisord.conf /etc/  
  
# Install the PHP extensions we need  
#RUN docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr  
RUN docker-php-ext-install pcntl bcmath opcache zip mcrypt mbstring >
/dev/null 2>&1  
  
# Install PHP pecl mongo  
COPY bin/* /usr/local/bin/  
RUN yes 'no' | pecl install mongo  
RUN echo 'extension=mongo.so' >> /usr/local/etc/php/conf.d/mongo.ini  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Set recommended PHP.ini settings  
# See https://secure.php.net/manual/en/opcache.installation.php  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=60'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
# Download and install Learning Locker  
# Upstream tarballs include ./learninglocker-v1.11.0/ so this gives us
/var/www/html  
RUN mkdir -p /var/www/html  
  
WORKDIR /tmp  
  
RUN curl -L -o learninglocker.tar.gz `curl -s
https://api.github.com/repos/LearningLocker/learninglocker/releases/latest |
jq --raw-output '.tarball_url'`\  
&& tar -xzf learninglocker.tar.gz -C /var/www/html --strip-components=1 \  
&& rm learninglocker.tar.gz \  
&& chown -R www-data /var/www/html  
  
RUN mkdir -p /var/www/api && ln -s /var/www/html/public /var/www/api/ll &&
chown www-data /var/www/api/ll  
RUN chown -R www-data:www-data /var/lib/nginx  
  
USER www-data  
  
WORKDIR /var/www/html  
RUN composer install  
RUN mkdir -p /var/www/html/public/js-localization/ && cp vendor/andywer/js-
localization/public/js/localization.js /var/www/html/public/js-
localization/localization.js  
EXPOSE 80  
EXPOSE 81  
USER root  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]  

