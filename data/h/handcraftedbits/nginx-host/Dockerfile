FROM alpine:3.5  
MAINTAINER HandcraftedBits <opensource@handcraftedbits.com>  
  
ARG VERSION_NGINX=1.10.3  
ARG VERSION_NGINX_HEADERS_MORE=0.32  
  
ENV NGINX_GZIP on  
ENV NGINX_HEADERS_REMOVE Server,X-Powered-By  
ENV NGINX_KEEPALIVE_TIMEOUT 65  
ENV NGINX_PROXY_READ_TIMEOUT 120s  
ENV NGINX_RESOLVER 8.8.8.8 8.8.4.4  
ENV NGINX_TYPES_HASH_MAX_SIZE 2048  
ENV NGINX_UNIT_WAIT 2  
ENV NGINX_WORKER_PROCESSES auto  
ENV NGINX_WORKER_CONNECTIONS 768  
  
COPY data /  
  
RUN apk update && \  
apk add bash build-base certbot gd gd-dev geoip geoip-dev git libxml2 libxslt
libxml2-dev libxslt-dev netcat-openbsd \  
openssl openssl-dev pcre pcre-dev perl perl-dev wget zlib zlib-dev && \  
  
cd /tmp && \  
wget https://github.com/openresty/headers-more-nginx-
module/archive/v${VERSION_NGINX_HEADERS_MORE}.tar.gz && \  
tar -xzvf v${VERSION_NGINX_HEADERS_MORE}.tar.gz && \  
wget http://nginx.org/download/nginx-${VERSION_NGINX}.tar.gz && \  
tar -xzvf nginx-${VERSION_NGINX}.tar.gz && \  
cd nginx-${VERSION_NGINX} && \  
./configure --conf-path=/etc/nginx/nginx.conf \  
\--error-log-path=/var/log/nginx/error.log \  
\--http-client-body-temp-path=/var/lib/nginx/body \  
\--http-fastcgi-temp-path=/var/lib/nginx/fastcgi \  
\--http-log-path=/var/log/nginx/access.log \  
\--http-proxy-temp-path=/var/lib/nginx/proxy \  
\--http-scgi-temp-path=/var/lib/nginx/scgi \  
\--http-uwsgi-temp-path=/var/lib/nginx/uwsgi \  
\--lock-path=/var/lock/nginx.lock \  
\--pid-path=/run/nginx.pid \  
\--prefix=/usr/share/nginx \  
\--with-http_addition_module \  
\--with-http_auth_request_module \  
\--with-http_dav_module \  
\--with-http_degradation_module \  
\--with-http_flv_module \  
\--with-http_geoip_module \  
\--with-http_gunzip_module \  
\--with-http_gzip_static_module \  
\--with-http_image_filter_module \  
\--with-http_mp4_module \  
\--with-http_perl_module \  
\--with-http_random_index_module \  
\--with-http_realip_module \  
\--with-http_secure_link_module \  
\--with-http_slice_module \  
\--with-http_ssl_module \  
\--with-http_stub_status_module \  
\--with-http_sub_module \  
\--with-http_v2_module \  
\--with-http_xslt_module \  
\--with-ipv6 \  
\--with-mail \  
\--with-mail_ssl_module \  
\--with-pcre-jit \  
\--with-stream \  
\--with-stream_ssl_module \  
\--with-threads \  
\--add-module=/tmp/headers-more-nginx-module-${VERSION_NGINX_HEADERS_MORE} &&
\  
make install && \  
cd / && \  
rm -rf /tmp/* && \  
  
wget -O /etc/ssl/certs/chain.letsencrypt.pem
https://letsencrypt.org/certs/lets-encrypt-x1-cross-signed.pem && \  
  
ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log && \  
mkdir -p /var/lib/nginx && \  
mkdir -p /var/log/letsencrypt && \  
chmod +x /opt/container/script/renew.sh && \  
echo "0 0 * * * /opt/container/script/renew.sh" | crontab - && \  
  
apk del build-base gd-dev geoip-dev git libxml2-dev libxslt-dev openssl-dev
pcre-dev perl-dev wget zlib-dev  
  
EXPOSE 80 443  
  
CMD [ "/bin/bash", "/opt/container/script/run-nginx.sh" ]  

