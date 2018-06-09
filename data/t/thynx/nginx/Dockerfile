FROM alpine:3.4  
  
MAINTAINER "Silas Rech" <silas@thynx.io>  
  
ENV NGX_VERSION=1.11.6 \  
NGX_VERSION_BROTLI=2.2.0 \  
NGX_VERSION_TRANSPARENCY=1.3.1 \  
NGX_VERSION_CORS=0.2.2 \  
NGX_GPG_KEY=B0F4253373F8F6F510D42178520A9993A1C052F8 \  
NGX_SHA_BROTLI=b19f4500bfb2f674f19cca4ad7a18ccdbbc6a61f160e329ead8073c3c118ed83
\  
NGX_SHA_TRANSPARENCY=c223b642fc541933b9cdb18b771a52ccf728fb309350898080970ab1fda18e6f
\  
NGX_SHA_CORS=a3c37b8f3ed5e125de9499cfaa663a8131298a9bf252b8473f58a1a6e446284b
\  
BUILD_DEPENDENCIES="\  
gcc \  
g++ \  
libc-dev \  
make \  
openssl-dev \  
pcre-dev \  
zlib-dev \  
linux-headers \  
curl \  
gnupg \  
sed \  
wget \  
patch \  
" \  
NGX_CONFIG="\  
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
\--with-http_ssl_module \  
\--with-http_realip_module \  
\--with-http_gunzip_module \  
\--with-http_gzip_static_module \  
\--with-http_secure_link_module \  
\--with-http_stub_status_module \  
\--with-threads \  
\--with-stream \  
\--with-stream_ssl_module \  
\--with-file-aio \  
\--with-http_v2_module \  
\--with-http_spdy_module \  
\--with-ipv6 \  
\--add-module=/usr/src/brotli \  
\--add-module=/usr/src/transparency \  
\--add-module=/usr/src/cors \  
\--without-http_ssi_module \  
\--without-http_uwsgi_module \  
\--without-http_scgi_module \  
\--without-http_empty_gif_module \  
\--without-http_autoindex_module \  
"  
  
COPY *.conf *.html /usr/src/bolt/  
COPY patches/ /usr/src/bolt/patches  
  
