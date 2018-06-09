FROM php:7.2-alpine  
  
RUN apk add \--no-cache git tini && \  
git clone https://github.com/nikic/php-ast.git /tmp/php-ast && \  
apk del git && \  
docker-php-ext-install pcntl && \  
apk add \--no-cache \--virtual .phpize-deps $PHPIZE_DEPS && \  
cd /tmp/php-ast && phpize && ./configure && make install && \  
apk del .phpize-deps && \  
echo extension=ast.so > /usr/local/etc/php/conf.d/ast.ini && \  
curl -sS https://getcomposer.org/installer | php -- \--install-
dir=/usr/local/bin/ \--filename=composer && \  
composer create-project \--no-dev \--prefer-dist etsy/phan /opt/phan 0.12.3 &&
\  
rm -r /tmp/php-ast /usr/local/bin/composer  
  
ENV PATH $PATH:/opt/phan/  
  
ENTRYPOINT ["/sbin/tini", "--"]  
  
CMD ["phan"]  

