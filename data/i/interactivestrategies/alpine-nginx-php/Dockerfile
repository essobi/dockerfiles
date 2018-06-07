FROM alpine:edge  
MAINTAINER Taylor Solomon <taylor.solomon@me.com>  
  
ENV S6_VERSION v1.17.2.0  
# Add testing repo to get latest apk packages  
RUN echo "ipv6" >> /etc/modules  
  
## Add basic stuff  
RUN apk add --update --no-cache curl bash  
  
# Add NGINX-Webserver with NAXSI  
RUN apk --update --repository=http://dl-4.alpinelinux.org/alpine/edge/testing
add \  
nginx \  
shadow \  
git \  
unzip \  
php7 \  
php7-ctype \  
php7-curl \  
php7-dom \  
php7-ftp \  
php7-gd \  
php7-iconv \  
php7-json \  
php7-fpm \  
php7-mbstring \  
php7-mysqli \  
php7-opcache \  
php7-openssl \  
php7-pdo \  
php7-pdo_mysql \  
php7-phar \  
php7-session \  
php7-sockets \  
php7-xml \  
php7-xmlrpc \  
php7-xmlreader \  
php7-xsl \  
php7-zip \  
php7-zlib \  
mysql-client  
  
# Move config files to the right places.  
COPY /config /  
  
# Small fixes  
RUN rm -fr /var/cache/apk/*  
RUN usermod -u 1000 nginx  
  
# Symlink php services to useful names  
RUN ln -s /etc/php7 /etc/php && \  
ln -s /usr/bin/php7 /usr/bin/php && \  
ln -s /usr/sbin/php-fpm7 /usr/bin/php-fpm && \  
ln -s /usr/lib/php7 /usr/lib/php  
  
RUN mkdir -p /var/www/.opcache && chown -R nginx /var/www/.opcache  
  
# Install composer global bin  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
# Install Drush  
RUN php -r "readfile('http://files.drush.org/drush.phar');" > drush && \  
chmod +x drush && \  
mv drush /usr/local/bin  
  
# Add S6-overlay to use S6 process manager  
# https://github.com/just-containers/s6-overlay/#the-docker-way  
ADD https://github.com/just-
containers/s6-overlay/releases/download/${S6_VERSION}/s6-overlay-amd64.tar.gz
/tmp/  
RUN gunzip -c /tmp/s6-overlay-amd64.tar.gz | tar -xf - -C /  
  
# Expose Ports  
EXPOSE 443  
EXPOSE 80  
VOLUME ["/var/www", "/var/log"]  
  
ENTRYPOINT ["/init"]  

