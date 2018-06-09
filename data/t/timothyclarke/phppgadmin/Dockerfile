FROM php:7.2-fpm-alpine  
  
# Install dependencies  
# postgresql is needed for pg_dump, as soon as we can move to fpm-alpine37
then we can drop  
RUN apk add --no-cache --virtual .build-deps \  
bzip2-dev \  
freetype-dev \  
libjpeg-turbo-dev \  
libpng-dev \  
libwebp-dev \  
libxpm-dev \  
postgresql \  
postgresql-client \  
postgresql-dev \  
; \  
\  
docker-php-ext-configure gd --with-freetype-dir=/usr --with-jpeg-dir=/usr
--with-webp-dir=/usr --with-png-dir=/usr --with-xpm-dir=/usr; \  
docker-php-ext-install bz2 gd pgsql opcache zip; \  
\  
runDeps="$( \  
scanelf --needed --nobanner --format '%n#p' --recursive
/usr/local/lib/php/extensions \  
| tr ',' '\n' \  
| sort -u \  
| awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1
}' \  
)"; \  
apk add --virtual .phpmpgdmin-phpexts-rundeps $runDeps; \  
apk del .build-deps; \  
apk add --no-cache nginx supervisor  
  
  
# Copy configuration  
COPY etc /etc/  
  
# Copy main script  
COPY run.sh /run.sh  
RUN chmod u+rwx /run.sh  
  
# Calculate download URL  
ENV VERSION 5-1-0  
ENV URL https://github.com/phppgadmin/phppgadmin/archive/REL_${VERSION}.tar.gz  
LABEL version=$VERSION  
  
# Download tarball, verify it using gpg and extract  
RUN set -x \  
&& apk add --no-cache curl \  
&& curl --output phpPgAdmin.tar.gz --location $URL \  
&& apk del --no-cache curl \  
&& tar xzf phpPgAdmin.tar.gz \  
&& rm -f phpPgAdmin.tar.gz \  
&& mv phppgadmin-REL_${VERSION} /www \  
&& mv /etc/config.inc.php /www/conf \  
&& chown -R root:nobody /www \  
&& find /www -type d -exec chmod 750 {} \; \  
&& find /www -type f -exec chmod 640 {} \;  
  
# Add directory for sessions to allow session persistence  
RUN mkdir /sessions  
  
# We expose phpMyAdmin on port 80  
EXPOSE 80  
  
ENTRYPOINT [ "/run.sh" ]  
CMD ["phppgadmin"]  

