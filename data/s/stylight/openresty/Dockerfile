FROM alpine:3.5  
  
MAINTAINER Stylight <open-source@stylight.com>  
  
ENV OPENRESTY_VERSION 1.11.2.1  
  
ENV GPG_KEYS A0E98066  
ENV CONFIG "\  
--prefix=/etc/nginx \  
--sbin-path=/usr/sbin/nginx \  
--conf-path=/etc/nginx/nginx.conf \  
--error-log-path=/var/log/nginx/error.log \  
--http-log-path=/var/log/nginx/access.log \  
--pid-path=/var/run/nginx.pid \  
--lock-path=/var/run/nginx.lock \  
--http-client-body-temp-path=/var/cache/nginx/client_temp \  
--http-proxy-temp-path=/var/cache/nginx/proxy_temp \  
--http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp \  
--http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp \  
--http-scgi-temp-path=/var/cache/nginx/scgi_temp \  
--user=nginx \  
--group=nginx \  
--with-http_ssl_module \  
--with-http_realip_module \  
--with-http_addition_module \  
--with-http_sub_module \  
--with-http_dav_module \  
--with-http_flv_module \  
--with-http_mp4_module \  
--with-http_gunzip_module \  
--with-http_gzip_static_module \  
--with-http_random_index_module \  
--with-http_secure_link_module \  
--with-http_stub_status_module \  
--with-http_auth_request_module \  
--with-http_realip_module \  
--with-mail \  
--with-mail_ssl_module \  
--with-file-aio \  
--with-luajit \  
--with-ipv6 \  
"  
  
# Open always adds another subversion to the end of \  
# original NginX version number. \  
RUN \  
export NGINX_VERSION=${OPENRESTY_VERSION%.*} \  
&& addgroup -S nginx \  
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
perl \  
&& curl -fSL
https://openresty.org/download/openresty-$OPENRESTY_VERSION.tar.gz -o
nginx.tar.gz \  
&& curl -fSL
https://openresty.org/download/openresty-$OPENRESTY_VERSION.tar.gz.asc -o
nginx.tar.gz.asc \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_KEYS" \  
&& gpg --batch --verify nginx.tar.gz.asc nginx.tar.gz \  
&& rm -r "$GNUPGHOME" nginx.tar.gz.asc \  
&& mkdir -p /usr/src \  
&& tar -zxC /usr/src -f nginx.tar.gz \  
&& rm nginx.tar.gz \  
&& cd /usr/src/openresty-$OPENRESTY_VERSION \  
&& ./configure $CONFIG --with-debug \  
&& make \  
&& install -m755 build/nginx-$NGINX_VERSION/objs/nginx /usr/sbin/nginx-debug \  
&& ./configure $CONFIG \  
&& make \  
&& make install \  
&& mkdir /etc/nginx/conf.d/ \  
&& mkdir -p /usr/share/nginx/html/ \  
&& strip /usr/sbin/nginx* \  
&& runDeps="$( \  
scanelf --needed --nobanner /usr/sbin/nginx \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --virtual .nginx-rundeps $runDeps \  
&& apk del .build-deps \  
&& rm -rf /usr/src/openresty-$OPENRESTY_VERSION \  
&& apk add --no-cache gettext ruby libgcc \  
\  
# forward request and error logs to docker log collector  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
# COPY nginx.conf /etc/nginx/nginx.conf  
# COPY nginx.vh.default.conf /etc/nginx/conf.d/default.conf  
  
EXPOSE 80 443  
  
CMD ["nginx", "-g", "daemon off;"]  

