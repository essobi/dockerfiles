FROM php:7.2-fpm-alpine  
  
ENV PS1 '\u@\h:\w\$ '  
RUN apk --no-cache add postgresql-dev icu-dev \  
&& docker-php-ext-install pdo pdo_pgsql intl \  
&& apk del postgresql-dev \  
&& apk --no-cache add --upgrade postgresql icu-libs \  
&& apk add --no-cache --virtual .phpize-deps $PHPIZE_DEPS \  
&& pecl install xdebug redis apcu \  
&& apk del .phpize-deps \  
&& docker-php-ext-enable apcu intl opcache pdo pdo_pgsql redis xdebug  
  
RUN version=$(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") \  
&& curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s
https://blackfire.io/api/v1/releases/probe/php/linux/amd64/$version \  
&& tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp \  
&& mv /tmp/blackfire-*.so $(php -r "echo
ini_get('extension_dir');")/blackfire.so \  
&& printf
"extension=blackfire.so\nblackfire.agent_socket=tcp://blackfire:8707\n" >
/usr/local/etc/php/conf.d/blackfire.ini \  
&& rm -rf /tmp/* \  
;  
#  
COPY entrypoint.sh /usr/local/bin/entrypoint  
RUN chmod +x /usr/local/bin/entrypoint  
#  
WORKDIR /var/www/html  
#  
EXPOSE 9000  
ENTRYPOINT ["entrypoint"]  
  
CMD ["php-fpm"]  

