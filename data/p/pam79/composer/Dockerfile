FROM pam79/laravel-php-fpm  
  
MAINTAINER Paapa Abdullah Morgan <paapaabdullahm@gmail.com>  
  
RUN apt-get update && apt-get install -y curl git openssh-server openssl bash  
  
RUN echo "memory_limit=-1" > "$PHP_INI_DIR/conf.d/memory-limit.ini" \  
&& echo "date.timezone=${PHP_TIMEZONE:-UTC}" >
"$PHP_INI_DIR/conf.d/date_timezone.ini"  
  
ENV PATH /root/.composer/vendor/bin:$PATH  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_VERSION 1.4.1  
RUN curl -s -f -L -o /tmp/installer.php
https://raw.githubusercontent.com/composer/getcomposer.org/da290238de6d63faace0343efbdd5aa9354332c5/web/installer
\  
&& php -r " \  
\$signature =
'669656bab3166a7aff8a7506b8cb2d1c292f042046c5a994c43155c0be6190fa0355160742ab2e1c88d40d5be660b410';
\  
\$hash = hash('SHA384', file_get_contents('/tmp/installer.php')); \  
if (!hash_equals(\$signature, \$hash)) { \  
unlink('/tmp/installer.php'); \  
echo 'Integrity check failed, installer is either corrupt or worse.' .
PHP_EOL; \  
exit(1); \  
}" \  
&& php /tmp/installer.php -- --install-dir=/usr/local/bin --filename=composer
--version=${COMPOSER_VERSION} \  
&& rm /tmp/installer.php  
  
VOLUME ["/app"]  
WORKDIR /app  
  
CMD ["-"]  
ENTRYPOINT ["composer", "--ansi"]

