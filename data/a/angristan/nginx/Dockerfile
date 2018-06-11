FROM alpine:3.3  
MAINTAINER Angristan <contact@angristan.fr>  
  
ARG NGINX_VER=1.9.15  
ARG LIBRESSL_VER=2.3.3  
ARG SIGNATURE="That's a secret."  
  
RUN NB_CORES=$(getconf _NPROCESSORS_CONF) \  
&& BUILD_DEPS=" \  
build-base \  
linux-headers \  
ca-certificates \  
automake \  
autoconf \  
git \  
tar \  
libtool \  
pcre-dev \  
zlib-dev \  
binutils" \  
&& apk -U add \  
$BUILD_DEPS \  
pcre \  
zlib \  
&& cd /tmp/ \  
&& wget
http://ftp.openbsd.org/pub/OpenBSD/LibreSSL/libressl-${LIBRESSL_VER}.tar.gz \  
&& tar -zxf libressl-${LIBRESSL_VER}.tar.gz \  
&& cd libressl-${LIBRESSL_VER} \  
&& ./configure \  
LDFLAGS=-lrt \  
\--prefix=/tmp/libressl/.openssl/ \  
&& make install-strip -j $NB_CORES \  
&& mkdir /tmp/nginx \  
&& cd /tmp/nginx \  
&& wget http://nginx.org/download/nginx-${NGINX_VER}.tar.gz \  
&& tar -zxf nginx-${NGINX_VER}.tar.gz \  
&& cd nginx-${NGINX_VER} \  
&& sed -i -e "s/\"Server: nginx\" CRLF/\"Server: $SIGNATURE\" CRLF/g" \  
-e "s/\"Server: \" NGINX_VER CRLF/\"Server: $SIGNATURE\" NGINX_VER CRLF/g" \  
src/http/ngx_http_header_filter_module.c \  
&& ./configure \  
\--prefix=/etc/nginx \  
\--sbin-path=/usr/sbin/nginx \  
\--conf-path=/etc/nginx/conf/nginx.conf \  
\--error-log-path=/var/log/nginx/error.log \  
\--http-log-path=/var/log/nginx/access.log \  
\--http-client-body-temp-path=/etc/nginx/client_temp \  
\--http-proxy-temp-path=/etc/nginx/proxy_temp \  
\--http-fastcgi-temp-path=/etc/nginx/fastcgi_temp \  
\--user=www-data \  
\--group=www-data \  
\--without-http_ssi_module \  
\--without-http_scgi_module \  
\--without-http_uwsgi_module \  
\--without-http_geo_module \  
\--without-http_split_clients_module \  
\--without-http_memcached_module \  
\--without-http_empty_gif_module \  
\--without-http_browser_module \  
\--with-threads \  
\--with-file-aio \  
\--with-http_ssl_module \  
\--with-http_v2_module \  
\--with-ipv6 \  
\--with-http_mp4_module \  
\--with-http_auth_request_module \  
\--with-http_slice_module \  
\--with-openssl=/tmp/libressl-${LIBRESSL_VER} \  
&& make -j $NB_CORES \  
&& make install \  
&& make clean \  
&& rm -rf /tmp/ \  
&& strip -s /usr/sbin/nginx \  
&& apk del $BUILD_DEPS \  
&& rm -rf /tmp/* /var/cache/apk/* \  
&& adduser -D www-data \  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log \  
&& mkdir -p /tmp/client_temp && mkdir -p /tmp/proxy_temp && mkdir -p
/tmp/fastcgi_temp  
  
COPY nginx.conf /etc/nginx/conf/nginx.conf  
  
EXPOSE 80 443  
  
CMD ["nginx"]  

