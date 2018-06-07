FROM php:fpm-alpine  
  
ENV KNOWN_VERSION=0.9.9 \  
KNOWN_DATABASE=MySQL \  
KNOWN_DBHOST=db \  
KNOWN_DBNAME=known \  
KNOWN_DBUSER=known_user \  
KNOWN_DBPASS=known_pass \  
KNOWN_UPLOADPATH=/Uploads/ \  
KNOWN_SESSIONNAME=known  
  
# Get nginx and supervisord  
RUN apk add --update --no-cache \  
bzip2 \  
coreutils \  
curl \  
curl-dev \  
freetype-dev \  
gettext \  
icu-dev \  
jpeg-dev \  
libmcrypt-dev \  
libpng-dev \  
libxml2-dev \  
mysql-client \  
nginx \  
openssl-dev \  
postgresql-dev \  
supervisor \  
tar \  
unzip && \  
mkdir -p /run/nginx && \  
chown -R www-data:www-data /var/lib/nginx && \  
rm /etc/nginx/nginx.conf && \  
rm -f /etc/nginx/sites-enabled/* && \  
ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log && \  
ln -sf /dev/stderr /var/log/php-fpm.log  
  
RUN docker-php-ext-configure \  
gd --with-png-dir=/usr --with-jpeg-dir=/usr && \  
docker-php-ext-configure \  
pgsql --with-pgsql=/usr && \  
docker-php-ext-install -j$(nproc) \  
exif \  
gd \  
intl \  
mcrypt \  
mysqli \  
opcache \  
pdo \  
pdo_mysql \  
pdo_pgsql \  
pgsql \  
xmlrpc \  
zip  
  
COPY opcache-recommended.ini /usr/local/etc/php/conf.d/  
  
RUN apk add --update --no-cache --virtual .build-deps\  
autoconf \  
automake \  
make \  
gcc \  
g++ \  
libtool \  
pcre-dev && \  
pecl install \  
APCu \  
mongodb && \  
docker-php-ext-enable \  
apcu \  
mongodb && \  
apk del .build-deps  
  
# Download Known source  
WORKDIR /var/www/html  
RUN curl -o known.tar.gz -SL
"https://github.com/idno/Known/archive/v${KNOWN_VERSION}.tar.gz" && \  
tar -xpf known.tar.gz --strip 1 && \  
cp nginx.conf /etc/nginx/ && \  
rm known.tar.gz && \  
chown -R www-data:www-data .  
  
VOLUME /Uploads  
VOLUME /var/www/html/Themes  
VOLUME /var/www/html/IdnoPlugins  
  
EXPOSE 80 9000  
  
COPY config.ini.tpl /var/www/html/  
COPY supervisor.conf /etc/supervisor/conf.d/  
COPY docker-entrypoint.sh /usr/local/bin/  
  
ENTRYPOINT [ "docker-entrypoint.sh" ]  
  
CMD [ "supervisord", "-c", "/etc/supervisor/conf.d/supervisor.conf" ]  

