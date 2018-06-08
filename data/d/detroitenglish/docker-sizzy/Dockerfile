# FROM node:slim  
FROM node:alpine  
COPY . /usr/sizzy  
ENV NGINX_VERSION 1.13.1  
ENV NGX_BROTLI_COMMIT bfd2885b2da4d763fed18f49216bb935223cd34b  
  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories \  
&& echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
&& echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories \  
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
autoconf \  
libtool \  
automake \  
git \  
g++ \  
cmake \  
alpine-sdk \  
bash \  
diffutils \  
elfutils-dev \  
m4 \  
python \  
ncurses \  
ocaml \  
opam \  
&& opam init -y \  
&& eval `opam config env` \  
&& opam update \  
&& opam install -y ocamlfind sedlex \  
&& git clone --depth 1 --branch "v0.45.0" https://github.com/facebook/flow.git
\  
&& cd flow \  
&& yarn \  
&& make \  
&& cp bin/flow /usr/bin/flow \  
&& apk add --no-cache elfutils-libelf \  
&& cd .. \  
&& rm -rf flow \  
&& cd /usr/sizzy \  
&& yarn \  
&& sed -i "s@\"flow\":\s\"flow\"@\"flow\": \"/usr/bin/flow\"@" package.json \  
&& yarn build \  
&& mkdir -p /var/www/app \  
&& mv /usr/sizzy/build/* /var/www/app \  
&& mv /usr/sizzy/brotlify.sh /var/www/app \  
&& addgroup -S nginx \  
&& adduser -D -S -h /var/cache/nginx -s /sbin/nologin -G nginx nginx \  
&& chown -R nginx:nginx /var/www/app \  
&& cd /var/www \  
&& sed -i "s@\!function.*view\")@console.log('analytics? nein danke.')@"
/var/www/app/index.html \  
&& rm -fr /usr/sizzy \  
&& cd /usr \  
&& git clone https://github.com/google/brotli.git \  
&& cd brotli \  
&& make \  
&& cp bin/brotli /usr/bin/brotli \  
&& cd .. \  
&& rm -fr brotli \  
&& cd /var/www/app \  
&& ./brotlify.sh \  
&& rm brotlify.sh \  
&& yarn cache clean \  
&& rm /usr/bin/flow /usr/bin/brotli \  
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
\--http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp \  
\--http-scgi-temp-path=/var/cache/nginx/scgi_temp \  
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
\--with-http_perl_module=dynamic \  
\--with-threads \  
\--with-stream \  
\--with-stream_ssl_module \  
\--with-http_slice_module \  
\--with-mail \  
\--with-mail_ssl_module \  
\--with-file-aio \  
\--with-http_v2_module \  
\--with-ipv6 \  
\--add-module=/usr/src/ngx_brotli \  
\--with-cc-opt=-Wno-error \  
" \  
&& mkdir -p /usr/src \  
&& cd /usr/src \  
&& git clone --recursive https://github.com/google/ngx_brotli.git \  
&& cd ngx_brotli \  
&& git checkout -b $NGX_BROTLI_COMMIT $NGX_BROTLI_COMMIT \  
&& cd .. \  
&& curl -fSL http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz -o
nginx.tar.gz \  
&& curl -fSL http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz.asc -o
nginx.tar.gz.asc \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_KEYS" \  
&& gpg --batch --verify nginx.tar.gz.asc nginx.tar.gz \  
&& mkdir -p /usr/src \  
&& tar -zxC /usr/src -f nginx.tar.gz \  
&& rm nginx.tar.gz \  
&& cd /usr/src/nginx-$NGINX_VERSION \  
&& ./configure $CONFIG --with-debug \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& mv objs/nginx objs/nginx-debug \  
&& mv objs/ngx_http_xslt_filter_module.so objs/ngx_http_xslt_filter_module-
debug.so \  
&& mv objs/ngx_http_image_filter_module.so objs/ngx_http_image_filter_module-
debug.so \  
&& mv objs/ngx_http_geoip_module.so objs/ngx_http_geoip_module-debug.so \  
&& mv objs/ngx_http_perl_module.so objs/ngx_http_perl_module-debug.so \  
&& ./configure $CONFIG \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& make install \  
&& rm -rf /etc/nginx/html/ \  
&& mkdir /etc/nginx/conf.d/ \  
&& mkdir -p /usr/share/nginx/html/ \  
&& install -m644 html/index.html /usr/share/nginx/html/ \  
&& install -m644 html/50x.html /usr/share/nginx/html/ \  
&& install -m755 objs/nginx-debug /usr/sbin/nginx-debug \  
&& install -m755 objs/ngx_http_xslt_filter_module-debug.so
/usr/lib/nginx/modules/ngx_http_xslt_filter_module-debug.so \  
&& install -m755 objs/ngx_http_image_filter_module-debug.so
/usr/lib/nginx/modules/ngx_http_image_filter_module-debug.so \  
&& install -m755 objs/ngx_http_geoip_module-debug.so
/usr/lib/nginx/modules/ngx_http_geoip_module-debug.so \  
&& install -m755 objs/ngx_http_perl_module-debug.so
/usr/lib/nginx/modules/ngx_http_perl_module-debug.so \  
&& ln -s ../../usr/lib/nginx/modules /etc/nginx/modules \  
&& strip /usr/sbin/nginx* \  
&& strip /usr/lib/nginx/modules/*.so \  
&& rm -rf /usr/src/nginx-$NGINX_VERSION \  
&& rm -rf /usr/src/ngx_brotli \  
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
# forward request and error logs to docker log collector  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
COPY sizzy.nginx.conf /etc/nginx/nginx.conf  
EXPOSE 80  
CMD ["nginx", "-g", "daemon off;"]  

