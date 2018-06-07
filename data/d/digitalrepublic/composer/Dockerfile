FROM alpine:3.6  
COPY scripts /scripts  
  
RUN /scripts/install-packages.sh \  
&& rm -rf /scripts  
  
# Adapted from  
#
https://github.com/composer/docker/blob/0303cc2362774266be5845e9f2487312fda8b7f5/1.4/Dockerfile  
RUN apk --no-cache add curl git subversion openssh openssl mercurial tini bash  
  
RUN echo "memory_limit=-1" > "/etc/php7/conf.d/memory-limit.ini" \  
&& echo "date.timezone=${PHP_TIMEZONE:-UTC}" >
"/etc/php7/conf.d/date_timezone.ini"  
  
ENV PATH "/composer/vendor/bin:$PATH"  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_HOME /composer  
ENV COMPOSER_VERSION 1.5.0  
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
&& php /tmp/installer.php --no-ansi --install-dir=/usr/bin --filename=composer
--version=${COMPOSER_VERSION} \  
&& rm /tmp/installer.php \  
&& chmod -R 777 /composer \  
&& composer --ansi --version --no-interaction  
  
COPY composer/docker-entrypoint /usr/local/bin/  
  
# Prestissimo speeds up composer install/update massively  
RUN composer global require hirak/prestissimo  
  
ARG oauth_token  
  
RUN composer config --global github-oauth.github.com $oauth_token  
  
WORKDIR /app  
  
ENTRYPOINT ["docker-entrypoint"]  
  
CMD ["composer"]

