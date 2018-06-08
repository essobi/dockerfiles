FROM alpine:latest  
  
MAINTAINER orleika <admin@orleika.io>  
  
ARG NGINX_VERSION=1.13.8  
ARG LIBRESSL_VERSION=2.6.4  
ARG GPG_LIBRESSL="A1EB 079B 8D3E B92B 4EBD 3139 663A F51B D5E4 D8D5"  
ARG GPG_NGINX="B0F4 2533 73F8 F6F5 10D4 2178 520A 9993 A1C0 52F8"  
  
RUN addgroup -S nginx \  
&& adduser -D -S -h /var/cache/nginx -s /sbin/nologin -G nginx nginx \  
&& BUILD_CORES=$(getconf _NPROCESSORS_ONLN) \  
&& apk add \--update \--no-cache \--virtual .build_dep \  
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
binutils \  
gnupg \  
&& apk add \--update \--no-cache \  
pcre \  
zlib \  
libgcc \  
libstdc++ \  
openssl \  
bind-tools \  
&& cd /tmp \  
&& git clone https://github.com/bagder/libbrotli \--depth=1 && cd libbrotli \  
&& ./autogen.sh && ./configure && make -j ${BUILD_CORES} && make install \  
&& cd /tmp \  
&& git clone https://github.com/google/ngx_brotli \--recursive \  
&& git clone https://github.com/openresty/headers-more-nginx-module \--depth=1
\  
&& LIBRESSL_TARBALL="libressl-${LIBRESSL_VERSION}.tar.gz" \  
&& wget -q http://ftp.openbsd.org/pub/OpenBSD/LibreSSL/${LIBRESSL_TARBALL} \  
&& echo "Verifying ${LIBRESSL_TARBALL}..." \  
&& wget -q http://ftp.openbsd.org/pub/OpenBSD/LibreSSL/${LIBRESSL_TARBALL}.asc
\  
&& gpg \--keyserver ha.pool.sks-keyservers.net \--recv-keys "$GPG_LIBRESSL" \  
&& gpg \--batch \--verify ${LIBRESSL_TARBALL}.asc ${LIBRESSL_TARBALL} \  
&& tar xzf ${LIBRESSL_TARBALL} \  
&& NGINX_TARBALL="nginx-${NGINX_VERSION}.tar.gz" \  
&& wget -q https://nginx.org/download/${NGINX_TARBALL} \  
&& echo "Verifying ${NGINX_TARBALL}..." \  
&& wget -q https://nginx.org/download/${NGINX_TARBALL}.asc \  
&& gpg \--keyserver ha.pool.sks-keyservers.net \--recv-keys "$GPG_NGINX" \  
&& gpg \--batch \--verify ${NGINX_TARBALL}.asc ${NGINX_TARBALL} \  
&& tar xzf ${NGINX_TARBALL} && cd nginx-${NGINX_VERSION} \  
&& ./configure \  
\--prefix=/etc/nginx \  
\--sbin-path=/usr/sbin/nginx \  
\--conf-path=/etc/nginx/nginx.conf \  
\--http-log-path=/var/log/nginx/access.log \  
\--error-log-path=/var/log/nginx/error.log \  
\--pid-path=/var/run/nginx.pid \  
\--lock-path=/var/run/nginx.lock \  
\--user=nginx \  
\--group=nginx \  
\--with-cc-opt='\--pipe -O3 -fPIE -fstack-protector-all -Wstack-protector
\--param ssp-buffer-size=4 -Wformat -Werror=format-security -Wno-deprecated-
declarations' \  
\--with-ld-opt='-Wl,-Bsymbolic-functions -Wl,-z,relro,-z,now' \  
\--with-openssl=/tmp/libressl-${LIBRESSL_VERSION} \  
\--with-http_ssl_module \  
\--with-http_v2_module \  
\--with-http_gzip_static_module \  
\--with-http_stub_status_module \  
\--with-file-aio \  
\--with-threads \  
\--with-pcre-jit \  
\--add-module=/tmp/headers-more-nginx-module \  
\--add-module=/tmp/ngx_brotli \  
&& make -j ${BUILD_CORES} && make install && make clean \  
&& rm -rf /etc/nginx/html/ \  
&& mkdir /etc/nginx/conf.d/ \  
&& mkdir -p /usr/share/nginx/html/ \  
&& install -m644 html/index.html /usr/share/nginx/html/ \  
&& install -m644 html/50x.html /usr/share/nginx/html/ \  
&& strip -s /usr/sbin/nginx \  
&& apk del .build_dep \  
&& rm -rf /tmp/* /root/.gnupg  
  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY default.conf /etc/nginx/sites-enabled/default.conf  
  
EXPOSE 80 443  
  
CMD ["nginx", "-g", "daemon off;"]  

