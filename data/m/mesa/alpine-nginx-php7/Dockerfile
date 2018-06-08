FROM alpine:edge  
  
MAINTAINER Daniel Langemann <daniel.langemann@gmx.de>  
  
RUN apk add --no-cache \  
nginx \  
php7-bcmath \  
php7-ctype \  
php7-curl \  
php7-dom \  
php7-fpm \  
php7-gd \  
php7-iconv \  
php7-intl \  
php7-json \  
php7-mbstring \  
php7-mcrypt \  
php7-opcache \  
php7-openssl \  
php7-pdo \  
php7-pdo_sqlite \  
php7-pdo_mysql \  
php7-phar \  
php7-phar \  
php7-posix \  
php7-session \  
php7-simplexml \  
php7-soap \  
php7-tokenizer \  
php7-xml \  
php7-xmlreader \  
php7-xsl \  
php7-zip \  
php7-zlib \  
supervisor \  
curl  
  
# Add composer  
RUN curl https://getcomposer.org/composer.phar > /usr/local/bin/composer &&
chmod +x /usr/local/bin/composer  
  
# Copy configuration  
COPY etc/ /etc  
  
RUN chmod +x /etc/docker-entrypoint.sh  
  
# Copy project files to nginx webroot  
COPY var/www /var/www  
  
VOLUME /var/www  
EXPOSE 80  
ENTRYPOINT ["/etc/docker-entrypoint.sh"]  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]  

