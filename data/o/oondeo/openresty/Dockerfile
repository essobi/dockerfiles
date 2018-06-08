# Dockerfile - alpine  
# https://github.com/openresty/docker-openresty  
FROM oondeo/alpine:3.7  
ENV SUMMARY="Nginx, resty and naxsi image with standar modules" \  
DESCRIPTION="The image use scripts and configurations compatible \  
with redhat openshift."  
LABEL summary="$SUMMARY" \  
description="$DESCRIPTION" \  
io.k8s.description="$DESCRIPTION" \  
io.k8s.display-name="Nginx" \  
io.openshift.s2i.scripts-url=image:///usr/libexec/s2i \  
io.s2i.scripts-url=image:///usr/libexec/s2i \  
com.redhat.component="nginx" \  
name="oondeo/openresty" \  
version="7" \  
release="1" \  
maintainer="OONDEO <info@oondeo.es>"  
  
# Docker Build Arguments  
ARG NAXSI_VERSION="0.55.3"  
ARG NGX_CACHE_PURGE_VERSION="2.4.2"  
ARG RESTY_VERSION="1.13.6.1"  
ARG RESTY_OPENSSL_VERSION="1.0.2k"  
ARG RESTY_PCRE_VERSION="8.41"  
ARG RESTY_J="1"  
ARG RESTY_CONFIG_OPTIONS="\  
\--with-file-aio \  
\--with-http_addition_module \  
\--with-http_auth_request_module \  
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
\--with-md5-asm \  
\--with-pcre-jit \  
\--with-sha1-asm \  
\--with-stream \  
\--with-stream_ssl_module \  
\--with-threads \  
\--without-http_scgi_module \  
\--add-dynamic-module=/tmp/ngx_cache_purge-${NGX_CACHE_PURGE_VERSION} \  
"  
# --with-mail \  
# --with-mail_ssl_module \  
# --with-http_flv_module \  
# --with-http_dav_module=dynamic \  
# --without-http_fastcgi_module  
ARG RESTY_CONFIG_OPTIONS_MORE=" --add-
module=/tmp/naxsi-$NAXSI_VERSION/naxsi_src"  
# These are not intended to be user-specified  
#ARG _RESTY_CONFIG_DEPS="--with-openssl=/tmp/openssl-${RESTY_OPENSSL_VERSION}
--with-pcre=/tmp/pcre-${RESTY_PCRE_VERSION}"  
ARG _RESTY_CONFIG_DEPS=""  
# 1) Install apk dependencies  
# 2) Download and untar OpenSSL, PCRE, and OpenResty  
# 3) Build OpenResty  
# 4) Cleanup  
COPY patch_naxsi.sh /root/  
RUN apk add --no-cache --virtual .build-deps \  
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
pcre-dev \  
libressl-dev \  
&& apk add --no-cache \  
gd \  
geoip \  
libgcc \  
libxslt \  
zlib \  
&& cd /tmp \  
&& curl -fSL https://github.com/nginx-
modules/ngx_cache_purge/archive/$NGX_CACHE_PURGE_VERSION.tar.gz -o
ngx_cache_purge-${NGX_CACHE_PURGE_VERSION}.tar.gz \  
&& tar xzf ngx_cache_purge-${NGX_CACHE_PURGE_VERSION}.tar.gz \  
&& curl -fSL https://github.com/nbs-system/naxsi/archive/$NAXSI_VERSION.tar.gz
-o naxsi-$NAXSI_VERSION.tar.gz \  
&& tar xzf naxsi-${NAXSI_VERSION}.tar.gz \  
&& curl -fSL
https://www.openssl.org/source/openssl-${RESTY_OPENSSL_VERSION}.tar.gz -o
openssl-${RESTY_OPENSSL_VERSION}.tar.gz \  
&& tar xzf openssl-${RESTY_OPENSSL_VERSION}.tar.gz \  
&& curl -fSL https://ftp.pcre.org/pub/pcre/pcre-${RESTY_PCRE_VERSION}.tar.gz
-o pcre-${RESTY_PCRE_VERSION}.tar.gz \  
&& tar xzf pcre-${RESTY_PCRE_VERSION}.tar.gz \  
&& curl -fSL https://openresty.org/download/openresty-${RESTY_VERSION}.tar.gz
-o openresty-${RESTY_VERSION}.tar.gz \  
&& tar xzf openresty-${RESTY_VERSION}.tar.gz \  
&& cd /tmp/openresty-${RESTY_VERSION} \  
&& /root/patch_naxsi.sh "${RESTY_CONFIG_OPTIONS_MORE}" \  
&& grep configure configure \  
&& ./configure -j${RESTY_J} ${_RESTY_CONFIG_DEPS} ${RESTY_CONFIG_OPTIONS} \  
&& make -j${RESTY_J} \  
&& make -j${RESTY_J} install \  
&& cd /tmp \  
&& rm -rf \  
openssl-${RESTY_OPENSSL_VERSION} \  
openssl-${RESTY_OPENSSL_VERSION}.tar.gz \  
openresty-${RESTY_VERSION}.tar.gz openresty-${RESTY_VERSION} \  
pcre-${RESTY_PCRE_VERSION}.tar.gz pcre-${RESTY_PCRE_VERSION} \  
&& install-deps /usr/local/openresty \  
&& apk del .build-deps \  
&& ln -sf /dev/stdout /usr/local/openresty/nginx/logs/access.log \  
&& ln -sf /dev/stderr /usr/local/openresty/nginx/logs/error.log \  
&& rm -rf /tmp/* /etc/nginx \  
&& rm -rf /usr/local/openresty/nginx/log \  
&& mv /usr/local/openresty/nginx/conf /opt/app-root/etc/nginx \  
&& mkdir -p /opt/app-root/var/log/nginx \  
&& ln -sf /opt/app-root/etc/nginx /usr/local/openresty/nginx/conf \  
&& ln -sf /opt/app-root/var/log/nginx /usr/local/openresty/nginx/log \  
&& ln -sf /opt/app-root/var/log/nginx /var/log/nginx \  
&& ln -sf /opt/app-root/etc/nginx /etc/nginx  
  
# Add additional binaries into PATH for convenience  
ENV
PATH=$PATH:/usr/local/openresty/luajit/bin/:/usr/local/openresty/nginx/sbin/:/usr/local/openresty/bin/  
  
# Copy nginx configuration files  
COPY root/ /  
  
RUN docker-footer  
USER 1001  
EXPOSE 8080 8081  
CMD ["/usr/libexec/s2i/bin/run"]  
#https://github.com/masterzen/nginx-upload-progress-module

