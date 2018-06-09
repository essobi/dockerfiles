FROM composer:1 AS composer  
  
FROM php:7.1-alpine  
  
# Inspired by official "composer" docker image  
RUN apk --no-cache add curl git subversion openssh openssl mercurial tini bash
zlib-dev libpng-dev $PHPIZE_DEPS  
  
RUN echo "memory_limit=-1" > "$PHP_INI_DIR/conf.d/memory-limit.ini" \  
&& echo "date.timezone=${PHP_TIMEZONE:-UTC}" >
"$PHP_INI_DIR/conf.d/date_timezone.ini"  
  
# Install some php modules so we can use this image to run functional tests  
RUN docker-php-ext-install zip mysqli gd \  
&& pecl install xdebug \  
&& echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name
xdebug.so)" > "$PHP_INI_DIR/conf.d/xdebug.ini"  
  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_HOME /tmp  
WORKDIR /app  
  
# Inspired by "t3easy/surf:gulp" docker image  
RUN apk --no-cache add rsync nodejs  
  
# install yarn  
RUN curl -o- -L https://yarnpkg.com/install.sh | bash  
ENV PATH "/root/.yarn/bin:/root/.config/yarn/global/node_modules/.bin:$PATH"  
# install gulp-cli as global module  
RUN yarn global add gulp-cli \  
&& touch ~/.dummy \  
&& yarn cache clean \  
&& rm -f ~/.dummy  
  
# copy composer from official composer image  
COPY \--from=composer /usr/bin/composer /usr/bin/composer  
ENV PATH "/tmp/vendor/bin:$PATH"  
# Install typo3/surf  
RUN composer global require typo3/surf:^2@dev \  
&& composer clear-cache  
  
CMD ["/bin/ash"]

