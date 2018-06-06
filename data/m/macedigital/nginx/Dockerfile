FROM alpine:edge  
  
RUN NGINX_GPG_KEYS=B0F4253373F8F6F510D42178520A9993A1C052F8 \  
NGINX_VERSION=1.11.10 \  
RTMP_VERSION=1.1.10 \  
HEADERS_MORE_VERSION=0.32 \  
NGINX_UID=99 \  
NGINX_USER=nginx \  
&& NGINX_CONF="\  
\--prefix=/etc/nginx \  
\--sbin-path=/usr/sbin/nginx \  
\--modules-path=/usr/lib/nginx/modules \  
\--conf-path=/etc/nginx/nginx.conf \  
\--error-log-path=/var/log/nginx/error.log \  
\--http-log-path=/var/log/nginx/access.log \  
\--http-client-body-temp-path=/var/cache/nginx/client_temp \  
\--http-proxy-temp-path=/var/cache/nginx/proxy_temp \  
\--http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp \  
\--http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp \  
\--http-scgi-temp-path=/var/cache/nginx/scgi_temp \  
\--pid-path=/run/nginx.pid \  
\--lock-path=/run/nginx.lock \  
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
\--with-http_xslt_module=dynamic \  
\--with-http_image_filter_module=dynamic \  
\--with-http_geoip_module=dynamic \  
\--with-threads \  
\--with-stream=dynamic \  
\--with-stream_geoip_module=dynamic \  
\--with-stream_realip_module \  
\--with-stream_ssl_module \  
\--with-stream_ssl_preread_module \  
\--with-http_slice_module \  
\--with-mail=dynamic \  
\--with-mail_ssl_module \  
\--with-file-aio \  
\--with-http_v2_module \  
\--with-ipv6 \  
\--with-pcre \  
\--with-pcre-jit \  
\--with-compat \  
\--add-module=/usr/src/ngx_brotli \  
\--add-dynamic-module=/usr/src/nginx-rtmp-module-$RTMP_VERSION \  
\--add-dynamic-module=/usr/src/headers-more-nginx-module-$HEADERS_MORE_VERSION
\  
" \  
&& addgroup -g $NGINX_UID -S $NGINX_USER \  
&& adduser -D -S -H -h /var/cache/nginx -u $NGINX_UID -s /sbin/nologin -G
$NGINX_USER $NGINX_USER \  
&& apk add --no-cache --virtual .build-deps \  
build-base \  
file \  
git \  
pcre-dev \  
zlib-dev \  
libressl-dev \  
linux-headers \  
curl \  
gnupg1 \  
libxslt-dev \  
gd-dev \  
geoip-dev \  
&& curl -fSLq https://nginx.org/download/nginx-$NGINX_VERSION.tar.gz -o
nginx.tar.gz \  
&& curl -fSLq https://nginx.org/download/nginx-$NGINX_VERSION.tar.gz.asc -o
nginx.tar.gz.asc \  
&& curl -fSLq https://github.com/arut/nginx-rtmp-
module/archive/v$RTMP_VERSION.tar.gz -o rtmp.tar.gz \  
&& curl -fSLq https://github.com/openresty/headers-more-nginx-
module/archive/v$HEADERS_MORE_VERSION.tar.gz -o headers.tar.gz \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$NGINX_GPG_KEYS" \  
&& gpg --batch --verify nginx.tar.gz.asc nginx.tar.gz \  
&& rm -r "$GNUPGHOME" nginx.tar.gz.asc \  
&& mkdir -p /usr/src \  
&& tar -zxC /usr/src -f nginx.tar.gz \  
&& tar -zxC /usr/src -f rtmp.tar.gz \  
&& tar -zxC /usr/src -f headers.tar.gz \  
&& rm nginx.tar.gz \  
&& rm rtmp.tar.gz \  
&& rm headers.tar.gz \  
&& cd /usr/src \  
&& git clone https://github.com/google/ngx_brotli.git \  
&& cd /usr/src/ngx_brotli \  
&& git submodule update --init \  
&& cd /usr/src/nginx-$NGINX_VERSION \  
&& export NGX_BROTLI_STATIC_MODULE_ONLY=1 \  
&& ./configure $NGINX_CONF \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& make install \  
&& rm -rf /etc/nginx/html/ \  
&& mkdir -p /etc/nginx/conf.d/ \  
&& mkdir -p /var/cache/nginx/ \  
&& mkdir -p /usr/share/nginx/html/ \  
&& install -m644 html/index.html /usr/share/nginx/html/ \  
&& install -m644 html/50x.html /usr/share/nginx/html/ \  
&& install -dm750 -o nginx -g nginx /var/cache/nginx/client_temp \  
&& install -dm750 -o nginx -g nginx /var/cache/nginx/proxy_temp \  
&& install -dm750 -o nginx -g nginx /var/cache/nginx/fastcgi_temp \  
&& install -dm750 -o nginx -g nginx /var/cache/nginx/uwsgi_temp \  
&& install -dm750 -o nginx -g nginx /var/cache/nginx/scgi_temp \  
&& ln -s /usr/lib/nginx/modules /etc/nginx/modules \  
&& strip /usr/sbin/nginx* \  
&& strip /usr/lib/nginx/modules/*.so \  
&& rm -Rf /usr/src \  
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
&& apk del .build-deps --purge \  
&& apk del .gettext --purge \  
&& mv /tmp/envsubst /usr/local/bin/ \  
\  
# add config for loading dynamic modules  
&& for module in /etc/nginx/modules/*.so; do echo "#load_module $module;" >>
/etc/nginx/conf.d/modules.conf; done \  
\  
# fix path to html files in nginx.conf  
&& sed -i "s/root html;/root \/usr\/share\/nginx\/html;/"
/etc/nginx/nginx.conf \  
\  
# forward request and error logs to docker log collector  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
EXPOSE 80 443  
  
# graceful shutdown, see https://github.com/nginxinc/docker-nginx/issues/46  
STOPSIGNAL QUIT  
  
CMD ["nginx", "-g", "daemon off;"]  

