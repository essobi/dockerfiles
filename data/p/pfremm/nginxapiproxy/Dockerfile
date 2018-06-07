# Dockerfile - alpine  
# https://github.com/openresty/docker-openresty  
  
#FROM alpine:edge  
FROM janeczku/alpine-kubernetes  
MAINTAINER Evan Wies <evan@neomantra.net>  
  
# Docker Build Arguments  
ARG RESTY_VERSION="1.9.15.1"  
ARG RESTY_OPENSSL_VERSION="1.0.2h"  
ARG RESTY_PCRE_VERSION="8.39"  
ARG RESTY_J="1"  
ARG RESTY_CONFIG_OPTIONS="\  
\--user=nginx \  
\--group=nginx \  
\--pid-path=/var/run/nginx.pid \  
\--lock-path=/var/run/nginx.lock \  
\--error-log-path=/var/log/nginx/error.log \  
\--http-log-path=/var/log/nginx/access.log \  
\--with-file-aio \  
\--with-http_addition_module \  
\--with-http_auth_request_module \  
\--with-http_dav_module \  
\--with-http_flv_module \  
\--with-http_geoip_module=dynamic \  
\--with-http_gunzip_module \  
\--with-http_gzip_static_module \  
\--with-http_image_filter_module=dynamic \  
\--with-http_mp4_module \  
\--with-http_random_index_module \  
\--with-http_realip_module \  
\--with-http_secure_link_module \  
\--with-http_slice_module \  
\--with-http_ssl_module \  
\--with-http_stub_status_module \  
\--with-http_sub_module \  
\--with-http_v2_module \  
\--with-http_xslt_module=dynamic \  
\--with-ipv6 \  
\--with-mail \  
\--with-mail_ssl_module \  
\--with-md5-asm \  
\--with-pcre-jit \  
\--with-sha1-asm \  
\--with-stream \  
\--with-stream_ssl_module \  
\--with-threads \  
\--without-http_fastcgi_module \  
\--without-http_uwsgi_module \  
\--without-http_scgi_module \  
"  
  
# These are not intended to be user-specified  
ARG _RESTY_CONFIG_DEPS="--with-openssl=/tmp/openssl-${RESTY_OPENSSL_VERSION}
--with-pcre=/tmp/pcre-${RESTY_PCRE_VERSION}"  
  
  
# 1) Install apk dependencies  
# 2) Download and untar OpenSSL, PCRE, and OpenResty  
# 3) Build OpenResty  
# 4) Cleanup  
  
RUN \  
apk add --no-cache --virtual .build-deps \  
build-base \  
curl \  
gd-dev \  
geoip-dev \  
libxslt-dev \  
linux-headers \  
make \  
perl-dev \  
readline-dev \  
zlib-dev \  
&& apk add --no-cache \  
gd \  
geoip \  
libgcc \  
libxslt \  
zlib \  
unzip \  
ca-certificates \  
bash \  
&& update-ca-certificates \  
&& cd /tmp \  
&& curl -fSL
https://www.openssl.org/source/openssl-${RESTY_OPENSSL_VERSION}.tar.gz -o
openssl-${RESTY_OPENSSL_VERSION}.tar.gz --insecure \  
&& tar xzf openssl-${RESTY_OPENSSL_VERSION}.tar.gz \  
&& curl -fSL
https://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-${RESTY_PCRE_VERSION}.tar.gz
-o pcre-${RESTY_PCRE_VERSION}.tar.gz --insecure \  
&& tar xzf pcre-${RESTY_PCRE_VERSION}.tar.gz \  
&& curl -fSL https://openresty.org/download/openresty-${RESTY_VERSION}.tar.gz
-o openresty-${RESTY_VERSION}.tar.gz --insecure\  
&& tar xzf openresty-${RESTY_VERSION}.tar.gz \  
&& cd /tmp/openresty-${RESTY_VERSION} \  
&& ./configure -j${RESTY_J} ${_RESTY_CONFIG_DEPS} ${RESTY_CONFIG_OPTIONS} \  
&& make -j${RESTY_J} \  
&& make -j${RESTY_J} install \  
&& cd /tmp \  
&& rm -rf \  
openssl-${RESTY_OPENSSL_VERSION} \  
openssl-${RESTY_OPENSSL_VERSION}.tar.gz \  
openresty-${RESTY_VERSION}.tar.gz openresty-${RESTY_VERSION} \  
pcre-${RESTY_PCRE_VERSION}.tar.gz pcre-${RESTY_PCRE_VERSION} \  
&& apk del .build-deps \  
&& addgroup -S nginx \  
&& adduser -S -G nginx nginx \  
&& mkdir -p /etc/nginx/sites-enabled \  
&& ln -s /usr/local/openresty/nginx/sbin/nginx /usr/local/bin/nginx \  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log \  
&& mkdir -p /tmp/nginx/  
  
  
COPY key.pem /usr/local/openresty/nginx/config/key.pem  
COPY cert.pem /usr/local/openresty/nginx/config/cert.pem  
COPY ca.pem /usr/local/openresty/nginx/config/ca.pem  
COPY nginx.conf /usr/local/openresty/nginx/conf/nginx.conf  
COPY apis.conf /usr/local/openresty/nginx/conf/sites-enabled/apis.conf  
COPY stub.conf /usr/local/openresty/nginx/conf/sites-enabled/stub.conf  
COPY test.lua /usr/local/openresty/nginx/conf/lua/test.lua  
CMD ["nginx"]

