FROM alpine:3.6  
  
LABEL maintainer "shawnoy@outlook.com"  
  
ARG NGINX_VERSION=1.12.2  
ARG WORKDIR=/tmp  
  
# Download Nginx  
RUN cd $WORKDIR && \  
wget http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz && \  
tar zxf nginx-$NGINX_VERSION.tar.gz  
  
# Add www-data user and group  
RUN addgroup -g 82 -S www-data && \  
adduser -u 82 -D -S -G www-data www-data  
  
RUN apk --no-cache \  
add \  
pcre-dev \  
emacs-nox \  
libressl-dev && \  
apk --no-cache --virtual build-tool \  
add \  
g++ \  
autoconf \  
automake \  
make \  
zlib-dev  
  
RUN cd $WORKDIR/nginx-$NGINX_VERSION && \  
./configure \  
--user=www-data \  
--group=www-data \  
--prefix=/usr/local/nginx-$NGINX_VERSION \  
--sbin-path=/usr/local/sbin/nginx \  
--conf-path=/etc/nginx/nginx.conf \  
--error-log-path=/var/log/nginx/error.log \  
--http-log-path=/var/log/nginx/access.log \  
--pid-path=/var/run/nginx.pid \  
--lock-path=/var/run/nginx.lock \  
--with-http_ssl_module \  
--with-http_realip_module \  
--with-http_addition_module \  
--with-http_sub_module \  
--with-http_dav_module \  
--with-http_gunzip_module \  
--with-http_gzip_static_module \  
--with-http_stub_status_module \  
--with-http_auth_request_module \  
--with-threads \  
--with-stream \  
--with-stream_ssl_module \  
--with-http_v2_module && \  
make -j "$(getconf _NPROCESSORS_ONLN)" && \  
make install && \  
mkdir /etc/nginx/sites-enable && \  
mkdir /etc/nginx/sites-available && \  
apk del build-tool && \  
rm -rf $WORKDIR/*  
  
COPY nginx.conf /etc/nginx/nginx.conf  
  
CMD nginx  

