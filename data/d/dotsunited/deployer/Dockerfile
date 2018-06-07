FROM php:7-alpine  
  
MAINTAINER Dots United GmbH <info@dotsunited.de>  
  
ENV PATH="~/.composer/vendor/bin:${PATH}"  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_HTACCESS_PROTECT 0  
ENV DEPLOYER_VERSION=6.0.5  
ENV DEPLOYER_RECIPES_VERSION=6.0.2  
RUN apk update --no-cache && \  
apk upgrade --no-cache && \  
apk add bash curl git openssh-client openssl rsync tini zlib-dev --no-cache  
  
RUN echo "memory_limit=-1" > "$PHP_INI_DIR/conf.d/memory-limit.ini"  
RUN echo "date.timezone=${PHP_TIMEZONE:-UTC}" >
"$PHP_INI_DIR/conf.d/date_timezone.ini"  
  
RUN docker-php-ext-install zip  
  
COPY \--from=composer:latest /usr/bin/composer /usr/bin/composer  
  
RUN mkdir -p ~/.composer /deployer  
  
COPY ssh_config /ssh_config  
RUN cat /ssh_config >> /etc/ssh/ssh_config  
RUN rm -f /ssh_config  
  
# Run self-update in case we have copied an outdated version earlier  
RUN composer self-update  
  
RUN composer global require --prefer-dist --no-interaction hirak/prestissimo  
RUN composer global require --prefer-dist --no-interaction
deployer/deployer:"$DEPLOYER_VERSION"  
RUN composer global require --prefer-dist --no-interaction
deployer/recipes:"$DEPLOYER_RECIPES_VERSION"  
  
RUN rm -rf ~/.composer/cache/*  
  
COPY docker-entrypoint /usr/local/bin/docker-entrypoint  
RUN chmod +x /usr/local/bin/docker-entrypoint  
  
WORKDIR /deployer  
  
ENTRYPOINT ["/sbin/tini", "--", "docker-entrypoint"]  
  
CMD ["dep", "--version"]  

