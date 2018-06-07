FROM unblibraries/nginx-php:alpine-php7  
MAINTAINER UNB Libraries Systems <libsystems_at_unb.ca>  
  
LABEL ca.unb.lib.generator="symfony"  
LABEL vcs-ref="alpine-nginx-php7-3.3"  
LABEL vcs-url="https://github.com/unb-libraries/drupal-symfony"  
  
ENV SYMFONY_ROOT_DIR ${APP_ROOT}/html  
ENV APP_CACHE_DIR ${SYMFONY_ROOT_DIR}/cache  
ENV APP_LOG_DIR ${SYMFONY_ROOT_DIR}/log  
ENV APP_WEBROOT ${SYMFONY_ROOT_DIR}/web  
  
COPY ./build /build  
COPY ./package-conf /package-conf  
COPY ./scripts/container /scripts  
# Add base symfony, required PHP packages.  
RUN apk update && apk \--update add rsync rsyslog postfix php7-ldap
php7-mbstring php7-ctype php7-tokenizer php7-simplexml php7-dom php7-session
php7-session php7-intl php7-pdo && \  
rm -f /var/cache/apk/* && \  
curl -LsS https://symfony.com/installer -o /usr/local/bin/symfony && \  
chmod a+x /usr/local/bin/symfony && \  
rm -rf html && \  
symfony new html && \  
# Package conf files.  
mkdir -p /etc/rsyslog.d && \  
mv /package-conf/nginx/app.conf /etc/nginx/conf.d/app.conf && \  
mv /package-conf/php/app-php.ini /etc/php7/conf.d/zz_app.ini && \  
mv /package-conf/php/app-php-fpm.conf /etc/php7/php-fpm.d/zz_app.conf && \  
rm -rf /package-conf  
# Build application defined by build dir.  
WORKDIR /app/html  
RUN rsync -a \--no-perms \--no-owner \--no-group \--delete
/build/composer.json ${SYMFONY_ROOT_DIR}/ && \  
composer install \--no-ansi \--prefer-dist && \  
rm -rf /root/.composer/cache && \  
rsync -a \--no-perms \--no-owner \--no-group \--delete /build/src/
${SYMFONY_ROOT_DIR}/src/ && \  
rsync -a \--no-perms \--no-owner \--no-group \--delete /build/app/
${SYMFONY_ROOT_DIR}/app/ && \  
rm -rf /build  

