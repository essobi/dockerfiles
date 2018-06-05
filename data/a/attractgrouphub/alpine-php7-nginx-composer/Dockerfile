FROM php:7.1.13-fpm-alpine  
  
MAINTAINER Amondar  
  
#nginx and common extensions for php  
RUN apk --update add gd gd-dev sqlite-dev libmcrypt-dev libxml2-dev \  
freetype libpng libjpeg-turbo freetype-dev libpng-dev libjpeg-turbo-dev && \  
rm -rf /var/cache/apk/* && \  
apk add --no-cache freetype libpng libjpeg-turbo freetype-dev libpng-dev
libjpeg-turbo-dev && \  
#php extencions  
docker-php-ext-configure gd \  
\--with-gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ && \  
NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) && \  
docker-php-ext-install -j${NPROC} pdo_mysql mcrypt xml pcntl exif gd zip
opcache && \  
apk del --no-cache freetype-dev libpng-dev libjpeg-turbo-dev && \  
#composer  
curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer  
  
RUN build_pkgs="build-base linux-headers openssl-dev pcre-dev wget zlib-dev" \  
&& runtime_pkgs="ca-certificates openssl pcre zlib" \  
&& apk --update add ${build_pkgs} ${runtime_pkgs} \  
&& cd /tmp \  
&& wget http://nginx.org/download/nginx-1.11.7.tar.gz \  
&& tar xzf nginx-1.11.7.tar.gz \  
&& cd /tmp/nginx-1.11.7 \  
&& ./configure \  
\--prefix=/etc/nginx \  
\--sbin-path=/usr/sbin/nginx \  
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
\--with-http_ssl_module \  
\--with-http_realip_module \  
\--with-http_addition_module \  
\--with-http_sub_module \  
\--with-http_dav_module \  
\--with-http_flv_module \  
\--with-http_mp4_module \  
\--with-http_gunzip_module \  
\--with-http_gzip_static_module \  
\--with-http_random_index_module \  
\--with-http_secure_link_module \  
\--with-http_stub_status_module \  
\--with-http_auth_request_module \  
\--with-threads \  
\--with-stream \  
\--with-stream_ssl_module \  
\--with-http_slice_module \  
\--with-mail \  
\--with-mail_ssl_module \  
\--with-file-aio \  
\--with-http_v2_module \  
\--with-http_image_filter_module \  
\--with-ipv6 \  
&& make \  
&& make install \  
&& sed -i -e 's/#access_log logs\/access.log main;/access_log \/dev\/stdout;/'
-e 's/#error_log logs\/error.log notice;/error_log stderr notice;/'
/etc/nginx/nginx.conf \  
&& adduser -D nginx \  
&& rm -rf /tmp/* \  
&& apk del ${build_pkgs} \  
&& rm -rf /var/cache/apk/*  
  

