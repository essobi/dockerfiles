FROM php:7.2-alpine  
MAINTAINER Will Hall "will@willhallonline.co.uk"  
LABEL io.whalebrew.name composer-brew  
LABEL io.whalebrew.config.working_dir '/app'  
  
# Install Dependencies  
RUN apk add --no-cache --virtual .persistent-deps \  
zip \  
unzip \  
git \  
patch  
  
# Remove memory limit for PHP-CLI and set timezone  
RUN echo "memory_limit = -1" > /usr/local/etc/php/conf.d/memory-limit.ini \  
&& echo "date.timezone = UTC" >> /usr/local/etc/php/conf.d/date-timezone.ini  
  
# Install Composer  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
\  
&& php composer-setup.php \  
&& php -r "unlink('composer-setup.php');" \  
&& mv composer.phar /usr/bin/composer \  
&& chmod +x /usr/bin/composer  
  
# Allow Composer to be run as root and set $PATH for Composer Executables  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV PATH "$PATH:/root/.composer/vendor/bin"  
WORKDIR /app  
  
CMD ["composer"]  

