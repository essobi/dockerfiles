FROM alpine:latest  
  
MAINTAINER nullity  
ENV UNAME www-data  
  
ENV CONFIG "\  
--prefix=/etc/nginx \  
--sbin-path=/usr/sbin/nginx \  
--modules-path=/usr/lib/nginx/modules \  
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
--user=$UNAME \  
--group=$UNAME \  
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
--with-http_auth_request_module \  
--with-http_stub_status_module \  
--with-http_geoip_module=dynamic \  
--with-threads \  
--with-stream \  
--with-stream_ssl_module \  
--with-http_slice_module \  
--with-mail \  
--with-mail_ssl_module \  
--with-file-aio \  
--with-http_v2_module \  
--with-ipv6 \  
--with-ld-opt='-Wl,-rpath,/usr/local/lib' \  
--add-module=ngx_devel_kit \  
--add-module=lua-nginx-module \  
--add-module=ngx-fancyindex \  
"  
  
RUN \  
addgroup -g 82 -S $UNAME \  
&& adduser -D -u 82 -S -h /var/cache/nginx -s /sbin/nologin -G $UNAME $UNAME \  
&& apk add --no-cache --virtual .build-deps \  
gcc \  
libc-dev \  
make \  
openssl-dev \  
pcre-dev \  
zlib-dev \  
linux-headers \  
curl \  
wget \  
gnupg \  
libxslt-dev \  
gd-dev \  
geoip-dev \  
perl-dev \  
git \  
&& mkdir /usr/src \  
&& cd /usr/src/ \  
&& wget $(curl -s https://api.github.com/repos/nginx/nginx/tags | grep
tarball_url | head -n 1 | cut -d '"' -f 4) -O- | tar xfz - \  
&& cd nginx-nginx* \  
&& git clone https://github.com/aperezdc/ngx-fancyindex.git \  
&& git clone https://github.com/simpl/ngx_devel_kit \  
&& git clone https://github.com/openresty/lua-nginx-module \  
&& git clone -b v2.1 http://luajit.org/git/luajit-2.0.git \  
&& cd luajit* \  
&& make install \  
&& export LUAJIT_LIB=/usr/local/lib \  
&& export LUAJIT_INC=/usr/local/include/luajit-2.1 \  
&& ln -sf luajit-2.1.0-beta2 /usr/local/bin/luajit \  
&& cd .. \  
&& auto/configure $CONFIG --with-debug \  
&& make \  
&& mv objs/nginx objs/nginx-debug \  
&& mv objs/ngx_http_geoip_module.so objs/ngx_http_geoip_module-debug.so \  
&& auto/configure $CONFIG \  
&& make -j"$(getconf _NPROCESSORS_ONLN)"\  
&& make install \  
&& rm -rf /etc/nginx/html/ \  
&& mkdir /etc/nginx/conf.d/ \  
&& mkdir -p /usr/share/nginx/html/ \  
&& install -m644 docs/html/index.html /usr/share/nginx/html/ \  
&& install -m644 docs/html/50x.html /usr/share/nginx/html/ \  
&& install -m755 objs/nginx-debug /usr/sbin/nginx-debug \  
&& install -m755 objs/ngx_http_geoip_module-debug.so
/usr/lib/nginx/modules/ngx_http_geoip_module-debug.so \  
&& ln -s ../../usr/lib/nginx/modules /etc/nginx/modules \  
&& strip /usr/sbin/nginx* \  
&& strip /usr/lib/nginx/modules/*.so \  
&& runDeps="$( \  
scanelf --needed --nobanner /usr/sbin/nginx /usr/lib/nginx/modules/*.so \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --virtual .nginx-rundeps $runDeps \  
&& apk del .build-deps \  
&& rm -rf /usr/src/nginx-nginx* \  
&& apk add --no-cache gettext libgcc \  
\  
# forward request and error logs to docker log collector  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY nginx.vh.default.conf /etc/nginx/conf.d/default.conf  
  
EXPOSE 80 443  
  
CMD ["nginx", "-g", "daemon off;"]  

