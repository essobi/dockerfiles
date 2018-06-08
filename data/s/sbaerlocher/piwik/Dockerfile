FROM piwik:fpm  
  
MAINTAINER s.baerlocher@sbaerlocher.ch  
  
# install phpredis extension  
ENV PHPREDIS_VERSION 3.1.4  
ADD https://github.com/phpredis/phpredis/archive/$PHPREDIS_VERSION.tar.gz
/tmp/redis.tar.gz  
RUN tar xzf /tmp/redis.tar.gz -C /tmp \  
&& mkdir -p /usr/src/php/ext \  
&& mv /tmp/phpredis-$PHPREDIS_VERSION /usr/src/php/ext/redis \  
&& echo 'redis' >> /usr/src/php-available-exts \  
&& docker-php-ext-install redis \  
&& rm -rf /usr/src/php/ext/redis  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["php-fpm"]  

