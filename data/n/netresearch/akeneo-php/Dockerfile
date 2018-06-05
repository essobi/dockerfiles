FROM php:5  
RUN echo "memory_limit=-1" > "$PHP_INI_DIR/conf.d/memory-limit.ini" \  
&& echo "date.timezone=${PHP_TIMEZONE:-UTC}" >
"$PHP_INI_DIR/conf.d/date_timezone.ini"  
  
COPY ./akeneo-php-* /usr/local/bin/  
  
RUN chmod +x /usr/local/bin/akeneo-php-*  
  
ARG WITH_GIT=true  
RUN akeneo-php-install-deps && rm /usr/local/bin/akeneo-php-install-deps  
  
ENV COMPOSER_ALLOW_SUPERUSER 1  
RUN akeneo-php-install-composer && rm /usr/local/bin/akeneo-php-install-
composer  
  
RUN mkdir -p /var/www/html  
WORKDIR /var/www/html  
  
CMD ["php", "-a"]  

