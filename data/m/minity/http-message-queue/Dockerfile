FROM alpine:3.5  
  
MAINTAINER Anton Tyutin "anton@tyutin.ru"  
  
ENV NGINX_VERSION 1.10.2  
ENV NCHAN_VERSION 1.1.0  
  
RUN addgroup -S nginx \  
&& adduser -D -S -h /var/cache/nginx -s /sbin/nologin -G nginx nginx \  
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
perl-dev \  
&& curl -qfsSL http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz -o
nginx.tar.gz \  
&& curl -qfsSL http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz.asc -o
nginx.tar.gz.asc \  
&& curl -qfsSL https://github.com/slact/nchan/archive/v$NCHAN_VERSION.tar.gz |
tar -zxC /tmp \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& export GPG_KEYS=B0F4253373F8F6F510D42178520A9993A1C052F8 \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_KEYS" \  
&& gpg --batch --verify nginx.tar.gz.asc nginx.tar.gz \  
&& rm -r "$GNUPGHOME" nginx.tar.gz.asc \  
&& mkdir -p /usr/src \  
&& tar -zxC /usr/src -f nginx.tar.gz \  
&& rm nginx.tar.gz \  
&& cd /usr/src/nginx-$NGINX_VERSION \  
&& ./configure \  
\--prefix=/ \  
\--sbin-path=/usr/sbin/nginx \  
\--modules-path=/usr/lib/nginx/modules \  
\--conf-path=/etc/nginx/nginx.conf \  
\--error-log-path=/var/log/nginx/error.log \  
\--http-log-path=/var/log/nginx/access.log \  
\--pid-path=/var/run/nginx.pid \  
\--lock-path=/var/run/nginx.lock \  
\--http-client-body-temp-path=/var/cache/nginx/client_temp \  
\--user=nginx \  
\--group=nginx \  
\--with-http_ssl_module \  
\--with-http_realip_module \  
\--with-threads \  
\--with-stream \  
\--with-stream_ssl_module \  
\--with-http_slice_module \  
\--without-http_proxy_module \  
\--without-http_fastcgi_module \  
\--without-http_scgi_module \  
\--without-http_uwsgi_module \  
\--without-http_autoindex_module \  
\--with-file-aio \  
\--with-ipv6 \  
\--add-module=/tmp/nchan-$NCHAN_VERSION \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& make install \  
&& rm -rf /etc/nginx/html/ \  
&& mkdir -p /usr/share/nginx/html/ \  
&& install -m644 html/index.html /usr/share/nginx/html/ \  
&& install -m644 html/50x.html /usr/share/nginx/html/ \  
&& strip /usr/sbin/nginx* \  
&& rm -rf /usr/src/nginx-$NGINX_VERSION \  
&& runDeps="$( \  
scanelf --needed --nobanner /usr/sbin/nginx \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --no-cache --virtual .nginx-rundeps $runDeps \  
&& apk del .build-deps \  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log \  
&& rm -rf /tmp/*  
  
COPY *.conf /etc/nginx/  
  
EXPOSE 80 443  
  
CMD ["nginx", "-g", "daemon off;"]  

