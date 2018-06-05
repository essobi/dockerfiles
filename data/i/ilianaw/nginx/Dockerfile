FROM alpine:edge as boringssl-builder  
RUN apk update && apk add cmake gcc g++ git go ninja perl  
RUN mkdir /usr/src && git clone https://boringssl.googlesource.com/boringssl
/usr/src/boringssl \  
&& cd /usr/src/boringssl && git reset --hard
f86693dff73415efa14f154d58b6c91169b114e3  
WORKDIR /usr/src/boringssl  
COPY boringssl-*.patch /usr/src/  
RUN git -c user.name=builder -c user.email=builder@docker.invalid am
/usr/src/boringssl-*.patch  
RUN mkdir build && cd build && cmake -GNinja -DCMAKE_BUILD_TYPE=Release
-DBUILD_SHARED_LIBS=1 ..  
RUN cd build && ninja run_tests  
  
FROM alpine:edge as nginx-builder  
RUN apk update && apk add coreutils curl findutils gcc git gnupg luajit-dev
make musl-dev pcre-dev zlib-dev  
ENV NGINX_VERSION="1.13.12"  
WORKDIR /usr/src  
RUN curl -sSL -O "https://nginx.org/download/nginx-$NGINX_VERSION.tar.gz" \  
-O "https://nginx.org/download/nginx-$NGINX_VERSION.tar.gz.asc"  
# key 520A9993A1C052F8: public key "Maxim Dounin <mdounin@mdounin.ru>"  
# see https://nginx.org/en/pgp_keys.html  
COPY mdounin.asc lua-nginx-module-*.patch nginx-200-k.patch strip-debug.sh
/usr/src/  
RUN gpg --import /usr/src/mdounin.asc \  
&& gpg --batch --verify "nginx-$NGINX_VERSION.tar.gz.asc"
"nginx-$NGINX_VERSION.tar.gz" \  
&& gpg-connect-agent killagent /bye  
RUN tar xf "nginx-$NGINX_VERSION.tar.gz"  
RUN git clone https://github.com/simplresty/ngx_devel_kit && cd ngx_devel_kit
\  
&& git reset --hard 682831dbf2bf741e504ffe8d78fa9d8399033aa4 # v0.3.1rc1  
RUN git clone https://github.com/openresty/lua-nginx-module && cd lua-nginx-
module \  
&& git reset --hard 612931c0f16b02fd3b1179267cffa6bd5be6d9cf # v0.10.13  
WORKDIR /usr/src/nginx-$NGINX_VERSION  
COPY \--from=boringssl-builder /usr/src/boringssl/build/crypto/libcrypto.so
/usr/src/boringssl/build/ssl/libssl.so \  
boringssl/.openssl/lib/  
COPY \--from=boringssl-builder /usr/src/boringssl/include/openssl/*
boringssl/.openssl/include/openssl/  
RUN patch -p1 </usr/src/nginx-200-k.patch  
RUN CC="cc -flto" LUAJIT_LIB=/usr/lib LUAJIT_INC=/usr/include/luajit-2.1 \  
./configure \  
\--with-cc-opt=-I$(pwd)/boringssl/.openssl/include \  
\--with-ld-opt=-L$(pwd)/boringssl/.openssl/lib \  
\--user=nginx --group=nginx \  
\--prefix=/var/lib/nginx \  
\--sbin-path=/usr/sbin/nginx \  
\--modules-path=/usr/lib/nginx/modules \  
\--conf-path=/etc/nginx/nginx.conf \  
\--pid-path=/run/nginx/nginx.pid \  
\--lock-path=/run/nginx/nginx.lock \  
\--http-client-body-temp-path=/var/cache/nginx/client_temp \  
\--http-proxy-temp-path=/var/cache/nginx/proxy_temp \  
\--http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp \  
\--http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp \  
\--http-scgi-temp-path=/var/cache/nginx/scgi_temp \  
\--add-dynamic-module=/usr/src/ngx_devel_kit \  
\--add-dynamic-module=/usr/src/lua-nginx-module \  
\--with-http_ssl_module \  
\--with-http_v2_module \  
\--without-http_access_module \  
\--without-http_auth_basic_module \  
\--without-http_autoindex_module \  
\--without-http_browser_module \  
\--without-http_empty_gif_module \  
\--without-http_fastcgi_module \  
\--without-http_geo_module \  
\--without-http_memcached_module \  
\--without-http_referer_module \  
\--without-http_scgi_module \  
\--without-http_split_clients_module \  
\--without-http_ssi_module \  
\--without-http_upstream_hash_module \  
\--without-http_upstream_ip_hash_module \  
\--without-http_upstream_zone_module \  
\--without-http_userid_module \  
\--without-http_uwsgi_module  
RUN touch boringssl/.openssl/include/openssl/ssl.h \  
&& make -j && cat objs/ngx_modules.c  
RUN make install DESTDIR=/buildroot  
RUN mkdir -p /buildroot/usr/lib && cp boringssl/.openssl/lib/*.so
/buildroot/usr/lib/  
WORKDIR /buildroot  
RUN find -type f -executable -execdir /usr/src/strip-debug.sh {} \;  
  
FROM alpine:edge  
COPY \--from=nginx-builder /buildroot/ /  
RUN apk add --no-cache ca-certificates luajit pcre zlib \  
&& addgroup -S nginx && adduser -D -S -h /var/cache/nginx -s /sbin/nologin -G
nginx nginx \  
&& rm /etc/passwd- /etc/group- /etc/shadow- \  
&& mkdir -p /run/nginx /var/lib/nginx/logs \  
&& ln -sf /dev/stdout /var/lib/nginx/logs/access.log \  
&& ln -sf /dev/stderr /var/lib/nginx/logs/error.log \  
&& /usr/sbin/nginx -V  
ENTRYPOINT ["/usr/sbin/nginx", "-g", "daemon off;"]  

