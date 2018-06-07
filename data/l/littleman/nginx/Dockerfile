# Usage: As part of a kubernetes pod  
# Inspired by  
# - https://github.com/sickp/docker-alpine-
nginx/blob/master/versions/1.9.10-k8s/Dockerfile  
# - https://github.com/docker-
library/redis/commit/18e13f767bd396c53aa1f0071b218816110060ac  
#  
# Notably,  
# - The user is running as www-data  
# - Some NGINX modules aren't compiled (mail, mail-ssl, dav, flv)  
# - It's not running on alpine-kubernetes  
  
FROM alpine:edge  
MAINTAINER littleman.co <support@littleman.co>  
  
# The docker build process does not pick up changes  
ENV ITERATION 3  
RUN \  
NGINX_VERSION="1.9.15" && \  
BUILD_PKGS="build-base linux-headers openssl-dev pcre-dev wget zlib-dev" && \  
RUNTIME_PKGS="ca-certificates openssl pcre zlib" && \  
apk --update add ${BUILD_PKGS} ${RUNTIME_PKGS} && \  
cd /tmp && \  
wget http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz && \  
tar xzf nginx-${NGINX_VERSION}.tar.gz && \  
cd /tmp/nginx-${NGINX_VERSION} && \  
./configure \  
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
--user=www-data \  
--group=www-data \  
--with-http_ssl_module \  
--with-http_realip_module \  
--with-http_addition_module \  
--with-http_sub_module \  
--with-http_mp4_module \  
--with-http_gunzip_module \  
--with-http_gzip_static_module \  
--with-http_random_index_module \  
--with-http_secure_link_module \  
--with-http_stub_status_module \  
--with-http_auth_request_module \  
--with-file-aio \  
--with-ipv6 \  
--with-threads \  
--with-stream \  
--with-stream_ssl_module \  
--with-http_v2_module && \  
make && \  
make install && \  
adduser -D www-data && \  
rm -rf /tmp/* && \  
apk del ${BUILD_PKGS} && \  
rm -rf /var/cache/apk/*  
  
# Forward request and error logs to docker log collector  
RUN ln -sf /proc/self/fd/1 /var/log/nginx/access.log && \  
ln -sf /proc/self/fd/2 /var/log/nginx/error.log # stderr  
  
# Update the configuration to version 1.1  
ADD etc/nginx /etc/nginx  
  
# Bind to the host file system for better performance. See
https://github.com/nginxinc/docker-nginx/issues/19  
VOLUME ["/var/cache/nginx", "/etc/ssl/", "/etc/nginx/sites-enabled",
"/etc/nginx/conf.d/"]  
  
CMD ["nginx", "-g", "daemon off;"]  
  

