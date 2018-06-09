FROM php:7.2-fpm-alpine  
  
RUN apk add --update --no-cache \  
autoconf \  
curl \  
freetype-dev \  
g++ \  
icu-dev \  
libmemcached-dev \  
libjpeg-turbo-dev \  
libpng-dev \  
libssl1.0 \  
libpq \  
libxml2-dev \  
make \  
postgresql-dev \  
sqlite-dev \  
tzdata \  
zlib-dev \  
&& docker-php-source extract \  
&& pecl channel-update pecl.php.net \  
&& pecl install redis \  
&& docker-php-ext-enable redis \  
&& docker-php-source delete \  
&& docker-php-ext-install pdo_pgsql soap intl opcache pcntl \  
&& rm -rf /var/cache/apk/* \  
&& apk del g++ make  
  
COPY ./configs/*.ini /usr/local/etc/php/conf.d  
  
ARG PUID=1000  
ARG PGID=1000  
ENV PUID ${PUID}  
ENV PGID ${PGID}  
  
RUN addgroup -g ${PGID} docuser && \  
adduser -u ${PUID} -G docuser -D docuser  
  
USER root  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV TZ=Pacific/Auckland  
RUN cp /usr/share/zoneinfo/Pacific/Auckland /etc/localtime  
RUN echo $TZ > /etc/timezone  
RUN date  
  
WORKDIR /var/www  
  
CMD ["php-fpm"]  
  
EXPOSE 9000  

