#  
#--------------------------------------------------------------------------  
# Image Setup  
#--------------------------------------------------------------------------  
#  
  
FROM alpine:latest  
  
MAINTAINER Pavel Bezrukov <bezrukov.ps@gmail.com>  
  
ENV TERM xterm  
  
ARG NGINX_VERSION=1.12.0  
ARG NGINX_PUSH_STREAM_MODULE_VERSION=0.4.1  
  
  
#####################################  
# Nginx User:  
#####################################  
  
# Add a non-root user to prevent files being created with root permissions on
host machine.  
ARG PUID=1000  
ARG PGID=1000  
RUN addgroup -g $PGID -S bitrix && \  
adduser -u $PUID -D -S -G bitrix bitrix && \  
echo "bitrix:$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c 13)" | chpasswd  
  
  
#####################################  
# Install base apps & Nginx Build:  
#####################################  
  
RUN apk -U --no-cache add openssl-dev pcre-dev zlib-dev linux-headers wget
build-base ca-certificates mc && \  
mkdir -p /tmp/src /usr/local/sbin && \  
cd /tmp/src && \  
wget https://github.com/wandenberg/nginx-push-stream-
module/archive/${NGINX_PUSH_STREAM_MODULE_VERSION}.tar.gz && \  
tar -zxf ${NGINX_PUSH_STREAM_MODULE_VERSION}.tar.gz -C /usr/local/sbin && \  
wget https://github.com/openresty/headers-more-nginx-
module/archive/master.tar.gz && \  
tar -zxf master.tar.gz -C /usr/local/sbin && \  
wget http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz && \  
tar -zxf nginx-${NGINX_VERSION}.tar.gz && \  
cd /tmp/src/nginx-${NGINX_VERSION} && \  
mkdir -p /var/cache/nginx && \  
./configure \  
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
\--user=bitrix \  
\--group=bitrix \  
\--with-compat \  
\--with-file-aio \  
\--with-threads \  
\--with-http_addition_module \  
\--with-http_auth_request_module \  
\--with-http_dav_module \  
\--with-http_flv_module \  
\--with-http_gunzip_module \  
\--with-http_gzip_static_module \  
\--with-http_mp4_module \  
\--with-http_random_index_module \  
\--with-http_realip_module \  
\--with-http_secure_link_module \  
\--with-http_slice_module \  
\--with-http_ssl_module \  
\--with-http_stub_status_module \  
\--with-http_sub_module \  
\--with-http_v2_module \  
\--with-mail \  
\--with-mail_ssl_module \  
\--with-stream \  
\--with-stream_realip_module \  
\--with-stream_ssl_module \  
\--with-stream_ssl_preread_module \  
\--add-module=/usr/local/sbin/nginx-push-stream-
module-${NGINX_PUSH_STREAM_MODULE_VERSION} \  
\--add-module=/usr/local/sbin/headers-more-nginx-module-master && \  
make && \  
make install && \  
apk del build-base && \  
mkdir -p /etc/nginx/ssl && \  
rm -rf /tmp/src && \  
rm -rf /var/cache/apk/* && \  
ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log && \  
nginx -V  
  
ADD ./bitrixenv_error/ /var/www/bitrixenv_error/  
  
ADD bx/ /etc/nginx/bx/  
ADD conf.d/ /etc/nginx/conf.d/  
ADD snippets/ /etc/nginx/snippets/  
ADD nginx.conf /etc/nginx/nginx.conf  
  
WORKDIR /home/bitrix  
  
CMD ["nginx", "-g", "daemon off;"]  
  
EXPOSE 80 443 8893 8894 8895  

