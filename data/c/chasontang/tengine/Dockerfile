FROM alpine:3.4  
  
MAINTAINER ChasonTang <chasontang@gmail.com>  
  
ENV TENGINE_VERSION 2.1.2  
ENV CONFIG "\  
\--user=nginx \  
\--group=nginx \  
\--with-file-aio \  
\--with-ipv6 \  
\--with-http_v2_module \  
\--with-http_realip_module \  
\--with-http_addition_module \  
\--with-http_sub_module \  
\--with-http_dav_module \  
\--with-http_flv_module \  
\--with-http_slice_module \  
\--with-http_mp4_module \  
\--with-http_gunzip_module \  
\--with-http_gzip_static_module \  
\--with-http_auth_request_module \  
\--with-http_concat_module \  
\--with-http_random_index_module \  
\--with-http_secure_link_module \  
\--with-http_degradation_module \  
\--with-http_sysguard_module \  
\--with-http_dyups_module \  
\--with-mail \  
\--with-mail_ssl_module \  
\--with-jemalloc \  
"  
  
ADD ngx_user.patch /  
  
RUN \  
addgroup -S nginx \  
&& adduser -D -S -h /usr/local/nginx -s /sbin/nologin -G nginx nginx \  
&& apk add --no-cache --virtual .build-deps \  
gcc \  
libc-dev \  
make \  
openssl-dev \  
pcre-dev \  
zlib-dev \  
linux-headers \  
curl \  
jemalloc-dev \  
&& curl -L
"http://tengine.taobao.org/download/tengine-$TENGINE_VERSION.tar.gz" -o
tengine.tar.gz \  
&& mkdir -p /usr/src \  
&& tar -zxC /usr/src -f tengine.tar.gz \  
&& rm tengine.tar.gz \  
&& cd /usr/src/tengine-$TENGINE_VERSION/src/os/unix/ \  
&& mv /ngx_user.patch ./ngx_user.patch \  
&& patch ngx_user.c ngx_user.patch \  
&& rm ngx_user.patch \  
&& cd ../../../ \  
# && cd /usr/src/tengine-$TENGINE_VERSION \  
&& ./configure $CONFIG --with-debug \  
&& make \  
&& mv objs/nginx objs/nginx-debug \  
&& ./configure $CONFIG \  
&& make \  
&& make install \  
&& install -m755 objs/nginx-debug /usr/local/nginx/sbin/nginx-debug \  
&& strip /usr/local/nginx/sbin/nginx* \  
&& runDeps="$( \  
scanelf --needed --nobanner /usr/local/nginx/sbin/nginx \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --virtual .nginx-rundeps $runDeps \  
&& apk del .build-deps \  
&& rm -rf /usr/src/tengine-$TENGINE_VERSION \  
# forward request and error logs to docker log collector  
&& ln -sf /dev/stdout /usr/local/nginx/logs/access.log \  
&& ln -sf /dev/stderr /usr/local/nginx/logs/error.log  
  
COPY nginx.conf /usr/local/nginx/conf/nginx.conf  
COPY nginx.vh.default.conf /usr/local/nginx/conf/conf.d/default.conf  
  
EXPOSE 80 443  
  
CMD ["/usr/local/nginx/sbin/nginx", "-g", "daemon off;"]  

