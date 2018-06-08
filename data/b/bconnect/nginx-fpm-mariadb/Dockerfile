FROM shito/alpine-nginx:edge  
MAINTAINER Sebastian Knoth <sk@bytepark.de>  
  
ENV DRUSH_VERSION 8.1.12  
ENV DRUPAL_INSTALL_PROFILE standard  
  
# Add PHP 7  
RUN apk upgrade -U && \  
apk --update --repository=http://dl-4.alpinelinux.org/alpine/edge/testing add
\  
openssl \  
php7 \  
php7-cli \  
php7-xml \  
php7-xsl \  
php7-pdo \  
php7-mcrypt \  
php7-curl \  
php7-json \  
php7-fpm \  
php7-phar \  
php7-openssl \  
php7-mysqli \  
php7-ctype \  
php7-gd \  
php7-opcache \  
php7-mbstring \  
php7-session \  
php7-json \  
php7-pcntl \  
php7-mysqli \  
php7-pdo_mysql \  
php7-mcrypt \  
php7-iconv \  
php7-intl \  
php7-simplexml \  
php7-bcmath \  
php7-imagick \  
php7-tokenizer \  
php7-pdo \  
mariadb \  
mariadb-client  
  
COPY /rootfs /  
  
# Small fixes  
RUN ln -s /etc/php7 /etc/php && \  
# ln -s /usr/bin/php7 /usr/bin/php && \  
ln -s /usr/sbin/php-fpm7 /usr/bin/php-fpm && \  
ln -s /usr/lib/php7 /usr/lib/php && \  
rm -fr /var/cache/apk/*  
  
# Enable default sessions  
RUN mkdir -p /var/lib/php7/sessions  
RUN chown nginx:nginx /var/lib/php7/sessions  
  
ADD https://github.com/drush-
ops/drush/releases/download/$DRUSH_VERSION/drush.phar /bin/drush  
RUN chmod +x /bin/drush  
  
RUN mkdir /var/www/app && \  
mkdir /var/www/app/vendor && \  
mkdir /var/www/app/docroot && \  
chown nginx:nginx /var/www/app -Rf  
  
RUN ls -al /  
  
VOLUME ["/data"]  
  
ENTRYPOINT ["/init"]

