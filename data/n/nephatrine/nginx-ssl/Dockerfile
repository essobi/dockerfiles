FROM nephatrine/base-alpine:latest  
LABEL maintainer="Daniel Wolf <nephatrine@gmail.com>"  
  
RUN echo "====== RUNTIME CONFIGURATION ======" \  
&& apk --update upgrade \  
&& apk add \  
certbot \  
geoip \  
libgd \  
libxslt \  
pcre \  
&& mkdir -p /var/cache/nginx \  
\  
&& echo "====== BUILD CONFIGURATION ======" \  
&& apk add --virtual .build-nginx \  
gcc \  
gd-dev \  
geoip-dev \  
git \  
libatomic_ops-dev \  
libc-dev \  
libressl-dev \  
libxml2-dev \  
libxslt-dev \  
linux-headers \  
make \  
pcre-dev \  
zlib-dev \  
\  
&& echo "====== COMPILE NGINX ======" \  
&& cd /usr/src \  
&& git clone https://github.com/nginx/nginx.git && cd nginx \  
&& ./auto/configure \  
--prefix=/var/www \  
--sbin-path=/usr/sbin/nginx \  
--modules-path=/usr/lib/nginx/modules \  
--conf-path=/etc/nginx/nginx.conf \  
--error-log-path=/var/log/nginx/error.log \  
--pid-path=/var/run/nginx.pid \  
--lock-path=/var/run/nginx.lock \  
--user=guardian \  
--group=users \  
--with-threads \  
--with-file-aio \  
--with-http_ssl_module \  
--with-http_v2_module \  
--with-http_realip_module \  
--with-http_addition_module \  
--with-http_xslt_module=dynamic \  
--with-http_image_filter_module=dynamic \  
--with-http_geoip_module=dynamic \  
--with-http_sub_module \  
--with-http_dav_module \  
--with-http_flv_module \  
--with-http_mp4_module \  
--with-http_gunzip_module \  
--with-http_gzip_static_module \  
--with-http_auth_request_module \  
--with-http_random_index_module \  
--with-http_secure_link_module \  
--with-http_degradation_module \  
--with-http_slice_module \  
--with-http_stub_status_module \  
--http-log-path=/var/log/nginx/access.log \  
--http-client-body-temp-path=/var/cache/nginx/client_body \  
--http-proxy-temp-path=/var/cache/nginx/proxy \  
--http-fastcgi-temp-path=/var/cache/nginx/fastcgi \  
--http-uwsgi-temp-path=/var/cache/nginx/uwsgi \  
--http-scgi-temp-path=/var/cache/nginx/scgi \  
--with-mail=dynamic \  
--with-mail_ssl_module \  
--with-stream=dynamic \  
--with-stream_ssl_module \  
--with-stream_realip_module \  
--with-stream_geoip_module=dynamic \  
--with-stream_ssl_preread_module \  
--with-compat \  
--with-pcre \  
--with-pcre-jit \  
--with-libatomic \  
&& make -j4 && make install \  
&& strip /usr/sbin/nginx \  
&& strip /usr/lib/nginx/modules/*.so \  
\  
&& echo "====== CLEANUP ======" \  
&& cd /usr/src \  
&& apk del --purge .build-nginx \  
&& rm -rf \  
/tmp/* \  
/usr/src/* \  
/var/cache/apk/*  
  
EXPOSE 80/tcp 443/tcp  
COPY override /

