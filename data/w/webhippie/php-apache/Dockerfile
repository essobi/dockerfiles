FROM webhippie/apache:latest  
MAINTAINER Thomas Boerger <thomas@webhippie.de>  
  
EXPOSE 8080  
WORKDIR /srv/www  
ENTRYPOINT ["/usr/bin/entrypoint"]  
CMD ["/bin/s6-svscan", "/etc/s6"]  
  
RUN apk update && \  
apk upgrade && \  
apk add \  
php7 \  
php7-apache2 \  
php7-ctype \  
php7-curl \  
php7-dom \  
php7-gd \  
php7-iconv \  
php7-intl \  
php7-json \  
php7-memcached \  
php7-mysqli \  
php7-mysqlnd \  
php7-openssl \  
php7-opcache \  
php7-pdo \  
php7-pdo_mysql \  
php7-pdo_pgsql \  
php7-pdo_sqlite \  
php7-pear \  
php7-pgsql \  
php7-phar \  
php7-sqlite3 \  
php7-xml \  
php7-zip \  
php7-zlib \  
php7-mbstring \  
php7-simplexml \  
php7-tokenizer \  
php7-xmlwriter \  
php7-fileinfo \  
git && \  
ln -sf \  
/usr/bin/php7 \  
/usr/bin/php && \  
rm -rf \  
/var/cache/apk/* \  
/etc/php7/*  
  
ADD rootfs /  
  
RUN curl -sS https://getcomposer.org/installer \  
| php -- --install-dir=/usr/bin --filename=composer  
  
ARG VERSION  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL org.label-schema.version=$VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE  
LABEL org.label-schema.vcs-ref=$VCS_REF  
LABEL org.label-schema.vcs-url="https://github.com/dockhippie/php.git"  
LABEL org.label-schema.name="PHP Apache"  
LABEL org.label-schema.vendor="Thomas Boerger"  
LABEL org.label-schema.schema-version="1.0"  

