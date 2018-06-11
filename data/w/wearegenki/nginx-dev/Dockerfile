# Nginx web server and reverse proxy for general purpose use  
  
FROM
alpine:3.7@sha256:7df6db5aa61ae9480f52f0b3a06a140ab98d427f86d8d5de0bedab9b8df6b1c0  
  
RUN set -xe \  
&& NGINX_VERSION=1.11.10 \  
&& GPG_KEYS=B0F4253373F8F6F510D42178520A9993A1C052F8 \  
&& CONFIG="\  
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
\--user=www \  
\--group=www \  
\--with-http_ssl_module \  
\--with-http_realip_module \  
\--with-pcre \  
\--with-pcre-jit \  
\--with-threads \  
\--with-file-aio \  
\--with-http_v2_module \  
\--without-http_uwsgi_module \  
\--without-http_scgi_module \  
\--without-http_memcached_module \  
\--without-http_empty_gif_module \  
\--without-http_upstream_hash_module \  
\--without-http_upstream_ip_hash_module \  
\--without-http_upstream_least_conn_module \  
" \  
&& addgroup -g 1333 -S www \  
&& adduser -D -u 1333 -S -h /var/cache/nginx -s /sbin/nologin -G www www \  
&& apk add --no-cache --virtual .build-deps \  
curl \  
gcc \  
gnupg \  
libc-dev \  
linux-headers \  
make \  
libressl-dev \  
pcre-dev \  
zlib-dev \  
&& curl -fSL http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz -o
nginx.tar.gz \  
&& curl -fSL http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz.asc -o
nginx.tar.gz.asc \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_KEYS" \  
&& gpg --batch --verify nginx.tar.gz.asc nginx.tar.gz \  
&& rm -r "$GNUPGHOME" nginx.tar.gz.asc \  
&& mkdir -p /usr/src \  
&& tar -zxC /usr/src -f nginx.tar.gz \  
&& rm nginx.tar.gz \  
&& cd /usr/src/nginx-$NGINX_VERSION \  
&& export CFLAGS="-fstack-protector-strong -fpic -fpie -O3 -m64" \  
LDFLAGS="-Wl,-O1 -Wl,--hash-style=both -pie" \  
&& ./configure $CONFIG --with-debug \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& mv objs/nginx objs/nginx-debug \  
&& ./configure $CONFIG \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& make install \  
&& rm -rf /etc/nginx/html/ \  
&& mkdir /etc/nginx/conf.d/ \  
&& mkdir -p /usr/share/nginx/html/ \  
&& install -m644 html/index.html /usr/share/nginx/html/ \  
&& install -m644 html/50x.html /usr/share/nginx/html/ \  
&& install -m755 objs/nginx-debug /usr/sbin/nginx-debug \  
&& ln -s ../../usr/lib/nginx/modules /etc/nginx/modules \  
&& strip /usr/sbin/nginx* \  
#&& strip /usr/lib/nginx/modules/*.so \  
&& rm -rf /usr/src/nginx-$NGINX_VERSION \  
\  
# Bring in gettext so we can get `envsubst`, then throw  
# the rest away. To do this, we need to install `gettext`  
# then move `envsubst` out of the way so `gettext` can  
# be deleted completely, then move `envsubst` back.  
&& apk add --no-cache --virtual .gettext gettext \  
&& mv /usr/bin/envsubst /tmp/ \  
\  
&& runDeps="$( \  
scanelf --needed --nobanner /usr/sbin/nginx /usr/lib/nginx/modules/*.so
/tmp/envsubst \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --no-cache --virtual .nginx-rundeps $runDeps \  
&& apk del .build-deps \  
&& apk del .gettext \  
&& mv /tmp/envsubst /usr/local/bin/ \  
\  
# Forward request and error logs to docker log collector  
# && ln -sf /dev/stdout /var/log/nginx/access.log \  
# && ln -sf /dev/stderr /var/log/nginx/error.log \  
&& ln -sf /proc/self/fd/2 /var/log/nginx/access.log \  
&& ln -sf /proc/self/fd/2 /var/log/nginx/error.log \  
\  
# Unset SUID on all files  
&& for i in $(find / -perm /6000 -type f); do chmod a-s $i; done  
  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY conf/ /etc/nginx/conf/  
COPY conf.d/default.conf /etc/nginx/conf.d/default.conf  
  
EXPOSE 80 443  
  
CMD ["nginx", "-g", "daemon off;"]  

