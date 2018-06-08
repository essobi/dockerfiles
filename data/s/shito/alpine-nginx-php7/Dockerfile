FROM shito/alpine-nginx:edge  
MAINTAINER Sebastian Knoth <sk@bytepark.de>  
  
# Add PHP 7  
RUN apk upgrade -U && \  
apk --update --repository=http://dl-4.alpinelinux.org/alpine/edge/testing add
\  
openssl \  
php7 \  
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
php7-opcache \  
php7-mbstring \  
php7-session \  
php7-pcntl  
  
COPY /rootfs /  
  
# Small fixes  
RUN ln -s /etc/php7 /etc/php && \  
ln -s /usr/bin/php7 /usr/bin/php && \  
ln -s /usr/sbin/php-fpm7 /usr/bin/php-fpm && \  
ln -s /usr/lib/php7 /usr/lib/php && \  
rm -fr /var/cache/apk/*  
  
# Install composer global bin  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
# Enable default sessions  
RUN mkdir -p /var/lib/php7/sessions  
RUN chown nginx:nginx /var/lib/php7/sessions  
# ADD SOURCE  
RUN mkdir -p /usr/share/nginx/html  
RUN chown -Rf nginx:nginx /usr/share/nginx/html  
  
ENTRYPOINT ["/init"]  