RUN \  
addgroup -g 82 -S nginx \  
&& adduser -u 82 -D -S -h /var/cache/nginx -s /sbin/nologin -G nginx nginx \  
&& apk -q add --no-cache --virtual .build-deps ${BUILD_DEPENDENCIES} \  
&& echo "Downloaded build dependencies" \  
&& curl -fSLs https://nginx.org/download/nginx-${NGX_VERSION}.tar.gz -o
nginx.tar.gz \  
&& curl -fSLs https://nginx.org/download/nginx-${NGX_VERSION}.tar.gz.asc -o
nginx.tar.gz.asc \  
&& echo "Downloaded NGINX v${NGX_VERSION}" \  
&& curl -fSLs https://github.com/thynx/ngx-
brotli/archive/${NGX_VERSION_BROTLI}.tar.gz -o brotli.tar.gz \  
&& echo "Downloaded NGINX Module 'Brotli Compression' v${NGX_VERSION_BROTLI}"
\  
&& curl -fSLs https://github.com/grahamedgecombe/nginx-
ct/archive/v${NGX_VERSION_TRANSPARENCY}.tar.gz -o transparency.tar.gz \  
&& echo "Downloaded NGINX Module 'Certificate Transparency'
v${NGX_VERSION_TRANSPARENCY}" \  
&& curl -fSLs
https://github.com/x-v8/ngx_http_cors_filter/archive/${NGX_VERSION_CORS}.tar.gz
-o cors.tar.gz \  
&& echo "Downloaded NGINX Module 'Cross Origin Resource Sharing'
v${NGX_VERSION_CORS}" \  
&& printf "\n" \  
&& echo "Verification of signature and fingerprint:" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg -q --keyserver ha.pool.sks-keyservers.net --recv-keys "${NGX_GPG_KEY}"
>> /dev/null 2>&1 \  
&& gpg -q --batch --verify nginx.tar.gz.asc nginx.tar.gz >> /dev/null 2>&1 \  
&& rm -r "${GNUPGHOME}" nginx.tar.gz.asc \  
&& printf "\n" \  
&& echo "nginx.tar.gz: OK" \  
&& echo "${NGX_SHA_BROTLI} *brotli.tar.gz" | sha256sum -c - \  
&& echo "${NGX_SHA_TRANSPARENCY} *transparency.tar.gz" | sha256sum -c - \  
&& echo "${NGX_SHA_CORS} *cors.tar.gz" | sha256sum -c - \  
&& printf "\n" \  
&& mkdir -p /usr/src \  
&& tar -zxC /usr/src -f nginx.tar.gz \  
&& tar -zxC /usr/src -f brotli.tar.gz \  
&& tar -zxC /usr/src -f transparency.tar.gz \  
&& tar -zxC /usr/src -f cors.tar.gz \  
&& mv /usr/src/nginx-${NGX_VERSION} /usr/src/nginx \  
&& mv /usr/src/ngx-brotli-${NGX_VERSION_BROTLI} /usr/src/brotli \  
&& mv /usr/src/nginx-ct-${NGX_VERSION_TRANSPARENCY} /usr/src/transparency \  
&& mv /usr/src/ngx_http_cors_filter-${NGX_VERSION_CORS} /usr/src/cors \  
&& rm nginx.tar.gz \  
&& rm brotli.tar.gz \  
&& rm transparency.tar.gz \  
&& rm cors.tar.gz \  
&& cd /usr/src/nginx \  
&& patch -p1 < /usr/src/bolt/patches/${NGX_VERSION}/dynamic-tls-records.patch
>> /dev/null 2>&1 \  
&& echo "Patched NGINX v${NGX_VERSION} to support Dynamic TLS Records" \  
&& patch -p1 < /usr/src/bolt/patches/${NGX_VERSION}/spdy.patch >> /dev/null
2>&1 \  
&& echo "Patched NGINX v${NGX_VERSION} to support SPDY" \  
&& sed -i -e 's/"Server: nginx"/"Server: Bolt ϟ"/g'
src/http/ngx_http_header_filter_module.c \  
&& sed -i -e 's/"nginx"/"Bolt ϟ"/g' src/http/v2/ngx_http_v2_filter_module.c \  
&& sed -i -e 's/"nginx\/"/"Bolt ϟ \/ "/g' src/core/nginx.h \  
&& sed -i -e "s/\"Server: \" NGINX_VER CRLF/\"Server: Bolt ϟ \/
${NGX_VERSION}\" CRLF/g" src/http/ngx_http_header_filter_module.c \  
&& ./configure ${NGX_CONFIG} >/dev/null \  
&& echo "Configured NGINX v${NGX_VERSION}" \  
&& make >/dev/null \  
&& echo "Compiled NGINX v${NGX_VERSION}" \  
&& make install >/dev/null \  
&& echo "Installed NGINX v${NGX_VERSION}" \  
&& rm -rf /etc/nginx/html/ \  
&& mkdir /etc/nginx/conf.d/ \  
&& mkdir -p /usr/share/nginx/html/ \  
&& cd / \  
&& sed -i -e "s/NGX_VERSION/${NGX_VERSION}/g" /usr/src/bolt/index.html \  
&& sed -i -e "s/NGX_VERSION/${NGX_VERSION}/g" /usr/src/bolt/error.html \  
&& install -m644 /usr/src/bolt/index.html /usr/share/nginx/html/ \  
&& install -m644 /usr/src/bolt/error.html /usr/share/nginx/html/ \  
&& install -m644 /usr/src/bolt/nginx.conf /etc/nginx/ \  
&& install -m644 /usr/src/bolt/host.conf /etc/nginx/conf.d/ \  
&& strip /usr/sbin/nginx* \  
&& export RUN_DEPENDENCIES="$( \  
scanelf --needed --nobanner /usr/sbin/nginx \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk -q add --virtual .nginx-rundeps ${RUN_DEPENDENCIES} \  
&& apk -q del .build-deps \  
&& rm -rf /usr/src/nginx-${NGX_VERSION} \  
&& rm -rf /usr/src/bolt \  
&& rm -rf /usr/src/brotli \  
&& rm -rf /usr/src/transparency \  
&& rm -rf /usr/src/cors \  
&& apk -q add --no-cache gettext \  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
EXPOSE 80/tcp 443/tcp  
  
CMD ["nginx", "-g", "daemon off;"]  

