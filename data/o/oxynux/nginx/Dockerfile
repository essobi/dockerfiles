FROM alpine:3.7  
LABEL maintainer "Arnaud Astruc <oxynux@gmail.com>"  
  
ENV NGINX_VERSION 1.13.9  
ENV LIBRESSL_VERSION 2.6.4  
ENV DYNAMIC_TLS_RECORDS_VERSION "1.13.0+"  
ENV HEADERS_MORE_MODULE_VERSION "0.33"  
  
ENV NGINX_FINGERPRINT "B0F4253373F8F6F510D42178520A9993A1C052F8"  
ENV LIBRESSL_FINGERPRINT "A1EB079B8D3EB92B4EBD3139663AF51BD5E4D8D5"  
  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN addgroup -S nginx && adduser -S -G nginx nginx  
  
# grab su-exec for easy step-down from root  
RUN apk add --no-cache 'su-exec>=0.2'  
  
# for docker log collector  
RUN mkfifo -m 600 /tmp/logpipe \  
&& cat <> /tmp/logpipe 1>&2 &  
  
# TCP Fast Open (-DTCP_FASTOPEN=23) https://www.keycdn.com/support/tcp-fast-
open/  
ARG NGINX_CC_FLAGS="-O2 -DTCP_FASTOPEN=23"  
  
ARG NGINX_CONFIG=" \  
\--prefix=/etc/nginx \  
\--sbin-path=/usr/sbin/nginx \  
\--conf-path=/etc/nginx/nginx.conf \  
\--error-log-path=/tmp/logpipe \  
\--http-log-path=/tmp/logpipe \  
\--pid-path=/var/run/nginx.pid \  
\--lock-path=/var/run/nginx.lock \  
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
\--with-http_xslt_module \  
\--with-http_image_filter_module \  
\--with-http_geoip_module \  
\--with-threads \  
\--with-stream \  
\--with-stream_ssl_module \  
\--with-stream_ssl_preread_module \  
\--with-stream_realip_module \  
\--with-stream_geoip_module \  
\--with-http_slice_module \  
\--with-mail \  
\--with-mail_ssl_module \  
\--with-compat \  
\--with-file-aio \  
\--with-http_v2_module \  
\--with-pcre-jit \  
\--with-openssl=/usr/src/libressl-$LIBRESSL_VERSION \  
\--add-module=/usr/src/headers-more-nginx-module-$HEADERS_MORE_MODULE_VERSION"  
  
RUN apk add --no-cache --virtual .build-deps \  
gcc \  
musl-dev \  
make \  
openssl-dev \  
pcre-dev \  
zlib-dev \  
linux-headers \  
curl \  
gnupg \  
libxslt-dev \  
gd-dev \  
geoip-dev \  
git \  
autoconf \  
automake \  
libtool \  
file \  
patch \  
&& curl -fSL http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz -o
nginx.tar.gz \  
&& curl -fSL http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz.asc -o
nginx.tar.gz.asc \  
&& found=''; \  
( \  
gpg --no-tty --keyserver pgp.mit.edu --recv-keys $NGINX_FINGERPRINT || \  
gpg --no-tty --keyserver keyserver.pgp.com --recv-keys $NGINX_FINGERPRINT || \  
gpg --no-tty --keyserver ha.pool.sks-keyservers.net --recv-keys
$NGINX_FINGERPRINT \  
) \  
&& found=yes && break; \  
test -z "$found" && echo >&2 "error: failed to fetch GPG key
$NGINX_FINGERPRINT" && exit 1; \  
gpg --verify nginx.tar.gz.asc \  
&& curl -fSL
http://ftp.openbsd.org/pub/OpenBSD/LibreSSL/libressl-$LIBRESSL_VERSION.tar.gz
-o libressl.tar.gz \  
&& curl -fSL
http://ftp.openbsd.org/pub/OpenBSD/LibreSSL/libressl-$LIBRESSL_VERSION.tar.gz.asc
-o libressl.tar.gz.asc \  
&& found=''; \  
( \  
gpg --no-tty --keyserver pgp.mit.edu --recv-keys $LIBRESSL_FINGERPRINT || \  
gpg --no-tty --keyserver keyserver.pgp.com --recv-keys $LIBRESSL_FINGERPRINT
|| \  
gpg --no-tty --keyserver ha.pool.sks-keyservers.net --recv-keys
$LIBRESSL_FINGERPRINT \  
) \  
&& found=yes && break; \  
test -z "$found" && echo >&2 "error: failed to fetch GPG key
$LIBRESSL_FINGERPRINT" && exit 1; \  
gpg --verify libressl.tar.gz.asc \  
&& mkdir -p /usr/src \  
&& curl -fSL https://github.com/openresty/headers-more-nginx-
module/archive/v$HEADERS_MORE_MODULE_VERSION.tar.gz -o ngx_headers_more.tar.gz
\  
&& tar -zxC /usr/src -f ngx_headers_more.tar.gz \  
&& ls -laR /usr/src \  
&& rm ngx_headers_more.tar.gz \  
&& tar -zxC /usr/src -f nginx.tar.gz \  
&& rm nginx.tar.gz \  
&& tar -zxC /usr/src -f libressl.tar.gz \  
&& rm libressl.tar.gz \  
&& cd /usr/src/nginx-$NGINX_VERSION \  
&& curl -fSL https://raw.githubusercontent.com/cujanovic/nginx-dynamic-tls-
records-
patch/master/nginx__dynamic_tls_records_$DYNAMIC_TLS_RECORDS_VERSION.patch -o
nginx__dynamic_tls_records.patch \  
&& patch -p1 < nginx__dynamic_tls_records.patch \  
&& rm nginx__dynamic_tls_records.patch \  
&& ./configure ${NGINX_CONFIG} \  
\--with-cc-opt="${NGINX_CC_FLAGS}" \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& make install \  
&& rm -rf /etc/nginx/html/ \  
&& mkdir /etc/nginx/conf.d/ \  
&& mkdir -p /usr/share/nginx/html/ \  
&& install -m644 html/index.html /usr/share/nginx/html/ \  
&& install -m644 html/50x.html /usr/share/nginx/html/ \  
&& strip /usr/sbin/nginx* \  
&& apk add --no-cache --virtual .gettext gettext \  
&& mv /usr/bin/envsubst /tmp/ \  
&& runDeps="$( \  
scanelf --needed --nobanner /usr/sbin/nginx /tmp/envsubst \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
) tzdata ca-certificates" \  
&& apk add --no-cache --virtual .nginx-rundeps $runDeps \  
&& apk del .build-deps \  
&& apk del .gettext \  
&& mv /tmp/envsubst /usr/local/bin/ \  
&& chown -R nginx:nginx /etc/nginx \  
&& rm -rf \  
/root/.gnupg \  
/usr/src \  
/libressl.tar.gz.asc \  
/nginx.tar.gz.asc  
  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY default.conf /etc/nginx/conf.d/default.conf  
  
WORKDIR /etc/nginx  
  
COPY docker-entrypoint.sh /usr/local/bin/  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
LABEL description="nginx mainline built from source with ngx_headers_more,
ngx_brotli and TCP Fast Open" \  
openssl="LibreSSL $LIBRESSL_VERSION" \  
nginx="nginx $NGINX_VERSION"  
  
EXPOSE 8080 4430  
CMD ["nginx", "-g", "daemon off;"]  

