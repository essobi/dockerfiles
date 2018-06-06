FROM php:7.1-alpine  
MAINTAINER Bart Reunes <metalarend@gmail.com>  
  
# Install Composer globally - https://github.com/composer/composer  
ENV COMPOSER_HOME /composer  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV PATH /composer/vendor/bin:$PATH  
  
RUN curl https://getcomposer.org/installer -o /tmp/composer-setup.php \  
&& curl https://composer.github.io/installer.sig -o /tmp/composer-setup.sig \  
&& php -r "if (hash_file('SHA384', '/tmp/composer-setup.php') !==
trim(file_get_contents('/tmp/composer-setup.sig'))) { echo 'Installer
corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" \  
&& php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin
--filename=composer \  
&& php -r "unlink('/tmp/composer-setup.php');" \  
&& php -r "unlink('/tmp/composer-setup.sig');"  
  
# Install Tini - https://github.com/krallin/tini  
RUN apk add --no-cache tini  
  
# Install PHP CodeSniffer - https://github.com/squizlabs/PHP_CodeSniffer  
RUN echo "memory_limit=-1" > $PHP_INI_DIR/conf.d/memory-limit.ini  
RUN composer global require --dev squizlabs/php_codesniffer:2.*  
  
# Install PHPCompatibility - https://github.com/wimg/PHPCompatibility  
RUN echo "date.timezone=Europe/Brussels" > $PHP_INI_DIR/conf.d/timezone.ini  
RUN composer global require --dev wimg/php-compatibility:dev-
feature/fix-102-107-directory-layout \  
&& phpcs --config-set installed_paths /composer/vendor/wimg/php-compatibility  
  
# Package container  
VOLUME ["/app"]  
WORKDIR "/app"  
ENTRYPOINT ["/sbin/tini", "--", "phpcs"]  
CMD ["--help"]  

