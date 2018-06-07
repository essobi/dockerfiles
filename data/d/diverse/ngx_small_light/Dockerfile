FROM alpine:3.5  
  
ENV NGINX_VERSION 1.13.5  
ENV SMALL_LIGHT_VERSION 0.9.2  
  
RUN set -ex \  
&& GPG_KEYS=B0F4253373F8F6F510D42178520A9993A1C052F8 \  
&&
SMALL_LIGHT_SHA256=4cf660651d11330a13aab29eb1722bf792d7c3c42e2919a36a1957c4ed0f1533
\  
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
libxslt-dev \  
gd-dev \  
geoip-dev \  
perl-dev \  
libwebp-dev \  
imagemagick-dev \  
imlib2-dev \  
jpeg-dev \  
libjpeg \  
&& curl -fSL http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz -o
nginx.tar.gz \  
&& curl -fSL http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz.asc -o
nginx.tar.gz.asc \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& found=''; \  
for server in \  
ha.pool.sks-keyservers.net \  
hkp://keyserver.ubuntu.com:80 \  
hkp://p80.pool.sks-keyservers.net:80 \  
pgp.mit.edu \  
; do \  
echo "Fetching GPG key $GPG_KEYS from $server"; \  
gpg --keyserver "$server" \--keyserver-options timeout=10 \--recv-keys
"$GPG_KEYS" && found=yes && break; \  
done; \  
test -z "$found" && echo >&2 "error: failed to fetch GPG key $GPG_KEYS" &&
exit 1; \  
gpg --batch --verify nginx.tar.gz.asc nginx.tar.gz \  
&& rm -r "$GNUPGHOME" nginx.tar.gz.asc \  
&& mkdir -p /usr/src/nginx \  
&& tar -zxf nginx.tar.gz -C /usr/src/nginx --strip-components=1 \  
&& rm nginx.tar.gz \  
&& cd /usr/src/nginx \  
&& curl -fSL
https://github.com/cubicdaiya/ngx_small_light/archive/v$SMALL_LIGHT_VERSION.tar.gz
-o ngx_small_light.tar.gz \  
&& echo "$SMALL_LIGHT_SHA256 *ngx_small_light.tar.gz" | sha256sum -c - \  
&& mkdir -p /usr/src/nginx/ngx_small_light \  
&& tar -zxf ngx_small_light.tar.gz -C /usr/src/nginx/ngx_small_light --strip-
components=1 \  
&& cd /usr/src/nginx/ngx_small_light \  
&& ./setup --with-imlib2 \  
&& cd /usr/src/nginx \  
&& ./configure \  
\--prefix=/etc/ngx_small_light \  
\--sbin-path=/usr/sbin/ngx_small_light \  
\--modules-path=/usr/lib/ngx_small_light/modules \  
\--conf-path=/etc/ngx_small_light/ngx_small_light.conf \  
\--error-log-path=/var/log/ngx_small_light/error.log \  
\--http-log-path=/var/log/ngx_small_light/access.log \  
\--pid-path=/var/run/ngx_small_light.pid \  
\--lock-path=/var/run/ngx_small_light.lock \  
\--http-client-body-temp-path=/var/cache/nginx/client_temp \  
\--http-proxy-temp-path=/var/cache/nginx/proxy_temp \  
\--http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp \  
\--http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp \  
\--http-scgi-temp-path=/var/cache/nginx/scgi_temp \  
\--user=nginx \  
\--group=nginx \  
\--with-http_ssl_module \  
\--with-http_stub_status_module \  
\--with-http_secure_link_module \  
\--with-http_gzip_static_module \  
\--with-http_realip_module \  
\--with-threads \  
\--add-module=ngx_small_light \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& make install \  
&& rm -rf /etc/ngx_small_light/html/ \  
&& mkdir /etc/ngx_small_light/conf.d/ \  
&& mkdir -p /usr/share/ngx_small_light/html/ \  
&& install -m644 html/index.html /usr/share/ngx_small_light/html/ \  
&& install -m644 html/50x.html /usr/share/ngx_small_light/html/ \  
&& strip /usr/sbin/ngx* \  
&& rm -rf /usr/src/nginx \  
&& apk add --no-cache --virtual .gettext gettext \  
&& mv /usr/bin/envsubst /tmp/ \  
&& runDeps="$( \  
scanelf --needed --nobanner /usr/sbin/ngx_small_light
/usr/lib/ngx_small_light/modules/*.so /tmp/envsubst \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --no-cache --virtual .run-deps $runDeps \  
&& apk del .build-deps \  
&& apk del .gettext \  
&& mv /tmp/envsubst /usr/local/bin/ \  
&& cd / \  
# forward request and error logs to docker log collector  
&& ln -sf /dev/stdout /var/log/ngx_small_light/access.log \  
&& ln -sf /dev/stderr /var/log/ngx_small_light/error.log  
  
COPY ngx_small_light.conf /etc/ngx_small_light/ngx_small_light.conf  
COPY small_light.vh.default.conf /etc/ngx_small_light/conf.d/default.conf  
  
EXPOSE 80  
  
STOPSIGNAL SIGTERM  
  
CMD ["ngx_small_light", "-g", "daemon off;"]  

