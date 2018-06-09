# Based on:  
# https://github.com/nginxinc/docker-
nginx/blob/master/mainline/alpine/Dockerfile  
# https://github.com/mbland/knowledge-sharing-
toolkit/blob/master/nginx/Dockerfile  
  
FROM alpine:3.7  
  
MAINTAINER Mike Bland "mbland@acm.org"  
  
ENV NGINX_VERSION=1.13.10 \  
ZLIB_VERSION=1.2.11 \  
PCRE_VERSION=8.42 \  
OPENSSL_VERSION=1.0.2o  
  
COPY server-header.patch /tmp/  
  
RUN addgroup -S nginx \  
&& adduser -D -S -h /var/cache/nginx -s /sbin/nologin -G nginx nginx \  
&& apk add --no-cache --virtual .build-deps \  
curl \  
file \  
g++ \  
libc-dev \  
linux-headers \  
make \  
perl \  
&& mkdir -p /usr/local/src && cd /usr/local/src \  
&& sh -c "curl https://nginx.org/download/nginx-$NGINX_VERSION.tar.gz | gzip
-dc | tar xf -" \  
&& sh -c "curl https://zlib.net/zlib-$ZLIB_VERSION.tar.gz | gzip -dc | tar xf
-" \  
&& sh -c "curl https://ftp.pcre.org/pub/pcre/pcre-$PCRE_VERSION.tar.gz | gzip
-dc | tar xf -" \  
&& sh -c "curl https://www.openssl.org/source/openssl-$OPENSSL_VERSION.tar.gz
| gzip -dc | tar xf -" \  
&& cd /usr/local/src/nginx-$NGINX_VERSION \  
&& patch -p1 < /tmp/server-header.patch \  
&& rm /tmp/server-header.patch \  
&& ./configure --prefix=/usr/local/nginx \  
\--conf-path=/usr/local/nginx/config/nginx.conf \  
\--error-log-path=/var/log/nginx/error.log \  
\--http-log-path=/var/log/nginx/access.log \  
\--user=nginx \  
\--group=nginx \  
\--with-http_addition_module \  
\--with-http_auth_request_module \  
\--with-http_gzip_static_module \  
\--with-http_secure_link_module \  
\--with-http_ssl_module \  
\--with-http_stub_status_module \  
\--with-http_sub_module \  
\--with-http_v2_module \  
\--with-ipv6 \  
\--with-md5-asm \  
\--with-openssl=../openssl-$OPENSSL_VERSION \  
\--with-pcre=../pcre-$PCRE_VERSION \  
\--with-sha1-asm \  
\--with-zlib=../zlib-$ZLIB_VERSION \  
\--without-http_browser_module \  
\--without-http_geo_module \  
\--without-http_memcached_module \  
\--without-http_scgi_module \  
\--without-http_ssi_module \  
\--without-http_userid_module \  
\--without-http_uwsgi_module \  
\--with-cc=/usr/bin/gcc \  
\--with-cc-opt='-I/usr/local/include' \  
\--with-ld-opt='-L/usr/local/lib -Wl,-rpath=/usr/local/lib' \  
&& make install \  
&& strip /usr/local/nginx/sbin/nginx \  
&& apk del .build-deps \  
&& rm -rf /usr/local/src \  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
EXPOSE 80 443  
CMD [ "/usr/local/nginx/sbin/nginx", "-g", "daemon off;" ]  

