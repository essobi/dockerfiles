FROM alpine:edge  
  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_HOME /tmp  
WORKDIR /app  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["composer"]  
  
ADD https://raw.githubusercontent.com/composer/docker/master/docker-
entrypoint.sh /docker-entrypoint.sh  
ADD
https://raw.githubusercontent.com/composer/getcomposer.org/master/web/installer
/tmp/installer.php  
  
RUN sed -i 's/bash/sh/g' /docker-entrypoint.sh && chmod +x /docker-
entrypoint.sh && \  
apk --no-cache add git tini php7 php7-zip php7-json php7-phar php7-mbstring
php7-openssl php7-curl && \  
echo "memory_limit=-1" > "/etc/php7/conf.d/memory-limit.ini" && \  
php /tmp/installer.php --no-ansi --install-dir=/usr/bin --filename=composer &&
\  
composer --ansi --version --no-interaction && \  
rm -rf /tmp/* /tmp/.htaccess  

