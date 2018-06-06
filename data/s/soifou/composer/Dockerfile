FROM alpine:3.7  
MAINTAINER François Fleur <fleur.fr@gmail.com>  
  
ENV PATH "/composer/vendor/bin:$PATH"  
ENV PHP_VERSION 7.1  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_HOME /composer  
ENV COMPOSER_VERSION 1.6.2  
ARG BUILD_DATE  
ARG VCS_REF  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.version="php-$PHP_VERSION" \  
org.label-schema.docker.dockerfile="/Dockerfile" \  
org.label-schema.vcs-url="https://github.com/soifou/composer"  
  
ADD https://php.codecasts.rocks/php-alpine.rsa.pub /etc/apk/keys/php-
alpine.rsa.pub  
  
RUN echo "@php https://php.codecasts.rocks/v3.7/php-$PHP_VERSION" >>
/etc/apk/repositories && \  
apk add --update --no-cache \  
ca-certificates \  
bash \  
curl \  
less \  
tini \  
git \  
openssh \  
openssl \  
mariadb-client \  
php7@php \  
php7-ctype@php \  
php7-curl@php \  
php7-dom@php \  
php7-gd@php \  
php7-iconv@php \  
php7-json@php \  
php7-mbstring@php \  
php7-mcrypt@php \  
php7-mongodb@php \  
php7-mysqli@php \  
php7-openssl@php \  
php7-pdo@php \  
php7-pdo_mysql@php \  
php7-phar@php \  
php7-posix@php \  
php7-session@php \  
php7-xml@php \  
php7-zip@php \  
php7-zlib@php  
  
RUN ln -sf /usr/bin/php7 /usr/bin/php  
  
ADD ./composer.sh /composer.sh  
RUN chmod u+x /composer.sh && \  
sh /composer.sh $COMPOSER_VERSION  
  
RUN rm -rf /tmp/src && \  
rm -f /composer.sh \  
rm -rf /var/cache/*  
  
COPY php.ini /usr/local/etc/php/conf.d/50-setting.ini  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod +x /docker-entrypoint.sh  
  
WORKDIR /app  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["composer"]

