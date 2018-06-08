FROM php:7.1.2-fpm-alpine  
MAINTAINER Su <sullivan.gaglione@foodmeup.io>  
  
ENV NGINX_VERSION 1.11.10  
ENV APP_DIR /var/www/html  
  
RUN GPG_KEYS=B0F4253373F8F6F510D42178520A9993A1C052F8 \  
&& CONFIG="\  
\--prefix=/etc/nginx \  
\--sbin-path=/usr/sbin/nginx \  
\--modules-path=/usr/lib/nginx/modules \  
\--conf-path=/etc/nginx/nginx.conf \  
\--error-log-path=/var/log/nginx/error.log \  
\--http-log-path=/var/log/nginx/access.log \  
\--pid-path=/var/run/nginx.pid \  
\--lock-path=/var/run/nginx.lock \  
\--http-client-body-temp-path=/var/cache/nginx/client_temp \  
\--http-proxy-temp-path=/var/cache/nginx/proxy_temp \  
\--http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp \  
\--http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp \  
\--http-scgi-temp-path=/var/cache/nginx/scgi_temp \  
\--user=nginx \  
\--group=nginx \  
\--with-http_flv_module \  
\--with-http_mp4_module \  
\--with-http_auth_request_module \  
\--with-threads \  
\--with-stream \  
\--with-compat \  
\--with-file-aio \  
\--with-http_v2_module \  
" \  
&& addgroup -S nginx \  
&& adduser -D -S -h /var/cache/nginx -s /bin/ash -G nginx nginx \  
&& apk add --no-cache --virtual .build-deps \  
gcc \  
libc-dev \  
make \  
openssl-dev \  
pcre-dev \  
zlib-dev \  
linux-headers \  
curl \  
gnupg \  
musl-dev \  
libffi-dev \  
gd-dev \  
&& curl -fSL http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz -o
nginx.tar.gz \  
&& curl -fSL http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz.asc -o
nginx.tar.gz.asc \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver pgp.mit.edu --recv-keys "$GPG_KEYS" || \  
gpg --keyserver keyserver.pgp.com --recv-keys "$GPG_KEYS" || \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_KEYS" \  
&& gpg --batch --verify nginx.tar.gz.asc nginx.tar.gz \  
&& rm -r "$GNUPGHOME" nginx.tar.gz.asc \  
&& mkdir -p /usr/src \  
&& tar -zxC /usr/src -f nginx.tar.gz \  
&& rm nginx.tar.gz \  
&& cd /usr/src/nginx-$NGINX_VERSION \  
&& ./configure $CONFIG --with-debug \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& mv objs/nginx objs/nginx-debug \  
&& ./configure $CONFIG \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& make install \  
&& rm -rf /etc/nginx/html/ \  
&& mkdir /etc/nginx/conf.d/ \  
&& mkdir -p /usr/share/nginx/html/ \  
&& install -m644 html/index.html /usr/share/nginx/html/ \  
&& install -m644 html/50x.html /usr/share/nginx/html/ \  
&& install -m755 objs/nginx-debug /usr/sbin/nginx-debug \  
&& ln -s ../../usr/lib/nginx/modules /etc/nginx/modules \  
&& strip /usr/sbin/nginx* \  
&& rm -rf /usr/src/nginx-$NGINX_VERSION \  
&& apk add --no-cache --virtual .nginx-rundeps \  
libintl \  
musl \  
pcre \  
zlib \  
# forward request and error logs to docker log collector  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
RUN echo @testing http://nl.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories \  
&& echo /etc/apk/respositories \  
&& apk update \  
&& apk add --no-cache --virtual .fmu-deps \  
bash \  
openssh-client \  
wget \  
supervisor \  
curl \  
libcurl \  
git \  
nodejs \  
mysql-client \  
openssl-dev \  
ca-certificates \  
dialog \  
libmcrypt-dev \  
libpng-dev \  
icu-dev \  
libpq \  
libxslt-dev \  
freetype-dev \  
acl \  
libjpeg-turbo-dev \  
&& docker-php-ext-configure gd \  
\--with-gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
&& pecl install xdebug \  
&& docker-php-ext-install iconv pdo pdo_mysql mysqli mbstring mcrypt gd exif
intl xsl json soap dom zip opcache bcmath \  
&& docker-php-source delete \  
&& mkdir -p /etc/nginx \  
&& mkdir -p /run/nginx \  
&& mkdir -p /var/log/supervisor \  
&& EXPECTED_COMPOSER_SIGNATURE=$(wget -q -O -
https://composer.github.io/installer.sig) \  
&& php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \  
&& php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'${EXPECTED_COMPOSER_SIGNATURE}') { echo 'Composer.phar Installer verified'; }
else { echo 'Composer.phar Installer corrupt'; unlink('composer-setup.php'); }
echo PHP_EOL;" \  
&& php composer-setup.php --install-dir=/usr/bin --filename=composer \  
&& php -r "unlink('composer-setup.php');" \  
&& apk del .build-deps \  
&& npm i -g yarn  
  
# Supervisor config  
COPY docker/supervisor/supervisord.conf /etc/supervisord.conf  
  
# Nginx config  
COPY docker/nginx/nginx.conf /etc/nginx/nginx.conf  
  
# Nginx site config  
RUN mkdir -p /etc/nginx/sites-available/ \  
&& mkdir -p /etc/nginx/sites-enabled/ \  
&& mkdir -p /var/www/html/  
COPY docker/nginx/default.conf /etc/nginx/sites-available/default.conf  
RUN ln -s /etc/nginx/sites-available/default.conf /etc/nginx/sites-
enabled/default.conf  
  
# PHP config  
COPY docker/php/php.ini /usr/local/etc/php/conf.d/docker-vars.ini  
COPY docker/php/php-fpm.conf /usr/local/etc/php-fpm.d/www.conf  
  
# Add source code  
WORKDIR /var/www/html  
COPY . .  
  
# setup access rights  
RUN chown -R nginx:nginx /var/www  
  
# Add script and setup access rights  
USER root  
RUN chmod 755 docker/start.sh  
  
# API  
EXPOSE 80  
  
CMD ["docker/start.sh"]  

